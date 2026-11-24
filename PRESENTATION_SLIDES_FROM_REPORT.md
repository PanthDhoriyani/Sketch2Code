# 📊 Sketch2Code: Capstone Project Report Defense Presentation
### Slide Deck Outline & Comprehensive Speaker Scripts
**Derived Directly From:** [`CAPSTONE_PROJECT_REPORT_SKETCH2CODE.docx`](CAPSTONE_PROJECT_REPORT_SKETCH2CODE.docx)  
**PowerPoint File:** [`SKETCH2CODE_CAPSTONE_REPORT_PRESENTATION.pptx`](SKETCH2CODE_CAPSTONE_REPORT_PRESENTATION.pptx)  
**Format:** 16:9 Widescreen | 15 Slides with Native Tables, Metric Badges & Speaker Notes

---

## 📑 Slide Outline & Report Chapter Mapping

| Slide # | Slide Title | Corresponding Report Chapter | Key Focus & Visuals |
| :---: | :--- | :--- | :--- |
| **1** | **Title Slide: Sketch2Code** | Title Page & Metadata | Academic metadata, candidate info, repository link |
| **2** | **Executive Abstract & Scope** | Executive Abstract | Problem bottleneck, 4-tier pipeline, keywords |
| **3** | **The Frontend Prototyping Bottleneck** | Chapter 1.1 - 1.3 | 4 failure modes of manual UI coding, formal math formulation |
| **4** | **Project Objectives & Scope Boundaries** | Chapter 1.4 | 5 primary engineering objectives & system scope |
| **5** | **Evolution of Generative Sequence Models** | Chapter 2.1 | Markov assumption $O(\|V\|^n)$ vs LSTM $O(d \cdot h + h^2)$ vs Transformers |
| **6** | **Multimodal VLMs & Analysis of Prior Art** | Chapter 2.2 - 2.3 | ViT 16x16 patch projection, cross-attention, critique of Pix2Code |
| **7** | **End-to-End System Architecture** | Chapter 3.1 | 4 decoupled architectural tiers (CV -> VLM -> AST -> Studio) |
| **8** | **CV Preprocessing & Spatial Grounding** | Chapter 3.2 - 3.3 | 1024px aspect preserve, median filter, 1.8x contrast, spatial rules |
| **9** | **AST Compiler Guardrail & Refinement** | Chapter 3.4 - 3.5 | BeautifulSoup DOM repair, CDN injection, delta conversational loop |
| **10** | **Multi-Provider Failover Architecture** | Chapter 4.1 | Groq LPU (sub-second), Gemini, OpenRouter, Local Offline fallback |
| **11** | **Experimental Benchmark Methodology** | Chapter 5.1 - 5.2 | 4 canonical UI scenarios & quantitative metrics testbed |
| **12** | **Empirical Benchmark Telemetry & Results** | Chapter 5.3 (Table 5.1) | 100% syntax validity, 100% responsiveness, latency, DOM tags |
| **13** | **Engineering Challenges & Mitigations** | Chapter 6 | Handwriting ambiguities, 503 failover, 45% token saving via Tailwind |
| **14** | **Contributions, Roadmap & References** | Chapter 7 | Core contributions, React/Vue roadmap, Figma plugins, bibliography |
| **15** | **Conclusion & Transition to Live Demo** | Chapter 7 / Live Demo | Summary takeaways, transition to code review & localhost:8501 demo |

---

## 🎤 Detailed Slide Transcripts & Speaker Scripts

### Slide 1: Cover & Academic Defense Title
- **Badge:** FINAL YEAR B.TECH CAPSTONE PROJECT REPORT DEFENSE
- **Title:** SKETCH2CODE: MULTIMODAL GENERATIVE AI FOR AUTOMATED WIREFRAME-TO-RESPONSIVE CODE SYNTHESIS
- **Subtitle:** An End-to-End System Coupling Computer Vision Preprocessing, Spatial-Grounded Vision Transformers, Deterministic AST DOM Sanitization, and Conversational Refinement.
- **Candidate:** Panth Dhoriyani | Department of Computer Science & Engineering
- **Academic Year:** 2026 | **GitHub:** `https://github.com/PanthDhoriyani/Sketch2Code`
> **Speaker Script:**  
> *"Respected jury members, good morning. Today I present my Final Year Capstone Project: Sketch2Code—a Multimodal Generative AI system designed for automated wireframe-to-responsive code synthesis. This presentation directly reflects our formal academic report. It covers our theoretical progression from baseline statistical models to deep multimodal transformers, our 4-tier engineering architecture, quantitative benchmark telemetry across canonical wireframes, and our interactive live studio."*

---

### Slide 2: Executive Abstract & Research Scope
- **Left Card (Formal Abstract):**
  - **The Latency Bottleneck:** Frontend engineers spend 30% to 50% of sprint cycles manually transcribing whiteboard sketches and mockups.
  - **Proposed Architecture:** 4 integrated tiers: adaptive CV preprocessing, spatial VLM generation, AST DOM sanitization, and interactive studio.
  - **Eliminating Failure Modes:** Naive LLMs produce broken HTML tags and miss CSS sheets; our AST compiler guardrail enforces 100% W3C HTML5 compliance.
  - **Empirical Outcomes:** 100% syntax validity, sub-3.5s latency, and full mobile responsiveness across 4 canonical UI paradigms.
- **Right Top Card (System Capabilities):** Input: Raw hand-drawn sketch | Output: W3C valid HTML5 + Tailwind CSS 3.4+ | Latency: Sub-3.5s (sub-1s on Groq).
- **Right Bottom Card (Keywords):** Multimodal Generative AI, Vision-to-Code Synthesis, AST DOM Sanitization, Tailwind CSS, Spatial Grounding.
> **Speaker Script:**  
> *"Here is the executive abstract from our report. In agile software development, translating design mockups into frontend code is a massive latency bottleneck. While naive LLMs produce broken HTML tags and miss CSS sheets, Sketch2Code combines computer vision preprocessing, spatial-grounded vision models, and an AST DOM compiler guardrail. Across four standard UI scenarios, the system delivers guaranteed 100% W3C validity with sub-3.5 second latency."*

---

### Slide 3: Chapter 1 — The Frontend Prototyping Bottleneck
- **Left Card (4 Failure Modes):**
  1. *Visual-Spatial Discrepancies:* Developers misinterpret designer spatial intent and proportions, causing costly redesign cycles.
  2. *Boilerplate Proliferation:* Writing repetitive flex containers and input wrappers wastes up to 20 hours per sprint.
  3. *Responsiveness Omissions:* Hand-crafted mockups omit mobile breakpoints during initial design, forcing retrofitted media queries.
  4. *Semantic Inconsistencies:* Fast manual coding frequently skips semantic HTML5 landmarks (`<header>`, `<main>`, `<nav>`), hurting a11y and SEO.
- **Right Top Card (Formal Problem Formulation):**
  - Given an unconstrained 2D raster image $I \in \mathbb{R}^{H \times W \times 3}$ containing variable stroke intensities, paper shadows, and handwritten text.
  - Learn a generative mapping $f: I \to C$ where $C$ is an ordered sequence of semantic HTML5 DOM nodes and Tailwind utility tokens.
  - Subject to syntactic validity $V(C) = 1$, layout fidelity $S(C, I) > 0.85$, and inference latency $T(f) < 5.0$ seconds.
- **Right Bottom Card (Quantified Industry Impact):**
  - 20 Hours / Sprint dedicated purely to static layout boilerplate.
  - 30% to 50% of sprint cycle consumed during handoff.
  - Goal: Compress this multi-hour transcription down to 3.5 seconds.
> **Speaker Script:**  
> *"Chapter 1 of our report details the frontend prototyping bottleneck. Frontend engineers routinely spend 20 hours per sprint writing repetitive layout boilerplate. The manual process creates spatial discrepancies, omission of responsive breakpoints, and semantic accessibility issues. We mathematically formulate this as an image-to-code mapping function that must produce syntactically valid HTML with layout fidelity under strict 5-second latency constraints."*

---

### Slide 4: Chapter 1 — Project Objectives & Scope Boundaries
- **Column 1 (Objectives 1 & 2):**
  - *1. Robust Visual Perception:* Automated image enhancement pipeline normalizing camera photos, desk shadows, and faint pencil strokes.
  - *2. Spatial-Grounded Synthesis:* Few-shot prompt architectures enforcing 1-to-1 spatial coordinate mapping, verbatim handwritten OCR transcription, and modern Tailwind styling.
- **Column 2 (Objectives 3 & 4):**
  - *3. Deterministic DOM Guardrail:* Abstract Syntax Tree (AST) compiler guardrail using BeautifulSoup to mathematically guarantee 100% W3C HTML5 compliance.
  - *4. Conversational Refinement:* Iterative conversational workbench allowing developers to modify code via natural language instructions.
- **Column 3 (Objective 5 & Scope):**
  - *5. Empirical Benchmarking:* Automated evaluation suite measuring syntax validity, responsiveness, latency, and DOM element density.
  - *In Scope:* HTML5, Tailwind CSS 3.4+, FontAwesome 6, responsive grids, cross-provider cloud VLM, and local offline fallback.
  - *Out of Scope:* Backend database connections, server routing, and state stores.
> **Speaker Script:**  
> *"To systematically address the problem, our project established five clear engineering objectives: robust visual perception via OpenCV, spatial-grounded code generation, deterministic AST DOM sanitization, conversational refinement, and quantitative benchmarking. We deliberately scope our output to responsive HTML5 and Tailwind CSS with modern CDNs to ensure clean, deployable code."*

---

### Slide 5: Chapter 2 — Theoretical Foundation: From Markov to Transformers
- **Card 1 (Discrete Markov Chains):**
  - *Statistical Foundation:* Operates under Markov assumption: $P(c_t \mid c_1 \dots c_{t-1}) \approx P(c_t \mid c_{t-n+1} \dots c_{t-1})$.
  - *Parameter Estimation:* MLE frequency counts in training corpus.
  - *Fatal Bottleneck:* Curse of Dimensionality: parameter space scales exponentially as $O(|V|^n)$.
  - *Outcome:* For $n \ge 5$, discrete tables suffer severe data sparsity, forcing Laplace smoothing backoff or rigid verbatim memorization.
- **Card 2 (Recurrent Neural Networks & LSTMs):**
  - *Continuous Latent Space:* Projects discrete vocabulary tokens into dense continuous vectors.
  - *Hidden State Memory:* Regulated by input, forget, and output gates; fixed parameter footprint $O(d \cdot h + h^2)$.
  - *Limitation:* Vanishing gradients over extended sequences prevent multi-column UI spatial synthesis.
- **Card 3 (Multimodal Transformers):**
  - *Attention Mechanism:* $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$ captures global spatial relationships.
  - *Patch Tokenization:* Vision Transformer (ViT) partitions image into $16 \times 16$ non-overlapping visual patches.
  - *Cross-Attention Alignment:* Projects visual patches directly into text decoder token space, enabling joint visual-spatial and code reasoning.
> **Speaker Script:**  
> *"Chapter 2 presents the mathematical foundation of sequence modeling. In our baseline project, we studied discrete Markov chains, which operate under the Markov assumption. However, discrete frequency tables suffer from the curse of dimensionality—scaling as O(|V|^n)—causing data sparsity. Recurrent networks and LSTMs introduced continuous dense vectors, but struggle with vanishing gradients across spatial 2D layouts. The modern Multimodal Transformer resolves this by treating image patches and code tokens as a unified sequence under self-attention."*

---

### Slide 6: Chapter 2 — Multimodal VLMs & Critique of Prior Art
- **Left Card (Prior Art Critique):**
  - *Classical OpenCV Contours:* Relied on edge detectors and bounding boxes. Fails completely on messy handwritten sketches and textured paper.
  - *Pix2Code (Beltramelli, 2018):* CNN-LSTM dual branch model. Restricted to synthetic mockups and produced non-responsive custom DSL tokens.
  - *Commercial Naive LLM Prompting:* Raw LLM calls produce syntax hallucinations, unclosed tags, missing CDNs, and layout distortions.
  - *The Sketch2Code Advantage:* Couples CV preprocessing with spatial grounding prompts and deterministic AST DOM repair.
- **Right Card (Multimodal VLM Architecture):**
  - *Visual Patch Projection:* Sketch is partitioned into $16 \times 16$ pixel patches and linearly projected.
  - *Spatial Coordinate Grounding:* Positional encodings preserve relative 2D coordinate positions.
  - *Cross-Modal Attention:* Decoder computes attention weights between visual bounding elements and HTML tags.
  - *Zero-Shot Spatial Mapping:* Directly deduces flex-row or 3-column grid layouts from drawn geometric proximity.
> **Speaker Script:**  
> *"Critiquing prior art: Classical OpenCV contour detectors require hand-tuned thresholds and fail on handwriting. Beltramelli's Pix2Code was limited to synthetic mockups and custom domain-specific languages. Unassisted LLM prompting frequently hallucinates invalid code. Sketch2Code leverages modern Vision Transformers with patch projection and cross-attention, backed by an AST compiler guardrail to eliminate probabilistic errors."*

---

### Slide 7: Chapter 3 — End-to-End System Architecture (The 4-Tier Pipeline)
- **Tier 1 (CV Preprocessor):** `src/sketch_preprocessor.py` | 1024px aspect preserve, 3x3 median denoising, 1.8x contrast scaling, 2.0x Laplacian edge sharpening, adaptive binarization ($T=180$).
- **Tier 2 (Generative Engine):** `src/ui_vision_generator.py` | Groq LPU (Qwen 3.8 / LLaMA), Gemini 3.8 Flash, spatial grounding prompts, exact OCR transcription, Tailwind CSS styling.
- **Tier 3 (AST Sanitizer):** `src/code_sanitizer.py` | Regex boundary extraction, BeautifulSoup DOM tree repair, tag auto-closure, Tailwind 3.4 & FontAwesome 6 CDN injection, 100% W3C guarantee.
- **Tier 4 (Studio Workbench):** `app.py` | Streamlit interactive studio, sandboxed live browser preview, code editor, conversational delta refinement, real-time jury benchmark telemetry.
> **Speaker Script:**  
> *"Chapter 3 introduces our 4-tier system architecture. Tier 1 is our Computer Vision preprocessor that normalizes shadows and sharpens pencil strokes. Tier 2 is our Multimodal Generative Engine running high-speed vision models with spatial prompts. Tier 3 is our AST DOM Sanitizer that guarantees W3C compliance and injects CDNs. Tier 4 is our Streamlit Interactive Studio with live side-by-side rendering, code download, and conversational refinement."*

---

### Slide 8: Chapter 3 — CV Preprocessing & Spatial Grounding (Tiers 1 & 2)
- **Left Card (Tier 1 Details):**
  - *Aspect-Preserving Scaling:* Resizes high-res phone photos to max 1024px while strictly maintaining aspect ratio, preventing column distortion.
  - *3x3 Median Denoising:* Suppresses paper texture and camera sensor noise without eroding thin pencil lines.
  - *Adaptive Contrast Scaling:* 1.8x non-linear contrast scaling and 1.05x brightness leveling, cleanly separating graphite from off-white paper.
  - *Laplacian Boundary Sharpening:* 2.0x Laplacian kernel accentuates button borders, input outlines, and dividers.
  - *Binary Edge Mask Telemetry:* Inverted binary mask using adaptive luminance thresholding ($T=180$) for structural inspection.
- **Right Card (Tier 2 Spatial Rules):**
  - *Visual Container Mapping:* Boxes marked with diagonal crosses ('X') or mountain/sun icons map to styled `<img>` containers with Unsplash placeholders.
  - *Form Control Recognition:* Rectangles with interior text labels instantiate as accessible `<input>` or `<textarea>` tags with matching `<label>` elements.
  - *Action Trigger Mapping:* Pill-shaped or rounded rectangles with imperative verbs ('Submit', 'Sign Up') map to interactive `<button>` tags with hover transitions.
  - *Responsive Grid Deduction:* Horizontal groupings of 3+ cards trigger responsive Tailwind grid classes: `grid grid-cols-1 md:grid-cols-3 gap-6`.
  - *Exact Handwritten OCR:* Transcribes handwritten text verbatim, preventing hallucinated marketing copy.
> **Speaker Script:**  
> *"Examining Tiers 1 and 2 in detail: Raw sketches photographed in classrooms or offices contain uneven lighting and faint lines. Our OpenCV pipeline normalizes dimensions to 1024px, applies median denoising, and enhances contrast by 1.8x. In Tier 2, our spatial grounding prompts establish strict mapping rules: 'X' marks become image placeholders, labeled boxes become form inputs, and horizontal groupings automatically become responsive Tailwind grids."*

---

### Slide 9: Chapter 3 — AST Compiler Guardrail & Conversational Loop (Tiers 3 & 4)
- **Left Card (Tier 3 AST Guardrail):**
  - *Deterministic Compiler Safety:* Probabilistic VLMs occasionally omit closing tags or emit markdown chatter. Tier 3 acts as a deterministic compiler guardrail.
  - *Regex Markdown Stripping:* Extracts raw code from ````html ... ```` blocks, discarding conversational commentary.
  - *BeautifulSoup DOM Parsing:* Constructs an in-memory Abstract Syntax Tree. Unclosed tags are automatically repaired per HTML5 standards.
  - *Head & CDN Auto-Injection:* Auto-injects Tailwind CSS 3.4+ CDN script, FontAwesome 6 icons, and Inter Google fonts.
  - *Format & Beautify:* Emits clean, 2-space indented production code.
- **Right Card (Tier 4 Conversational Loop):**
  - *The Need for Iterative UX:* Developers need to tweak styling without redrawing wireframes.
  - *Architectural Delta Prompting:* Pairs current synthesized HTML DOM structure with user's natural language revision instruction.
  - *Preserving Spatial Structure:* Instructs model to modify colors, fonts, or component hierarchies while strictly preserving core layout geometry.
  - *Example Prompts:* 'Change primary theme to emerald dark mode', 'Add a search box to the header', 'Change card buttons to outlined style'.
  - *Immediate Feedback:* Synthesizes delta updates in under 2 seconds and re-renders live sandbox instantly.
> **Speaker Script:**  
> *"Tiers 3 and 4 provide enterprise-grade reliability and usability. Tier 3 is our AST DOM compiler guardrail. We pass the generated code through BeautifulSoup's AST parser, which auto-closes any orphaned tags, enforces W3C syntax, and injects modern Tailwind and FontAwesome CDNs. Tier 4 provides conversational refinement: developers can type natural language instructions to switch themes or add widgets, and our delta engine updates the code without touching the original wireframe."*

---

### Slide 10: Chapter 4 — Multi-Provider Failover Architecture
- **Provider Table:**

| Provider Engine | Primary Model | Inference Latency | Academic Defense Role |
| :--- | :---: | :---: | :--- |
| **Groq Cloud (LPU)** | `qwen/qwen3.8-27b` | **< 0.8s (sub-second)** | Primary high-speed free tier engine (zero queue bottleneck) |
| **Google AI Studio** | `gemini-3.8-flash` | 1.5s - 2.5s | Google Multimodal Vision cloud engine alternative |
| **OpenRouter Hub** | `llama-3.2-11b:free` | 1.8s - 3.0s | Open-source vision fallback provider |
| **Local Heuristics** | Rule-Guided Engine | **< 0.05s (instant)** | 100% offline zero-network failover for uninterrupted demo |

- **Bottom Card (Zero-Downtime Defense Rationale):**
  - *Academic Risk:* Public cloud APIs frequently return 503 high-demand errors or rate limits during live jury presentations.
  - *Mitigation:* Abstracted behind a unified interface (`src/ui_vision_generator.py`). Automatic failover to Groq LPU or offline local generator.
  - *Result:* Zero presentation downtime verified across hundreds of generation cycles.
> **Speaker Script:**  
> *"Chapter 4 addresses a crucial engineering consideration: system resilience during high-stakes defense. Cloud APIs often hit 503 traffic spikes or rate limits. To guarantee uninterrupted evaluation, we implemented a multi-provider failover architecture. Our primary engine is Groq LPU running Qwen 3.8 at sub-second speeds. We maintain secondary pipelines for Google Gemini and OpenRouter, and an offline rule-guided fallback synthesizer that requires zero internet connection."*

---

### Slide 11: Chapter 5 — Experimental Benchmark Methodology
- **Left Card (4 Canonical Scenarios):**
  1. *Authentication Screen (`login_wireframe.png`):* Centered auth card, dual inputs (email, password), 'Remember Me' checkbox, primary submit button, social OAuth pills.
  2. *E-Commerce Showcase (`ecommerce_card.png`):* Product card with image placeholder ('X'), discount badge, title, star ratings, price tags, 'Add to Cart' CTA button.
  3. *Analytics Dashboard (`dashboard_wireframe.png`):* Navigation sidebar, stat KPI metric cards (revenue, users), chart container, recent transactions data table.
  4. *SaaS Hero Landing (`saas_landing_wireframe.png`):* Header navbar, hero headline, dual CTA buttons, responsive 3-column feature grid with icons and descriptions.
- **Right Card (Quantitative Evaluation Metrics):**
  - *HTML Syntax Validity Score:* Confirms complete enclosure of `<html>`, `<head>`, `<body>`, and zero orphaned tags via DOM AST parsing. (Target: 100%).
  - *Mobile Viewport Responsiveness:* Quantifies ratio of elements using Tailwind responsive prefixes (`sm:`, `md:`, `lg:`) and fluid layouts. (Target: > 80%).
  - *End-to-End Generation Latency:* Wall-clock time in seconds from input submission to complete browser render.
  - *DOM Extraction Density:* Total HTML tags generated, form inputs recognized, and interactive buttons instantiated.
  - *Automated Runner:* Executed via `run_benchmark_eval.py` outputting to `evaluation/benchmark_results.csv`.
> **Speaker Script:**  
> *"Chapter 5 outlines our empirical evaluation methodology. To rigorously test the system, we constructed an automated benchmark testbed across four canonical UI archetypes: an authentication screen, an e-commerce card, a multi-widget analytics dashboard, and a SaaS landing page. We evaluate each scenario across four quantitative metrics: HTML syntax validity, mobile responsiveness, end-to-end generation latency, and DOM element density."*

---

### Slide 12: Chapter 5 — Empirical Benchmark Telemetry & Results
- **Empirical Table (Report Table 5.1):**

| Benchmark Scenario | Syntax Validity | Responsiveness | Latency | DOM Tags | Lines | Tokens |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Authentication Screen** | **100.0%** | 85% | **1.12 s** | 37 | 80 | 853 |
| **E-Commerce Product Card** | **100.0%** | 90% | **0.98 s** | 31 | 68 | 685 |
| **Analytics Dashboard** | **100.0%** | **100%** | **1.65 s** | 83 | 207 | 1,717 |
| **SaaS Landing Page** | **100.0%** | **100%** | **1.42 s** | 49 | 119 | 1,271 |

- **Metric Badges:**
  - `100.0%` Syntax Validity (Zero broken or unclosed tags via AST guardrail)
  - `< 1.7 s` Average Latency (Sub-second on Groq LPU hardware acceleration)
  - `100%` Complex Responsiveness (Full `md:` & `lg:` grid layout adaptation)
  - `45%` Token Reduction (Tailwind utility classes vs verbose custom CSS)
> **Speaker Script:**  
> *"Here are the empirical benchmark results from Table 5.1 of our report. Every scenario achieved a flawless 100% syntax validity rate thanks to our BeautifulSoup AST compiler. Complex multi-widget layouts like the Analytics Dashboard and SaaS Landing achieved 100% mobile responsiveness. Furthermore, average generation latency remained under 1.7 seconds, comfortably below human interactive limits, while Tailwind utility classes saved 45% in token consumption compared to standard CSS."*

---

### Slide 13: Chapter 6 — Engineering Challenges & Trade-Offs
- **Left Card (Real-World Challenges):**
  1. *Handwriting & Stroke Ambiguities:* Messy pencil handwriting and overlapping lines created OCR confusion in early tests.
  2. *Cloud API Rate Limits & 503 Traffic Spikes:* Free-tier cloud endpoints routinely experience 503 high-demand blocks.
  3. *Token Budget Inflation & Generation Lag:* Emitting verbose CSS stylesheets consumed excessive tokens, causing latency and syntax truncation.
  4. *Hallucinated Phantom UI Elements:* Unconstrained prompting led model to invent arbitrary navigation links.
- **Right Card (Architectural Mitigations):**
  - *Adaptive Contrast Preprocessing:* 1.8x non-linear contrast scaling and Laplacian sharpening cleanly isolates handwriting from paper shadows.
  - *Multi-Provider Failover Matrix:* Implemented Groq LPU inference backed by Gemini, OpenRouter, and local offline heuristic synthesizers.
  - *Tailwind CSS Standardization:* Switching to utility-first Tailwind classes reduced output token count by 45%, cutting latency in half.
  - *Negative Prompt Constraints:* Strict negative rules explicitly penalize model for adding un-drawn UI components.
> **Speaker Script:**  
> *"Chapter 6 discusses the engineering trade-offs and challenges encountered. Handwriting ambiguities were mitigated using adaptive contrast preprocessing. 503 cloud API rate limits were resolved through our multi-provider failover matrix. Verbose CSS token inflation was solved by standardizing on Tailwind CSS, which cut token consumption by 45%. Finally, negative prompt constraints prevented the hallucination of phantom UI elements."*

---

### Slide 14: Chapter 7 — Contributions, Roadmap & Academic References
- **Column 1 (Summary of Contributions):**
  - *1. End-to-End Pipeline:* Integrated CV preprocessing, multimodal VLM reasoning, and compiler guardrails.
  - *2. 100% W3C Validity:* Proved that AST parsing guarantees deterministic syntax safety for probabilistic generative AI.
  - *3. Real-Time Performance:* Sub-1.7s average latency for rapid developer prototyping.
  - *4. Conversational Refinement:* Enables natural language iterative UI styling.
- **Column 2 (Future Engineering Roadmap):**
  - *React & Vue JSX Synthesis:* Extend synthesis to modular React (JSX), Vue.js, and Svelte component trees with reactive state hooks.
  - *IDE & Design Tool Extensions:* Build native plugins for VS Code and Figma allowing whiteboard photos to paste directly into project source trees.
  - *Automated Mock Backends:* Generate mock REST endpoints and JSON fixtures matching recognized form fields.
- **Column 3 (Academic Bibliography):**
  - Beltramelli (2018): *Pix2Code: Generating code from GUI screenshots* (ACM EICS).
  - Vaswani et al. (2017): *Attention Is All You Need* (NeurIPS).
  - Dosovitskiy et al. (2020): *ViT: Transformers for Image Recognition at Scale* (ICLR).
  - Radford et al. (2021): *CLIP: Learning Transferable Visual Models* (ICML).
  - Tailwind Labs (2024): *Tailwind CSS Utility-First Documentation*.
  - W3C (2023): *HTML5 & DOM Living Standard*.
> **Speaker Script:**  
> *"In Chapter 7, we summarize our contributions: a complete multimodal vision-to-code pipeline with 100% W3C validity and conversational refinement. For future work, our architecture can be naturally extended to generate modular React JSX components, Figma plugins, and automated mock REST backends. Our bibliography anchors this work in seminal papers including Pix2Code, Transformers, and ViT."*

---

### Slide 15: Conclusion & Transition to Live Demonstration
- **Header:** CONCLUSION & TRANSITION TO LIVE SYSTEM DEMONSTRATION
- **Big Callout:** Sketch2Code demonstrates that Multimodal Generative AI can be engineered into a deterministic, production-grade frontend synthesis tool.
- **Three-Part Live Demonstration Plan:**
  1. *Source Code Walkthrough:* `src/` architecture, OpenCV filters, prompt templates, and AST compiler guardrail.
  2. *Live Interactive Studio Demonstration (`http://localhost:8501`):*
     - Synthesis of complex Analytics Dashboard & E-Commerce Card in < 3.5s.
     - Live DOM element inspection & responsiveness toggle.
     - Conversational Prompt Refinement ('Switch to dark mode with emerald accents').
  3. *Viva Defense & Jury Q&A Examination.*
> **Speaker Script:**  
> *"In conclusion, Sketch2Code proves that Generative AI can be transformed from experimental chat demos into a rigorous, deterministic software engineering tool. We will now transition to the live demonstration phase. I will guide you through our Python codebase and compiler guardrails, execute live wireframe synthesis in our Streamlit studio, demonstrate conversational prompt refinement, and invite your questions for our viva examination. Thank you."*
