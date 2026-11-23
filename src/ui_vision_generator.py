"""
Universal Multimodal Vision-to-Code Generative Engine
Supports:
1. Groq (Free, Ultra-Fast LLaMA 3.2 Vision: llama-3.2-11b-vision-preview, llama-3.2-90b-vision-preview)
2. OpenRouter (Free Vision Models: meta-llama/llama-3.2-11b-vision-instruct:free, etc.)
3. OpenAI (GPT-4o, GPT-4o-mini)
4. Google Gemini (gemini-3.8-flash, gemini-2.0-flash-exp)
5. Built-in Offline Fallback
"""

import os
import io
import time
import base64
import requests
from PIL import Image
from typing import Tuple, Dict, Any, Optional

from src.prompt_templates import (
    SKETCH_TO_CODE_SYSTEM_PROMPT,
    REFINEMENT_SYSTEM_PROMPT,
    STYLE_PRESETS
)


AI_PROVIDERS = {
    "Groq (Free & Ultra-Fast)": {
        "base_url": "https://api.groq.com/openai/v1/chat/completions",
        "default_model": "qwen/qwen3.8-27b",
        "models": ["qwen/qwen3.8-27b"],
        "key_link": "https://console.groq.com/keys"
    },
    "OpenRouter (Free Models)": {
        "base_url": "https://openrouter.ai/api/v1/chat/completions",
        "default_model": "meta-llama/llama-3.2-11b-vision-instruct:free",
        "models": [
            "meta-llama/llama-3.2-11b-vision-instruct:free",
            "qwen/qwen-2-vl-72b-instruct",
            "google/gemini-2.0-flash-exp:free"
        ],
        "key_link": "https://openrouter.ai/keys"
    },
    "OpenAI (GPT-4o)": {
        "base_url": "https://api.openai.com/v1/chat/completions",
        "default_model": "gpt-4o-mini",
        "models": ["gpt-4o-mini", "gpt-4o"],
        "key_link": "https://platform.openai.com/api-keys"
    },
    "Google Gemini": {
        "base_url": "gemini",
        "default_model": "gemini-3.8-flash",
        "models": ["gemini-3.8-flash", "gemini-3.8-flash-lite", "gemini-2.0-flash-exp"],
        "key_link": "https://aistudio.google.com/app/apikey"
    }
}


class UIVisionGenerator:
    """
    Universal Vision-to-Code Generator supporting OpenAI-compatible APIs
    (Groq, OpenRouter, OpenAI) as well as Google Gemini and Local Fallback.
    """

    PROVIDERS = AI_PROVIDERS

    def __init__(
        self,
        provider: str = "Groq (Free & Ultra-Fast)",
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ):
        self.provider = provider if provider in self.PROVIDERS else "Groq (Free & Ultra-Fast)"
        self.api_key = (api_key or "").strip()
        provider_info = self.PROVIDERS[self.provider]
        self.model_name = model_name if model_name else provider_info["default_model"]

    def test_connection(self) -> Tuple[bool, str]:
        """Tests API connectivity with a lightweight text ping."""
        if not self.api_key:
            return False, f"Please enter your {self.provider} API key first!"

        # Google Gemini test
        if self.provider == "Google Gemini":
            try:
                from google import genai
                c = genai.Client(api_key=self.api_key)
                resp = c.models.generate_content(model=self.model_name, contents="Ping. Reply with 'OK'.")
                return True, f"Connected to {self.model_name}!"
            except Exception as e:
                return False, f"Gemini Error: {str(e)[:150]}"

        # OpenAI-compatible test (Groq, OpenRouter, OpenAI)
        provider_info = self.PROVIDERS[self.provider]
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": "Reply with 'OK'."}],
            "max_tokens": 10
        }

        try:
            resp = requests.post(provider_info["base_url"], headers=headers, json=payload, timeout=10)
            if resp.status_code == 200:
                return True, f"Connected to {self.provider} ({self.model_name}) successfully!"
            else:
                err_data = resp.json().get("error", resp.text)
                return False, f"HTTP {resp.status_code}: {err_data}"
        except Exception as e:
            return False, f"Connection Failed: {str(e)[:150]}"

    def generate_ui_from_sketch(
        self,
        image: Image.Image,
        style_preset: str = "Modern Clean",
        user_notes: str = ""
    ) -> Tuple[str, Dict[str, Any]]:
        """Translates wireframe image into HTML5 + Tailwind CSS code."""
        start_time = time.time()
        style_instruction = STYLE_PRESETS.get(style_preset, STYLE_PRESETS["Modern Clean"])

        combined_prompt = f"""{SKETCH_TO_CODE_SYSTEM_PROMPT}

### DESIGN THEME PRESET:
{style_instruction}

### USER-SPECIFIED CUSTOM DETAILS / HINTS:
{user_notes if user_notes.strip() else "None provided. Faithfully follow the exact spatial layout and handwritten text in the sketch."}

Now, carefully inspect the provided wireframe image and synthesize the complete, pixel-faithful HTML5 + Tailwind CSS code:
"""

        # If API key is provided, execute multimodal vision call
        if self.api_key:
            try:
                raw_html = self._call_vision_api(image, combined_prompt)
                latency = round(time.time() - start_time, 2)
                return raw_html, {
                    "engine": f"{self.provider} ({self.model_name})",
                    "latency_sec": latency,
                    "status": "success",
                    "mode": f"Live VLM ({self.model_name})",
                    "is_live_vlm": True,
                    "error": None
                }
            except Exception as e:
                error_msg = str(e)
                print(f"Vision API call failed: {error_msg}")
                raw_html = self._synthesize_offline(image, style_preset, user_notes)
                latency = round(time.time() - start_time, 2)
                return raw_html, {
                    "engine": "Local Structural Fallback Synthesizer",
                    "latency_sec": latency,
                    "status": "error_fallback",
                    "mode": "Offline Heuristic Fallback (Due to API Error)",
                    "is_live_vlm": False,
                    "error": error_msg
                }

        # Offline fallback if no key provided
        raw_html = self._synthesize_offline(image, style_preset, user_notes)
        latency = round(time.time() - start_time, 2)
        return raw_html, {
            "engine": "Local Structural Fallback Synthesizer",
            "latency_sec": latency,
            "status": "offline_no_key",
            "mode": "Offline Heuristic Fallback (No Key Provided)",
            "is_live_vlm": False,
            "error": "No API key entered in sidebar."
        }

    def _call_vision_api(self, image: Image.Image, prompt: str) -> str:
        """Dispatches multimodal vision request to the selected provider."""
        # Convert PIL image to base64 JPEG
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG", quality=90)
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        data_url = f"data:image/jpeg;base64,{img_base64}"

        # 1. Google Gemini Provider
        if self.provider == "Google Gemini":
            from google import genai
            from google.genai import types
            c = genai.Client(api_key=self.api_key)
            resp = c.models.generate_content(
                model=self.model_name,
                contents=[
                    types.Part.from_bytes(data=buffered.getvalue(), mime_type="image/jpeg"),
                    prompt
                ],
                config=types.GenerateContentConfig(temperature=0.1)
            )
            return resp.text

        # 2. OpenAI-Compatible Provider (Groq, OpenRouter, OpenAI)
        provider_info = self.PROVIDERS[self.provider]
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url
                            }
                        }
                    ]
                }
            ],
            "temperature": 0.1,
            "max_tokens": 4096
        }

        response = requests.post(provider_info["base_url"], headers=headers, json=payload, timeout=45)
        if response.status_code != 200:
            err_details = response.json().get("error", response.text)
            raise RuntimeError(f"HTTP {response.status_code}: {err_details}")

        data = response.json()
        return data["choices"][0]["message"]["content"]

    def refine_ui_code(
        self,
        current_html: str,
        refinement_instruction: str
    ) -> Tuple[str, Dict[str, Any]]:
        """Applies conversational revisions to existing generated HTML code."""
        start_time = time.time()
        prompt = f"""{REFINEMENT_SYSTEM_PROMPT}

### USER REVISION REQUEST:
{refinement_instruction}

### CURRENT HTML CODE:
{current_html}

Output the updated, complete HTML code:
"""

        if self.api_key:
            try:
                if self.provider == "Google Gemini":
                    from google import genai
                    c = genai.Client(api_key=self.api_key)
                    resp = c.models.generate_content(model=self.model_name, contents=prompt)
                    updated_html = resp.text
                else:
                    provider_info = self.PROVIDERS[self.provider]
                    headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
                    payload = {
                        "model": self.model_name,
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.1
                    }
                    resp = requests.post(provider_info["base_url"], headers=headers, json=payload, timeout=30)
                    updated_html = resp.json()["choices"][0]["message"]["content"]

                latency = round(time.time() - start_time, 2)
                return updated_html, {
                    "engine": f"{self.provider} Refinement",
                    "latency_sec": latency,
                    "status": "success"
                }
            except Exception as e:
                print(f"Online refinement failed ({e}). Performing local rule refinement.")

        updated_html = self._apply_offline_refinement(current_html, refinement_instruction)
        latency = round(time.time() - start_time, 2)
        return updated_html, {
            "engine": "Local Rule Refinement",
            "latency_sec": latency,
            "status": "success (offline fallback)"
        }

    def _synthesize_offline(self, image: Image.Image, style: str, notes: str) -> str:
        """Fallback generator when offline."""
        w, h = image.size
        aspect = w / h

        notes_lower = notes.lower()
        if "card" in notes_lower or "product" in notes_lower or "shop" in notes_lower:
            return self._template_product_card(style)
        elif "dashboard" in notes_lower or "analytics" in notes_lower or "stats" in notes_lower:
            return self._template_dashboard(style)
        elif "login" in notes_lower or "auth" in notes_lower or "sign" in notes_lower:
            return self._template_login_form(style)
        elif "landing" in notes_lower or "hero" in notes_lower or "home" in notes_lower:
            return self._template_landing_page(style)
        elif aspect < 0.85:
            return self._template_login_form(style)
        elif aspect > 1.3:
            return self._template_dashboard(style)
        else:
            return self._template_landing_page(style)

    def _apply_offline_refinement(self, html: str, instruction: str) -> str:
        inst = instruction.lower()
        if "dark" in inst:
            html = html.replace("bg-slate-50", "bg-slate-900").replace("bg-white", "bg-slate-800")
            html = html.replace("text-slate-900", "text-white").replace("text-slate-800", "text-slate-100")
        elif "emerald" in inst or "green" in inst:
            html = html.replace("indigo-600", "emerald-600").replace("indigo-700", "emerald-700")
        elif "red" in inst or "crimson" in inst:
            html = html.replace("indigo-600", "rose-600").replace("indigo-700", "rose-700")
        elif "rounded" in inst:
            html = html.replace("rounded-lg", "rounded-2xl").replace("rounded-md", "rounded-xl")
        return html

    def _template_login_form(self, style: str) -> str:
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe Auth Screen</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-gradient-to-br from-slate-100 via-indigo-50 to-slate-200 min-h-screen flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl w-full max-w-md p-8 border border-slate-100">
        <div class="text-center mb-8">
            <div class="w-14 h-14 bg-indigo-600 text-white rounded-xl flex items-center justify-center mx-auto mb-3 shadow-md shadow-indigo-200">
                <i class="fa-solid fa-layer-group text-2xl"></i>
            </div>
            <h2 class="text-2xl font-bold text-slate-900">Welcome Back</h2>
            <p class="text-sm text-slate-500 mt-1">Please enter your credentials to access your account</p>
        </div>
        <form class="space-y-5">
            <div>
                <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Email Address</label>
                <input type="email" placeholder="name@company.com" required 
                       class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition">
            </div>
            <div>
                <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Password</label>
                <input type="password" placeholder="••••••••" required 
                       class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition">
            </div>
            <button type="button" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2.5 rounded-lg shadow-md transition">
                Sign In
            </button>
        </form>
    </div>
</body>
</html>"""

    def _template_dashboard(self, style: str) -> str:
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe Analytics Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 text-slate-800 flex min-h-screen">
    <aside class="w-64 bg-white border-r border-slate-200 p-6 hidden md:flex flex-col justify-between">
        <span class="font-bold text-lg text-slate-900">ApexAnalytics</span>
        <nav class="space-y-2">
            <a href="#" class="block px-3 py-2 bg-indigo-50 text-indigo-600 rounded-lg font-medium text-sm">Dashboard</a>
            <a href="#" class="block px-3 py-2 text-slate-600 hover:bg-slate-50 rounded-lg font-medium text-sm">Settings</a>
        </nav>
    </aside>
    <main class="flex-1 p-8">
        <h1 class="text-2xl font-bold text-slate-900 mb-6">Performance Metrics</h1>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <span class="text-xs text-slate-400 uppercase">Revenue</span>
                <h3 class="text-3xl font-extrabold text-slate-900 mt-2">$84,230</h3>
            </div>
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <span class="text-xs text-slate-400 uppercase">Users</span>
                <h3 class="text-3xl font-extrabold text-slate-900 mt-2">12,450</h3>
            </div>
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <span class="text-xs text-slate-400 uppercase">Conversion</span>
                <h3 class="text-3xl font-extrabold text-slate-900 mt-2">3.82%</h3>
            </div>
        </div>
    </main>
</body>
</html>"""

    def _template_product_card(self, style: str) -> str:
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe Product Card</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-100 min-h-screen flex items-center justify-center p-6">
    <div class="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden max-w-sm w-full p-6">
        <div class="h-48 bg-slate-200 rounded-xl mb-4 flex items-center justify-center text-slate-400">
            [ Product Image ]
        </div>
        <h3 class="text-lg font-bold text-slate-900">Studio Wireless Headphones</h3>
        <p class="text-sm text-slate-500 mt-1">Active noise cancellation with 40h battery life.</p>
        <div class="mt-4 flex items-center justify-between">
            <span class="text-2xl font-bold text-slate-900">$279.00</span>
            <button class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-xl text-sm font-medium">Add to Cart</button>
        </div>
    </div>
</body>
</html>"""

    def _template_landing_page(self, style: str) -> str:
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe SaaS Landing Page</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 text-slate-800">
    <header class="bg-white border-b border-slate-200 px-6 py-4 flex justify-between items-center">
        <span class="font-extrabold text-lg text-slate-900">Synthetix</span>
        <button class="bg-indigo-600 text-white text-sm font-medium px-4 py-2 rounded-lg">Get Started</button>
    </header>
    <section class="max-w-4xl mx-auto px-6 py-20 text-center">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-4">Transform Sketches into Live UI</h1>
        <p class="text-slate-600 mb-8">Multimodal vision-to-code synthesis in real-time.</p>
        <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-6 py-3 rounded-xl">Try Demo</button>
    </section>
</body>
</html>"""
