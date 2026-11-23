"""
Sketch2Code: Wireframe to Live UI Studio
Generative AI Capstone Project — Final Jury Defense
Author: 4th Year B.Tech / BE Computer Science Student
"""

import os
import sys
import time
from PIL import Image
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# Ensure local imports work reliably
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Auto-load local .env if present (ignored by git)
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(env_path):
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    except Exception:
        pass

from src.sketch_preprocessor import SketchPreprocessor
from src.ui_vision_generator import UIVisionGenerator, AI_PROVIDERS
from src.code_sanitizer import CodeSanitizer
from src.sketch_metrics import UIBenchmarkMetrics
from src.prompt_templates import STYLE_PRESETS

# Page Configuration
st.set_page_config(
    page_title="Sketch2Code: Wireframe to Live UI Studio",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for modern academic & engineering presentation
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4F46E5 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #64748B;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 0.75rem;
        padding: 1rem;
        text-align: center;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #4F46E5;
    }
    .metric-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        color: #64748B;
        font-weight: 600;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown("<div class='main-header'>📐 Sketch2Code: Wireframe-to-Live UI Studio</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'><b>Generative AI Capstone Project</b> | Multimodal Vision-to-Code Synthesis & Real-Time DOM Generation</div>", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "current_html" not in st.session_state:
    st.session_state.current_html = ""
if "processed_image" not in st.session_state:
    st.session_state.processed_image = None
if "generation_metadata" not in st.session_state:
    st.session_state.generation_metadata = {}
if "eval_metrics" not in st.session_state:
    st.session_state.eval_metrics = {}

# --- SIDEBAR CONTROLS ---
st.sidebar.header("⚙️ Studio Controls")

# Input Source
input_mode = st.sidebar.radio(
    "1. Wireframe Source",
    options=["Select Curated Benchmark Sample", "Upload Custom Sketch / Image"],
    index=0
)

uploaded_img = None
sample_notes = ""

if input_mode == "Select Curated Benchmark Sample":
    sample_choice = st.sidebar.selectbox(
        "Choose Wireframe Scenario",
        options=[
            "Login Screen (Auth Form)",
            "E-Commerce Showcase Card",
            "Analytics Dashboard with Metrics",
            "SaaS Landing Page (Hero + Features)"
        ]
    )
    sample_mapping = {
        "Login Screen (Auth Form)": ("samples/login_wireframe.png", "login auth screen with credentials and social button"),
        "E-Commerce Showcase Card": ("samples/ecommerce_card.png", "product card with headphones, rating, and add to cart"),
        "Analytics Dashboard with Metrics": ("samples/dashboard_wireframe.png", "analytics dashboard with KPI cards and sidebar"),
        "SaaS Landing Page (Hero + Features)": ("samples/saas_landing_wireframe.png", "landing page with hero CTA and 3-column feature grid")
    }
    sample_path, sample_notes = sample_mapping[sample_choice]
    if os.path.exists(sample_path):
        uploaded_img = Image.open(sample_path)
else:
    file_upload = st.sidebar.file_uploader("Upload Wireframe Photo (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
    if file_upload:
        uploaded_img = Image.open(file_upload)
        sample_notes = st.sidebar.text_input("Optional Sketch Hint", placeholder="e.g. signup form with avatar")

st.sidebar.markdown("---")

# Preprocessing Controls
st.sidebar.subheader("🖼️ Vision Preprocessing")
apply_enhancement = st.sidebar.checkbox("Stroke Enhancement (Contrast & Sharpness)", value=True)
apply_denoise = st.sidebar.checkbox("Auto-Denoise Background", value=True)
view_binarized = st.sidebar.checkbox("Inspect Binarized Line Edges", value=False)

# Styling Presets
st.sidebar.subheader("🎨 UI Theme & Styling")
selected_style = st.sidebar.selectbox("Design Preset", options=list(STYLE_PRESETS.keys()), index=0)

# Model Settings
st.sidebar.subheader("🤖 Multimodal Vision Engine")
selected_provider = st.sidebar.selectbox(
    "1. Select AI Provider",
    options=list(AI_PROVIDERS.keys()),
    index=0,
    help="Groq offers completely free, ultra-fast LLaMA 3.2 Vision with zero 503 traffic blocks."
)
provider_info = AI_PROVIDERS[selected_provider]

# Helper to fetch secrets from Streamlit Cloud Secrets or os.environ
def get_secret(key: str, default: str = "") -> str:
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    return os.environ.get(key, default)

default_key = ""
if selected_provider == "Groq (Free & Ultra-Fast)":
    default_key = get_secret("GROQ_API_KEY", "")
elif selected_provider == "Google Gemini":
    default_key = get_secret("GEMINI_API_KEY", "")
elif selected_provider == "OpenRouter (All Models)":
    default_key = get_secret("OPENROUTER_API_KEY", "")
elif selected_provider == "OpenAI (GPT-4o Vision)":
    default_key = get_secret("OPENAI_API_KEY", "")

api_key_input = st.sidebar.text_input(
    f"{selected_provider.split(' ')[0]} API Key",
    value=default_key,
    type="password",
    help=f"Get your key from {provider_info['key_link']}"
)

selected_model = st.sidebar.selectbox(
    "Vision Model",
    options=provider_info["models"],
    index=0,
    help="Active vision model for this provider."
)

col_test_btn, col_link = st.sidebar.columns([1.2, 1])
with col_test_btn:
    test_key_clicked = st.button("🔍 Test Key", use_container_width=True)
with col_link:
    st.markdown(f"[Free Key ↗]({provider_info['key_link']})", unsafe_allow_html=True)

if test_key_clicked:
    if not api_key_input.strip():
        st.sidebar.error("Please enter a key first!")
    else:
        with st.sidebar.status(f"Testing {selected_provider}..."):
            tester = UIVisionGenerator(provider=selected_provider, api_key=api_key_input, model_name=selected_model)
            ok, msg = tester.test_connection()
            if ok:
                st.sidebar.success(msg)
            else:
                st.sidebar.error(msg)

force_offline = st.sidebar.checkbox("Force Offline Heuristic Mode", value=False, help="Runs local structure synthesizer without internet calls.")

# Action Button
st.sidebar.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.sidebar.button("🚀 Synthesize Live UI", type="primary", use_container_width=True)

# --- MAIN WORKBENCH SPLIT-SCREEN ---
col_left, col_right = st.columns([1, 1.4], gap="medium")

# --- LEFT COLUMN: VISION PERCEPTION ---
with col_left:
    st.subheader("1. Wireframe Perception & Preprocessing")
    if uploaded_img is not None:
        # Preprocess
        proc_img, meta = SketchPreprocessor.auto_standardize(uploaded_img)
        if apply_enhancement:
            proc_img = SketchPreprocessor.enhance_sketch(proc_img, denoise=apply_denoise)
        if view_binarized:
            display_img = SketchPreprocessor.binarize_sketch(proc_img)
        else:
            display_img = proc_img

        st.session_state.processed_image = proc_img
        st.image(display_img, caption=f"Perception Input ({meta['processed_resolution']})", use_container_width=True)

        with st.expander("🔍 Image Preprocessing Telemetry", expanded=False):
            st.write(f"- **Original Resolution:** `{meta['original_resolution']}`")
            st.write(f"- **Processed Dimensions:** `{meta['processed_resolution']}`")
            st.write(f"- **Aspect Ratio:** `{meta['aspect_ratio']}`")
            st.write(f"- **Scaling Factor:** `{meta['scaling_ratio']}`")
            st.write(f"- **Stroke Enhancement:** `{'Active' if apply_enhancement else 'Disabled'}`")
    else:
        st.info("👈 Please select a sample or upload a wireframe sketch to begin.")

# --- SYNTHESIS EXECUTION ---
if generate_btn and uploaded_img is not None:
    with st.spinner("🤖 Multimodal Vision-to-Code Synthesizer generating responsive DOM..."):
        active_key = "" if force_offline else api_key_input.strip()
        generator = UIVisionGenerator(provider=selected_provider, api_key=active_key, model_name=selected_model)
        
        raw_code, gen_meta = generator.generate_ui_from_sketch(
            st.session_state.processed_image,
            style_preset=selected_style,
            user_notes=sample_notes
        )
        
        # Clean and sanitize HTML DOM
        sanitized_html, san_meta = CodeSanitizer.clean_and_sanitize(raw_code)
        
        # Calculate quantitative benchmark metrics
        latency = gen_meta.get("latency_sec", 0.0)
        metrics = UIBenchmarkMetrics.evaluate_synthesized_html(sanitized_html, latency_sec=latency)
        
        st.session_state.current_html = sanitized_html
        st.session_state.generation_metadata = gen_meta
        st.session_state.eval_metrics = metrics
        
        if gen_meta.get("is_live_vlm", False):
            st.success(f"✨ Pixel-Accurate UI Synthesized in {gen_meta.get('latency_sec', 0.0)}s via {gen_meta.get('engine')}!")
        elif gen_meta.get("error"):
            st.error(f"❌ {selected_provider} Call Failed: {gen_meta.get('error')}")
            st.warning("⚠️ The app displayed the local fallback layout because the API call failed with the error above. Please check your API key, network, or click '🔍 Test Key' in the sidebar.")
        else:
            st.warning(f"⚠️ Running in Offline Fallback Mode: Generated generic template because no {selected_provider} API Key was entered in the sidebar.")

# --- RIGHT COLUMN: GENERATIVE CODE & WORKBENCH ---
with col_right:
    st.subheader("2. Synthesized Code & Interactive Workbench")

    tab_preview, tab_code, tab_refine, tab_metrics = st.tabs([
        "🌐 Live Interactive Preview",
        "💻 Generated Code",
        "✏️ Conversational Refine",
        "📊 Jury Benchmarks"
    ])

    # TAB 1: LIVE INTERACTIVE PREVIEW
    with tab_preview:
        if st.session_state.current_html:
            st.caption("⚡ Rendered directly in your browser with full Tailwind CSS & FontAwesome interactivity:")
            components.html(st.session_state.current_html, height=620, scrolling=True)
        else:
            st.markdown("""
            <div style="border: 2px dashed #CBD5E1; border-radius: 12px; padding: 60px 20px; text-align: center; color: #94A3B8;">
                <i class="fa-solid fa-code" style="font-size: 2.5rem; margin-bottom: 12px;"></i>
                <p style="font-size: 1.1rem; font-weight: 500;">No UI synthesized yet</p>
                <p style="font-size: 0.85rem;">Click the <b>'🚀 Synthesize Live UI'</b> button in the sidebar to generate responsive HTML/Tailwind components from the sketch.</p>
            </div>
            """, unsafe_allow_html=True)

    # TAB 2: CODE VIEW & EXPORT
    with tab_code:
        if st.session_state.current_html:
            col_actions_1, col_actions_2 = st.columns([1, 1])
            with col_actions_1:
                st.download_button(
                    label="📥 Download standalone index.html",
                    data=st.session_state.current_html,
                    file_name="synthesized_wireframe.html",
                    mime="text/html",
                    use_container_width=True
                )
            with col_actions_2:
                st.button("📋 Ready to Deploy", use_container_width=True)

            st.code(st.session_state.current_html, language="html")
        else:
            st.info("Synthesize a wireframe to inspect and export the generated HTML5 & Tailwind CSS code.")

    # TAB 3: CONVERSATIONAL REFINEMENT
    with tab_refine:
        if st.session_state.current_html:
            st.markdown("**Iterative Prompt Refinement:** Modify the generated UI using natural language.")
            refine_instruction = st.text_input(
                "Describe your desired changes",
                placeholder="e.g. Change primary color to emerald green and add a search box in the navbar",
                key="refine_input"
            )
            if st.button("Apply AI Refinement", type="secondary"):
                if refine_instruction.strip():
                    with st.spinner("Applying requested architectural modifications..."):
                        generator = UIVisionGenerator(provider=selected_provider, api_key=api_key_input, model_name=selected_model)
                        updated_raw, ref_meta = generator.refine_ui_code(
                            st.session_state.current_html,
                            refine_instruction
                        )
                        sanitized_updated, _ = CodeSanitizer.clean_and_sanitize(updated_raw)
                        st.session_state.current_html = sanitized_updated
                        st.session_state.eval_metrics = UIBenchmarkMetrics.evaluate_synthesized_html(
                            sanitized_updated,
                            latency_sec=ref_meta.get("latency_sec", 0.0)
                        )
                        st.rerun()
        else:
            st.info("Synthesize a wireframe first before applying conversational refinements.")

    # TAB 4: JURY BENCHMARK METRICS
    with tab_metrics:
        st.markdown("**Quantitative Academic & System Benchmarks for Final Jury:**")
        if st.session_state.eval_metrics:
            m = st.session_state.eval_metrics
            
            # Row 1 of metrics
            r1_1, r1_2, r1_3, r1_4 = st.columns(4)
            with r1_1:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['syntax_validity_score']}</div><div class='metric-label'>Syntax Validity</div></div>", unsafe_allow_html=True)
            with r1_2:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['responsiveness_score']}</div><div class='metric-label'>Responsiveness</div></div>", unsafe_allow_html=True)
            with r1_3:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['latency_seconds']}</div><div class='metric-label'>Inference Latency</div></div>", unsafe_allow_html=True)
            with r1_4:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['dom_elements_count']}</div><div class='metric-label'>DOM Elements</div></div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Row 2 of metrics
            r2_1, r2_2, r2_3, r2_4 = st.columns(4)
            with r2_1:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['buttons_detected']}</div><div class='metric-label'>Buttons Mapped</div></div>", unsafe_allow_html=True)
            with r2_2:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['inputs_detected']}</div><div class='metric-label'>Form Inputs</div></div>", unsafe_allow_html=True)
            with r2_3:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['lines_of_code']}</div><div class='metric-label'>Lines of Code</div></div>", unsafe_allow_html=True)
            with r2_4:
                st.markdown(f"<div class='metric-card'><div class='metric-value'>{m['approx_tokens_generated']}</div><div class='metric-label'>Tokens Generated</div></div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

        # Baseline Comparison Table
        if os.path.exists("evaluation/benchmark_results.csv"):
            st.markdown("##### 📈 Automated Cross-Sample Benchmark Telemetry")
            bench_df = pd.read_csv("evaluation/benchmark_results.csv")
            st.dataframe(bench_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #94A3B8; font-size: 0.85rem;'>
    <b>Capstone Major Project:</b> Wireframe Sketch-to-Live UI Generator (Sketch2Code) | 
    <b>Core Technologies:</b> Multimodal Generative Vision, Tailwind CSS, DOM AST Sanitization, Streamlit | 
    <b>Defense Status:</b> Production Ready
</div>
""", unsafe_allow_html=True)
