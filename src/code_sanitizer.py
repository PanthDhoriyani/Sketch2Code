"""
Code Sanitizer and DOM Validator for Synthesized HTML
Part of the Wireframe Sketch-to-Live UI Capstone Project
"""

import re
from bs4 import BeautifulSoup
from typing import Tuple, Dict, Any


class CodeSanitizer:
    """
    Cleans raw LLM markdown outputs, enforces valid HTML5 DOM structure,
    injects required Tailwind CDN & FontAwesome headers, and beautifies code.
    """

    TAILWIND_CDN = '<script src="https://cdn.tailwindcss.com"></script>'
    FONTAWESOME_CDN = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
    INTER_FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap">'

    @classmethod
    def clean_and_sanitize(cls, raw_code: str) -> Tuple[str, Dict[str, Any]]:
        """
        Takes raw string from model (which might contain markdown ```html blocks)
        and guarantees clean, complete, standalone HTML5.
        """
        # 1. Strip markdown code fences if present
        cleaned = raw_code.strip()
        if "```" in cleaned:
            # Match code inside ```html ... ``` or ``` ... ```
            match = re.search(r"```(?:html)?\s*(.*?)\s*```", cleaned, re.DOTALL | re.IGNORECASE)
            if match:
                cleaned = match.group(1).strip()
            else:
                cleaned = re.sub(r"^```[a-zA-Z]*", "", cleaned)
                cleaned = re.sub(r"```$", "", cleaned).strip()

        # 2. Parse with BeautifulSoup to validate/fix DOM
        soup = BeautifulSoup(cleaned, "html.parser")

        # 3. Ensure <html> and <body> exist
        if not soup.find("html"):
            wrapper = BeautifulSoup(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe Synthesized UI</title>
</head>
<body class="bg-slate-50 min-h-screen">
</body>
</html>""", "html.parser")
            body = wrapper.find("body")
            for elem in soup.contents:
                body.append(elem)
            soup = wrapper

        # 4. Inject required CDNs into <head> if missing
        head = soup.find("head")
        if not head:
            head = soup.new_tag("head")
            soup.html.insert(0, head)

        head_html = str(head)
        if "cdn.tailwindcss.com" not in head_html:
            tw_tag = BeautifulSoup(cls.TAILWIND_CDN, "html.parser")
            head.append(tw_tag)

        if "font-awesome" not in head_html and "fontawesome" not in head_html:
            fa_tag = BeautifulSoup(cls.FONTAWESOME_CDN, "html.parser")
            head.append(fa_tag)

        # 5. Format / Beautify HTML
        formatted_html = soup.prettify()

        stats = {
            "num_tags": len(soup.find_all()),
            "has_head": bool(soup.find("head")),
            "has_body": bool(soup.find("body")),
            "tailwind_enabled": True,
            "fontawesome_enabled": True
        }

        return formatted_html, stats
