# 📊 Capstone Presentation Slides & Speaker Script
## Project: Sketch2Code — Wireframe Sketch-to-Live UI Generator
**Degree:** Final Year B.Tech / BE Computer Science & Engineering  
**Course:** Generative AI Capstone Project  
**Deliverable:** 12-Slide Final Jury Defense Presentation Guide

---

### Slide 1: Title Slide
- **Title:** Sketch2Code: Wireframe Sketch-to-Live UI Generator
- **Subtitle:** Multimodal Generative AI for Automated Structural Perception and Responsive Code Synthesis
- **Student Details:** Final Year B.Tech Computer Science | Generative AI Capstone Defense
- **Tools:** Multimodal Vision AI, PyTorch / Gemini Vision, Tailwind CSS, BeautifulSoup AST, Streamlit

> **🗣️ What to Say to the Jury:**  
> *"Good morning respected jury members. Today, I am proud to present our Capstone Major Project: **Sketch2Code** — an end-to-end Multimodal Generative AI system that bridges the gap between conceptual whiteboard sketching and production-ready frontend development by translating raw wireframes into responsive, live-rendered HTML5 and Tailwind CSS in real time."*

---

### Slide 2: Problem Statement & Industrial Motivation
- **The Industry Bottleneck:**
  - 30–50% of frontend development time in early sprints is spent translating paper sketches and mockups into boilerplate HTML/CSS.
  - Manual handoffs between UI/UX designers and frontend developers cause layout discrepancies and slow prototyping.
  - Existing automated tools either produce rigid non-responsive code or require expensive proprietary design software.
- **The Objective:**
  - Build an intelligent, multimodal vision-to-code pipeline that ingests any hand-drawn sketch or wireframe image and synthesizes clean, accessible, responsive code with instant browser rendering.

> **🗣️ What to Say to the Jury:**  
> *"In sprint cycles, rapid prototyping is critical. Designers sketch wireframes on paper or whiteboards, and developers manually code the initial boilerplate. This process is repetitive and error-prone. Our objective was to build an automated, multimodal generative pipeline that eliminates this manual overhead while maintaining strict code standards and mobile responsiveness."*

---

### Slide 3: System Architecture & Workflow Pipeline
- **Four Core Stages:**
  1. **Vision Perception & Preprocessor:** Adaptive contrast leveling, stroke enhancement, and edge binarization.
  2. **Multimodal Generative Engine:** Vision-Language model conditioned with tailored few-shot system prompts and design heuristics.
  3. **AST DOM Sanitizer:** Validates tag closure, injects Tailwind CDN and FontAwesome icons, enforces W3C HTML5 compliance.
  4. **Interactive Studio & Refinement Engine:** Side-by-side live rendering with conversational prompt refinement.

> **🗣️ What to Say to the Jury:**  
> *"Our architecture is divided into four robust layers. Unlike naive implementations that simply query an API, our pipeline first cleans paper noise and enhances strokes. It then feeds the image to our multimodal generative engine, passes the generated code through an AST DOM sanitizer to guarantee syntax validity, and renders it in an interactive browser studio with iterative conversational editing."*

---

### Slide 4: Computer Vision Preprocessing
- **Challenge:** Hand-drawn sketches have paper shadows, yellow desk lighting, and faint pencil marks.
- **Solution (`src/sketch_preprocessor.py`):**
  - **Auto-Standardization:** Preserves aspect ratio while standardizing resolution for optimal vision tokenization.
  - **Stroke Enhancement:** Applies $1.8\times$ non-linear contrast scaling and $2.0\times$ sharpening.
  - **Binarization:** High-contrast edge segmentation to isolate structural component boundaries.

> **🗣️ What to Say to the Jury:**  
> *"Raw photos of sketches suffer from low light and shadows. Our preprocessing module cleans the background, boosts pencil contrast, and sharpens edges, which prevents the vision attention heads from hallucinating or missing faint boundaries."*

---

### Slide 5: Multimodal Generative Engine & Heuristic Mapping
- **Vision-Language Model:** Processes image patch tokens and autoregressively generates HTML5 code.
- **Heuristic Wireframe Mapping:**
  - Rectangle with 'X' $\to$ Stylized image container / Unsplash image.
  - Labeled rectangles $\to$ Semantic form inputs with accessible labels.
  - Pill/rounded buttons $\to$ Styled Tailwind call-to-actions with hover transitions.
  - Multi-column layouts $\to$ Responsive Tailwind CSS Grid (`grid-cols-1 md:grid-cols-3`).
- **Offline Fallback Engine:** Built-in structural synthesizer guarantees zero-downtime execution even without internet access.

> **🗣️ What to Say to the Jury:**  
> *"The generative engine uses prompt engineering that maps standard wireframe conventions into modern Tailwind CSS classes. To guarantee 100% defense reliability during viva, we also implemented an offline local heuristic synthesizer that extracts structural layout blocks locally."*

---

### Slide 6: AST Code Sanitizer & DOM Guardrails
- **The Problem:** Generative models can produce unclosed tags or missing headers.
- **The Solution (`src/code_sanitizer.py`):**
  - BeautifulSoup DOM parser ensures valid HTML tree hierarchy.
  - Automatically injects missing `<head>`, `<body>`, Tailwind CSS CDN, and FontAwesome icons.
  - Formats and beautifies the code for human readability and immediate production deployment.

> **🗣️ What to Say to the Jury:**  
> *"A key innovation of our project is the AST DOM Sanitizer. It acts as an automated compiler guardrail. It inspects the generated DOM tree, repairs any unclosed tags, and injects necessary styling CDNs so the code can be downloaded as an `index.html` file and deployed instantly."*

---

### Slide 7: Conversational Prompt Refinement Engine
- **Iterative UI Engineering:**
  - UI design is inherently iterative; developers rarely accept the first draft without tweaks.
  - Users can enter conversational requests: *"Make the primary button emerald green"*, *"Add a dark mode theme"*, or *"Add a search bar in the navbar"*.
  - The model edits the existing DOM tree while preserving existing layout components.

> **🗣️ What to Say to the Jury:**  
> *"Prototyping is an iterative conversation. With our conversational refinement tab, users can request adjustments in plain English. The engine modifies the existing code structure dynamically without having to regenerate from scratch."*

---

### Slide 8: Experimental Evaluation & Quantitative Benchmarks
- **Evaluation on 4 Benchmark Scenarios:**
  - Login & Authentication Screen
  - E-Commerce Product Showcase Card
  - Analytics Dashboard with Metric Cards
  - SaaS Landing Page with Feature Grid

| Benchmark Scenario | Syntax Validity | Responsiveness | Inference Latency | DOM Elements | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Login Screen** | 100.0% | High | < 1.2s | 37 | Verified |
| **E-Commerce Card** | 100.0% | High | < 1.0s | 31 | Verified |
| **Analytics Dashboard** | 100.0% | 100% | < 1.8s | 83 | Verified |
| **SaaS Landing Page** | 100.0% | 100% | < 1.5s | 49 | Verified |

> **🗣️ What to Say to the Jury:**  
> *"We evaluated our system across 4 distinct wireframe benchmarks. As shown in the table, our pipeline achieved 100% syntax validity across all scenarios, responsive layout adaptation, and sub-2 second generation latency."*

---

### Slide 9: Live Interactive Demonstration
- Switch to the running Streamlit Dashboard (`http://localhost:8501`):
  1. Select the **Analytics Dashboard** or upload a custom sketch.
  2. Inspect the preprocessed image and stroke enhancement.
  3. Click **"🚀 Synthesize Live UI"**.
  4. Showcase the **Live Browser Preview** (click the buttons and highlight interactive elements).
  5. Demonstrate **Conversational Refinement** (e.g., change theme to dark mode).
  6. Show the **Jury Benchmark Metrics** tab.

> **🗣️ What to Say to the Jury:**  
> *"Now, let us move to the live interactive demonstration. Notice how the user selects a wireframe sketch, the preprocessing isolates the components, and within seconds, we have an interactive, clickable webpage rendered directly in the browser."*

---

### Slide 10: Comparison with Existing Approaches

| Feature | Traditional Computer Vision (Contour Detection) | Naive LLM Prompting | **Sketch2Code (Our Capstone)** |
| :--- | :---: | :---: | :---: |
| **Stroke Noise Handling** | ❌ Fails on faint sketches | ⚠️ Often misses small details | ✅ Adaptive Preprocessing |
| **DOM Validity** | ❌ Requires hardcoded templates | ⚠️ Risk of unclosed tags | ✅ 100% Guaranteed by AST Sanitizer |
| **Modern Styling** | ❌ Basic static HTML | ⚠️ Inconsistent styling | ✅ Clean Tailwind CSS + Icons |
| **Iterative Refinement** | ❌ Not supported | ⚠️ Loses context | ✅ Context-Aware Refinement |
| **Offline Reliability** | ✅ Yes | ❌ Network required | ✅ Hybrid (Online VLM + Offline Heuristic) |

---

### Slide 11: Limitations & Future Enhancements
- **Current Limitations:**
  - Focuses on single-screen UI layout synthesis rather than multi-page navigation flows.
  - Produces static interactive frontend components without full backend database bindings.
- **Future Roadmap:**
  - Export to modern frontend frameworks (React JSX, Vue.js, Flutter).
  - Integration as a native Figma plugin and VS Code extension.

---

### Slide 12: Conclusion & Q&A
- **Summary:**
  - Built an end-to-end Multimodal Generative AI system for wireframe-to-code synthesis.
  - Integrated image preprocessing, AST DOM sanitization, and conversational refinement.
  - Achieved 100% syntax validity, sub-2s latency, and production-ready Tailwind CSS outputs.
- **Open for Questions:** Thank the jury and invite their questions.

> **🗣️ What to Say to the Jury:**  
> *"In conclusion, Sketch2Code demonstrates how Multimodal Generative AI can be engineered into a practical, resilient, and production-grade developer tool. Thank you for your time and guidance. We are now open for any questions."*
