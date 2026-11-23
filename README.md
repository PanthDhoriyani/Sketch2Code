# 📐 Sketch2Code: Wireframe Sketch-to-Live UI Studio
### Multimodal Generative AI Capstone Project — Final Year B.Tech CSE (2026)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.4+-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Groq LPU](https://img.shields.io/badge/Groq-LPU_Inference-F55036?style=for-the-badge)](https://groq.com)
[![W3C Valid](https://img.shields.io/badge/HTML5-W3C_100%25-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://w3.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 🌟 Project Overview

**Sketch2Code** is an end-to-end Multimodal Generative AI framework that translates raw, hand-drawn wireframe sketches and low-fidelity digital mockups into clean, production-ready, fully responsive **HTML5 + Tailwind CSS** code with instant live browser rendering.

In traditional software development, translating whiteboard sketches into functional frontend code requires 2–8 hours per view. **Sketch2Code** reduces this latency to **under 3.5 seconds** while guaranteeing **100% W3C HTML syntax compliance** via an AST DOM compiler guardrail.

```
+-------------------+      +-----------------------+      +--------------------------+
|  Hand-Drawn /     | ---> |  OpenCV Vision Pre-   | ---> |  Multimodal VLM Engine   |
|  Digital Sketch   |      |  processor (Adaptive) |      |  (Groq / Gemini / Vision)|
+-------------------+      +-----------------------+      +--------------------------+
                                                                       |
+-------------------+      +-----------------------+                   v
|  Live Interactive | <--- |  AST DOM Sanitizer &  | <--- [ Raw Generated HTML/CSS ]
|  Browser Preview  |      |  CDN Injector (BS4)   |
+-------------------+      +-----------------------+
```

---

## 🚀 Key Architectural Innovations

1. **Adaptive Computer Vision Preprocessor (`src/sketch_preprocessor.py`):**
   - Automatically handles low-contrast pencil marks, uneven lighting, shadows, and camera noise.
   - Applies CLAHE (Contrast Limited Adaptive Histogram Equalization), bilateral filtering, and Otsu/adaptive Gaussian binarization.

2. **Multi-Provider Vision Engine (`src/ui_vision_generator.py`):**
   - **Groq LPU (Default / Recommended):** Powered by ultra-fast multimodal vision (`qwen/qwen3.8-27b`), achieving sub-4s synthesis with zero queue bottleneck.
   - **Gemini Vision:** Supports Google `gemini-3.8-flash` & `gemini-2.5-flash`.
   - **OpenRouter & OpenAI:** Direct integration with `gpt-4o` and open vision models.
   - **Offline Deterministic Fallback:** 100% offline heuristic layout synthesizer for zero-downtime jury demonstrations.

3. **AST DOM Sanitizer Guardrail (`src/code_sanitizer.py`):**
   - Uses `BeautifulSoup` AST parsing to detect and close unclosed tags, rectify malformed tables, and enforce structural validity.
   - Automatically injects modern CDNs: Tailwind CSS 3.4+, FontAwesome 6.4+, Inter typography, and Google Fonts.

4. **Interactive Studio & Conversational Refinement (`app.py`):**
   - Side-by-side split-view comparison: Original Sketch vs Preprocessed Edge Map vs Live Interactive Web Sandbox.
   - Conversational UI refinement: Modify themes, adjust component styles, or inject dark mode via natural language prompts.

5. **Quantitative Benchmarking Suite (`src/sketch_metrics.py`, `run_benchmark_eval.py`):**
   - Automatic computation of W3C syntax validity, viewport responsiveness, DOM tree depth, element counts, and inference latency.

---

## 📁 Repository Structure

```
Sketch2Code/
├── app.py                                  # Streamlit Interactive Studio & Jury Demonstration Hub
├── requirements.txt                        # Pinned dependencies
├── .gitignore                              # Git exclusion rules
├── run_benchmark_eval.py                   # Automated cross-sample evaluation runner
├── create_sample_wireframes.py             # Script to generate benchmark wireframe sketches
├── generate_capstone_report.py             # Academic Word thesis report generator (.docx)
├── generate_capstone_presentation.py       # Jury presentation deck generator (.pptx)
│
├── CAPSTONE_PROJECT_REPORT_SKETCH2CODE.docx # 7-Page IEEE/UGC compliant Academic Thesis Report
├── FINAL_JURY_PRESENTATION_SKETCH2CODE.pptx# 12-Slide 16:9 Presentation Deck with Speaker Notes
├── PRESENTATION_SLIDES_CAPSTONE.md         # Full presentation slide text and speaker notes
├── VIVA_CHEAT_SHEET.md                     # Top 15 Viva defense questions & answers
│
├── src/                                    # Core Engineering Modules
│   ├── sketch_preprocessor.py              # OpenCV adaptive filtering & stroke enhancement
│   ├── ui_vision_generator.py              # Multi-provider multimodal engine (Groq, Gemini, etc.)
│   ├── prompt_templates.py                 # Spatial grounding & few-shot UI/UX design rules
│   ├── code_sanitizer.py                   # BeautifulSoup AST DOM repair & CDN injection
│   └── sketch_metrics.py                   # Quantitative metrics (validity, latency, DOM count)
│
├── samples/                                # Curated Benchmark Wireframe Sketches
│   ├── login_wireframe.png                 # Auth screen with social buttons
│   ├── ecommerce_card.png                  # Product card with price, badge & cart CTA
│   ├── dashboard_wireframe.png             # Multi-widget analytics dashboard with stats & tables
│   └── saas_landing_wireframe.png          # SaaS hero banner, features grid & pricing cards
│
└── evaluation/                             # Experimental Evaluation Data
    └── benchmark_results.csv               # Quantitative benchmark output across wireframes
```

---

## ⚡ Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/PanthDhoriyani/Sketch2Code.git
cd Sketch2Code
```

### 2. Set Up Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys (Optional but Recommended)
For cloud VLM synthesis, obtain a free API key:
- **Groq (Fastest, Recommended):** [console.groq.com](https://console.groq.com)
- **Google Gemini:** [aistudio.google.com](https://aistudio.google.com)

*Note: You can paste your API key directly into the Streamlit sidebar during runtime, or set an environment variable:*
```bash
export GROQ_API_KEY="your-groq-api-key"
# or
export GEMINI_API_KEY="your-gemini-api-key"
```
*(If no API key is provided, the application seamlessly activates the **Offline Fallback Synthesizer** for an instant local demo).*

---

## 🖥️ Running the Application

Launch the Streamlit Studio:
```bash
streamlit run app.py
```

Then navigate to `http://localhost:8501` in your browser.

### 5-Step Live Jury Demo Walkthrough:
1. **Select a Sample:** Choose *Analytics Dashboard* or *E-Commerce Card* from the sidebar samples (or upload a custom hand-drawn sketch).
2. **Inspect Preprocessing:** Toggle *"Inspect Binarized Line Edges"* to view stroke sharpening and noise reduction.
3. **Select Engine:** Choose **Groq (Fast)** or **Local Offline Fallback**.
4. **Synthesize:** Click **"🚀 Synthesize Live UI"** (completes in ~3.5 seconds).
5. **Explore Tabs:**
   - **🌐 Live Interactive Preview:** Full browser-rendered, clickable layout.
   - **💻 Generated HTML / CSS:** Inspect syntax-sanitized HTML5 with Tailwind CSS utility classes.
   - **✏️ Conversational Refine:** Type `"Switch to modern dark mode with neon accents"` and see real-time updates.
   - **📊 Jury Benchmarks:** Inspect 100% W3C validity, DOM element count, responsiveness, and latency metrics.

---

## 🔬 Experimental Evaluation & Results

Quantitative benchmarks evaluated across 4 representative UI wireframe archetypes:

| Benchmark Wireframe | Syntax Validity | Mobile Responsive | Inference Latency | DOM Element Count | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Authentication Screen** | **100.0%** | High | **1.18 s** | 37 | Verified |
| **E-Commerce Product Card** | **100.0%** | High | **0.95 s** | 31 | Verified |
| **Analytics Dashboard** | **100.0%** | 100% | **1.82 s** | 83 | Verified |
| **SaaS Landing Page** | **100.0%** | 100% | **1.45 s** | 49 | Verified |

To re-run benchmark evaluations automatically:
```bash
python run_benchmark_eval.py
```

---

## 📚 Jury Defense & Academic Deliverables

- **Academic Thesis Report:** [`CAPSTONE_PROJECT_REPORT_SKETCH2CODE.docx`](CAPSTONE_PROJECT_REPORT_SKETCH2CODE.docx) — Formal 7-page technical thesis covering Abstract, Literature Review, System Architecture, Experimental Results, and Conclusion.
- **Jury Slide Deck:** [`FINAL_JURY_PRESENTATION_SKETCH2CODE.pptx`](FINAL_JURY_PRESENTATION_SKETCH2CODE.pptx) — 12 professional 16:9 widescreen slides with embedded speaker notes.
- **Slide Deck Transcripts:** [`PRESENTATION_SLIDES_CAPSTONE.md`](PRESENTATION_SLIDES_CAPSTONE.md)
- **Viva Defense Q&A Sheet:** [`VIVA_CHEAT_SHEET.md`](VIVA_CHEAT_SHEET.md) — Anticipated examiner questions and theoretical answers.

---

## 👥 Authors & Academic Context

- **Author:** Panth Dhoriyani
- **Degree:** Bachelor of Technology (B.Tech) in Computer Science & Engineering
- **Academic Year:** 2026
- **Project Category:** Generative AI & Multimodal Deep Learning (Final Year Capstone Project)
