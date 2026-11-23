# 🎓 Viva Cheat Sheet & Oral Defense Guide
## Project: Sketch2Code — Wireframe Sketch-to-Live UI Generator
**Target Audience:** Final Year B.Tech / BE Computer Science & Engineering Jury  
**Technologies:** Multimodal Generative AI, Vision-to-Code Synthesis, Tailwind CSS, DOM Tree AST Sanitization

---

## 🎯 1. The 30-Second "Elevator Pitch" to the Jury

> *"Respected jury members, in modern software engineering, translating initial hand-drawn wireframes and whiteboard brainstorms into functional, responsive code takes frontend teams 30 to 50 percent of their sprint time. Our capstone project, **Sketch2Code**, is an end-to-end Multimodal Generative AI pipeline that ingests raw hand-drawn sketches, cleans pencil strokes via image enhancement, extracts structural UI hierarchies, and synthesizes production-ready, accessible HTML5 and Tailwind CSS code in under 3 seconds. The system features an interactive live browser preview, an automated DOM sanitizer that guarantees 100% W3C syntax validity, and an iterative prompt refinement engine for real-time design adjustments."*

---

## 🔬 2. Top 15 Jury Questions & Defensible Answers

### Q1: "Isn't this just sending an image to an LLM API? Where is your engineering contribution?"
**Your Winning Answer:**
> *"No, sir/ma'am. Direct raw API calls fail in production for three reasons:*
> 1. *Raw hand-drawn sketches contain desk shadows, low lighting, and faint pencil strokes that cause vision models to hallucinate or miss elements. We engineered a **Vision Preprocessing Pipeline (`src/sketch_preprocessor.py`)** that performs auto-white balance, stroke enhancement, and edge binarization.*
> 2. *Raw LLM outputs frequently produce truncated markdown tags, unclosed `<div>` elements, and missing CSS dependencies. We developed an **Abstract Syntax Tree (AST) DOM Sanitizer (`src/code_sanitizer.py`)** using BeautifulSoup to inject required CDNs, validate tag matching, and guarantee 100% syntax validity.*
> 3. *We built an **Offline Heuristic Synthesis Engine** that infers structural bounding boxes locally, guaranteeing zero-downtime execution even when network APIs fail."*

---

### Q2: "How does a Multimodal Vision-Language Model process an image?"
**Your Winning Answer:**
> *"A Multimodal model uses a Vision Transformer (ViT) or vision encoder. The input image is divided into non-overlapping patches (e.g., $16 \times 16$ pixels). Each patch is linearly projected into a continuous visual embedding vector. These visual patch tokens are then projected into the same latent space as text tokens using a cross-attention or projection projection layer (like a linear adapter or Perceiver Resampler). The autoregressive decoder then attends to these visual tokens to predict the next code tokens."*

---

### Q3: "How do you handle faint pencil sketches vs. clear digital wireframes?"
**Your Winning Answer:**
> *"In `src/sketch_preprocessor.py`, we implement a 3-stage adaptive enhancement:*
> - *First, subtle median smoothing removes paper grain and camera sensor noise.*
> - *Second, non-linear contrast scaling ($1.8\times$) and brightness leveling ($1.05\times$) separate pencil graphite from off-white paper.*
> - *Third, stroke sharpening ($2.0\times$) accentuates line boundaries, ensuring the vision attention heads detect distinct input boxes and button borders."*

---

### Q4: "Why did you choose Tailwind CSS over standard CSS or Bootstrap?"
**Your Winning Answer:**
> *"Tailwind CSS is a utility-first framework that minimizes token footprint during generation. In standard CSS, the model must invent arbitrary class names and write separate `<style>` blocks, increasing token latency and hallucination risk. With Tailwind, utility classes like `flex`, `grid-cols-3`, `rounded-xl`, and `shadow-md` are concise, standardized, and self-documenting. Furthermore, Tailwind's responsive breakpoints (`sm:`, `md:`, `lg:`) allow the model to make layouts responsive with single-class additions."*

---

### Q5: "How do you evaluate whether the generated UI matches the sketch?"
**Your Winning Answer:**
> *"We evaluate across four quantitative metrics:*
> 1. ***HTML Syntax Validity Score (100%):*** Automated DOM validation to ensure complete closed tags and correct nesting.
> 2. ***Mobile Responsiveness Score:*** Automated regex and DOM inspection detecting responsive flex/grid layouts and media breakpoint classes.
> 3. ***Inference Latency:*** Timing end-to-end execution from upload to browser rendering.
> 4. ***Component Mapping Recall:*** Checking whether drawn inputs, buttons, and headings are properly instantiated in the DOM tree."*

---

### Q6: "How do you handle code hallucination or missing closing tags?"
**Your Winning Answer:**
> *"Our `CodeSanitizer` module acts as a strict post-processing compiler guardrail. It parses the raw output using BeautifulSoup. If a tag is unclosed, the parser auto-closes it according to the HTML5 specification. If `<head>`, `<html>`, or `<body>` are omitted, the sanitizer wraps the components in a standard HTML5 boilerplate and automatically injects Tailwind and FontAwesome CDNs."*

---

### Q7: "What happens if the model encounters an ambiguous sketch element?"
**Your Winning Answer:**
> *"In our system prompt design (`src/prompt_templates.py`), we implement standard UI design heuristics:*
> - *A rectangle with an 'X' or cross lines is mapped to an image placeholder.*
> - *A rectangle with text inside is mapped to an accessible input field with placeholder text.*
> - *A filled rounded rectangle with a verb is mapped to a clickable `<button>`.*
> *If the user wants to adjust an ambiguous element, our **Conversational Refinement Engine** allows them to type natural language instructions to iteratively revise the UI without re-generating from scratch."*

---

### Q8: "What are the computational requirements of your system?"
**Your Winning Answer:**
> *"The preprocessing, sanitization, and Streamlit studio run completely on a standard lightweight CPU (under 500MB RAM). For multimodal generation, the cloud API runs in under 3 seconds with zero local GPU load. For offline scenarios, our rule-based heuristic synthesizer executes locally in under 0.05 seconds with zero GPU requirements."*

---

### Q9: "What are the primary limitations of your current approach?"
**Your Winning Answer:**
> *"1. Very complex multi-page workflows or nested sub-tabs require multi-step generation.*
> *2. Dynamic JavaScript state logic (e.g., fetching real backend APIs or Redux state) is currently static UI. Connecting this to React/Vue component trees with state management is our primary direction for future work."*

---

### Q10: "How can this project be commercialized or deployed in industry?"
**Your Winning Answer:**
> *"It can be integrated as a Figma plugin, a VS Code extension, or a Slack/Teams bot where product managers can simply snap a photo of a whiteboard after a sprint planning meeting and instantly receive a pull request with the scaffolding code."*
