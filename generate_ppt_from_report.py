"""
Automated PowerPoint (.pptx) Generator Derived Directly from Capstone Project Report
Report Source: CAPSTONE_PROJECT_REPORT_SKETCH2CODE.docx
Produces a 15-slide, high-impact 16:9 presentation deck with comprehensive speaker notes.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


def build_presentation(output_filepaths):
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 Widescreen
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Academic Theme Palette
    NAVY = RGBColor(30, 58, 138)         # #1E3A8A - Deep Academic Navy
    ROYAL = RGBColor(37, 99, 235)        # #2563EB - Tech Royal Blue
    LIGHT_BG = RGBColor(248, 250, 252)   # #F8FAFC - Clean Off-White Background
    CARD_BG = RGBColor(255, 255, 255)    # #FFFFFF - Pure White Card
    BORDER_COLOR = RGBColor(226, 232, 240)# #E2E8F0 - Subtle Card Border
    TEXT_DARK = RGBColor(15, 23, 42)     # #0F172A - High Contrast Dark Slate
    TEXT_MUTED = RGBColor(100, 116, 139) # #64748B - Slate Muted
    WHITE = RGBColor(255, 255, 255)
    EMERALD = RGBColor(16, 185, 129)     # #10B981 - Success & Verification
    ROSE = RGBColor(225, 29, 72)         # #E11D48 - Bottlenecks & Warnings
    AMBER = RGBColor(217, 119, 6)        # #D97706 - Key Callouts

    def apply_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = LIGHT_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, chapter_tag="CAPSTONE PROJECT REPORT | GENERATIVE AI"):
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
        banner.fill.solid()
        banner.fill.fore_color.rgb = NAVY
        banner.line.color.rgb = NAVY

        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = chapter_tag.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RGBColor(147, 197, 253)

        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.44), Inches(11.5), Inches(0.6))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE

    def add_card(slide, left, top, width, height, title, items, accent_color=ROYAL, bg_color=CARD_BG):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.15), width - Inches(0.5), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = accent_color
        p_t.space_after = Pt(8)

        for item in items:
            p = tf.add_paragraph()
            p.font.size = Pt(10.5)
            p.space_after = Pt(5)
            p.line_spacing = 1.15

            if isinstance(item, tuple):
                r_prefix = p.add_run()
                r_prefix.text = item[0]
                r_prefix.font.bold = True
                r_prefix.font.color.rgb = NAVY
                r_text = p.add_run()
                r_text.text = item[1]
                r_text.font.color.rgb = TEXT_DARK
            else:
                p.text = f"• {item}"
                p.font.color.rgb = TEXT_DARK

    def add_metric_callout(slide, left, top, width, height, value, label, subtext="", color=ROYAL):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE
        box.line.color.rgb = BORDER_COLOR
        box.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left, top + Inches(0.1), width, height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = value
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = label
        p2.font.size = Pt(10.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_DARK
        p2.alignment = PP_ALIGN.CENTER

        if subtext:
            p3 = tf.add_paragraph()
            p3.text = subtext
            p3.font.size = Pt(9)
            p3.font.color.rgb = TEXT_MUTED
            p3.alignment = PP_ALIGN.CENTER

    # ==========================================================
    # SLIDE 1: COVER & TITLE SLIDE
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.1), Inches(5.2), Inches(0.45))
    badge.fill.solid()
    badge.fill.fore_color.rgb = ROYAL
    badge.line.fill.background()
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "FINAL YEAR B.TECH CAPSTONE PROJECT REPORT DEFENSE"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = WHITE
    p_b.alignment = PP_ALIGN.CENTER

    tb_t = s1.shapes.add_textbox(Inches(0.8), Inches(1.75), Inches(11.8), Inches(2.2))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True

    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "SKETCH2CODE: MULTIMODAL GENERATIVE AI FOR AUTOMATED WIREFRAME-TO-RESPONSIVE CODE SYNTHESIS"
    p_t1.font.size = Pt(28)
    p_t1.font.bold = True
    p_t1.font.color.rgb = WHITE
    p_t1.space_after = Pt(12)

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "An End-to-End System Coupling Computer Vision Preprocessing, Spatial-Grounded Vision Transformers, Deterministic AST DOM Sanitization, and Conversational Refinement."
    p_t2.font.size = Pt(15)
    p_t2.font.color.rgb = RGBColor(191, 219, 254)

    card_meta = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.5), Inches(11.733), Inches(2.3))
    card_meta.fill.solid()
    card_meta.fill.fore_color.rgb = RGBColor(15, 23, 42)
    card_meta.line.color.rgb = RGBColor(51, 65, 85)

    tb_m = s1.shapes.add_textbox(Inches(1.1), Inches(4.7), Inches(11.1), Inches(1.9))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    pm1 = tf_m.paragraphs[0]
    pm1.text = "ACADEMIC & CANDIDATE METADATA"
    pm1.font.size = Pt(12)
    pm1.font.bold = True
    pm1.font.color.rgb = RGBColor(147, 197, 253)
    pm1.space_after = Pt(6)

    pm2 = tf_m.add_paragraph()
    pm2.text = "• Candidate: Panth Dhoriyani | Final Year B.Tech Computer Science & Engineering\n" \
               "• Degree & Department: Bachelor of Technology (B.Tech), Dept. of Computer Science & Engineering\n" \
               "• Course & Focus: Generative AI Capstone | Multimodal Deep Learning & Compiler Guardrails\n" \
               "• Defense Year: 2026 | Repository: https://github.com/PanthDhoriyani/Sketch2Code"
    pm2.font.size = Pt(12)
    pm2.font.color.rgb = RGBColor(226, 232, 240)
    pm2.line_spacing = 1.3

    s1.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Respected jury members, good morning. Today I present my Final Year Capstone Project: Sketch2Code—a Multimodal Generative AI "
        "system designed for automated wireframe-to-responsive code synthesis. This presentation directly reflects our formal "
        "academic report. It covers our theoretical progression from baseline statistical models to deep multimodal transformers, "
        "our 4-tier engineering architecture, quantitative benchmark telemetry across canonical wireframes, and our interactive live studio."
    )

    # ==========================================================
    # SLIDE 2: EXECUTIVE ABSTRACT & SCOPE
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s2)
    add_header(s2, "Executive Abstract & Research Scope", "REPORT ABSTRACT | EXECUTIVE SUMMARY")

    add_card(s2, Inches(0.8), Inches(1.4), Inches(7.5), Inches(5.6),
             "Formal Academic Abstract", [
                 ("The Engineering Latency Bottleneck: ", "Frontend engineers spend 30% to 50% of sprint cycles manually translating whiteboard sketches and paper mockups into boilerplate HTML5/CSS."),
                 ("Proposed Multi-Tier Architecture: ", "Sketch2Code resolves this through 4 integrated tiers: (1) adaptive OpenCV contrast & edge preprocessing, (2) spatial-grounded multimodal vision-language generation, (3) deterministic BeautifulSoup AST DOM sanitization, and (4) split-screen interactive web studio."),
                 ("Eliminating Naive LLM Failure Modes: ", "Standard LLMs fail on sketches by emitting broken tags, missing CSS CDNs, and hallucinating phantom UI elements. Our AST compiler guardrail mathematically enforces 100% W3C HTML5 compliance."),
                 ("Empirical Outcomes: ", "Evaluated across 4 canonical UI paradigms, achieving 100% syntax validity, sub-3.5s latency, and full mobile responsiveness.")
             ], ROYAL)

    add_card(s2, Inches(8.6), Inches(1.4), Inches(3.9), Inches(2.6),
             "Core System Capabilities", [
                 ("Input: ", "Raw hand-drawn paper sketch or digital mockup."),
                 ("Output: ", "W3C valid HTML5 + Tailwind CSS 3.4+."),
                 ("Latency: ", "Sub-3.5s end-to-end (sub-1s on Groq LPU)."),
                 ("Target: ", "Production-ready rapid prototyping.")
             ], EMERALD)

    add_card(s2, Inches(8.6), Inches(4.2), Inches(3.9), Inches(2.8),
             "Research Keywords", [
                 ("Multimodal Generative AI: ", "VLM token alignment."),
                 ("Vision-to-Code Synthesis: ", "Automated frontend generation."),
                 ("AST DOM Sanitization: ", "Compiler-grade reliability."),
                 ("Tailwind CSS: ", "Utility-first responsive styling."),
                 ("Spatial Grounding: ", "Preserving layout geometry.")
             ], NAVY)

    s2.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Here is the executive abstract from our report. In agile software development, translating design mockups into frontend "
        "code is a massive latency bottleneck. While naive LLMs produce broken HTML tags and miss CSS sheets, Sketch2Code combines "
        "computer vision preprocessing, spatial-grounded vision models, and an AST DOM compiler guardrail. Across four standard UI scenarios, "
        "the system delivers guaranteed 100% W3C validity with sub-3.5 second latency."
    )

    # ==========================================================
    # SLIDE 3: CHAPTER 1 - PROBLEM STATEMENT & BOTTLENECK
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s3)
    add_header(s3, "Chapter 1: The Frontend Prototyping Bottleneck", "CHAPTER 1: INTRODUCTION & PROBLEM STATEMENT")

    add_card(s3, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.6),
             "The 4 Failure Modes of Manual Scaffolding", [
                 ("1. Visual-Spatial Discrepancies: ", "Developers misinterpret designer layout intent and proportions, causing costly redesign cycles during sprint reviews."),
                 ("2. Boilerplate Proliferation: ", "Hand-writing repetitive flex containers, grid classes, and input wrappers wastes up to 20 hours per developer per sprint."),
                 ("3. Responsiveness Omissions: ", "Hand-crafted mockups omit tablet and mobile breakpoints during initial design, forcing retrofitted media queries later."),
                 ("4. Semantic Inconsistencies: ", "Fast manual coding frequently skips semantic HTML5 landmarks (<header>, <main>, <nav>), hurting web accessibility (a11y) and SEO.")
             ], ROSE)

    add_card(s3, Inches(6.7), Inches(1.4), Inches(5.8), Inches(2.8),
             "Formal Mathematical Problem Statement", [
                 ("Given: ", "An unconstrained 2D raster image I in R^{H x W x 3} of a hand-drawn or digital wireframe with variable stroke intensities, paper shadows, and handwritten text."),
                 ("Objective: ", "Learn a generative mapping function f: I -> C where C is an ordered sequence of semantic HTML5 DOM nodes and Tailwind utility tokens."),
                 ("Constraints: ", "Guaranteed syntactic validity V(C) = 1, layout fidelity S(C, I) > 0.85, and interactive inference latency T(f) < 5.0 seconds.")
             ], NAVY)

    add_card(s3, Inches(6.7), Inches(4.4), Inches(5.8), Inches(2.6),
             "Quantified Industry Impact", [
                 ("20 Hours / Sprint: ", "Dedicated purely to static layout boilerplate before business logic."),
                 ("30% - 50% Latency: ", "Of sprint cycles consumed during UX-to-frontend handoff."),
                 ("Goal of Sketch2Code: ", "Compress this multi-hour transcription down to 3.5 seconds.")
             ], ROYAL)

    s3.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Chapter 1 of our report details the frontend prototyping bottleneck. Frontend engineers routinely spend 20 hours per sprint "
        "writing repetitive layout boilerplate. The manual process creates spatial discrepancies, omission of responsive breakpoints, "
        "and semantic accessibility issues. We mathematically formulate this as an image-to-code mapping function that must produce "
        "syntactically valid HTML with layout fidelity under strict 5-second latency constraints."
    )

    # ==========================================================
    # SLIDE 4: CHAPTER 1 - PROJECT OBJECTIVES & SCOPE
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s4)
    add_header(s4, "Chapter 1: Project Objectives & Scope Boundaries", "CHAPTER 1: SCOPE & ENGINEERING OBJECTIVES")

    add_card(s4, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "Core Objectives (1 & 2)", [
                 ("1. Robust Visual Perception: ", "Build an automated image enhancement pipeline capable of normalizing camera photos, desk shadows, and faint pencil strokes without losing structural boundaries."),
                 ("2. Spatial-Grounded Synthesis: ", "Design specialized few-shot prompt architectures that enforce 1-to-1 spatial coordinate mapping, verbatim handwritten OCR transcription, and modern Tailwind component styling.")
             ], ROYAL)

    add_card(s4, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "Core Objectives (3 & 4)", [
                 ("3. Deterministic DOM Guardrail: ", "Develop a post-generation Abstract Syntax Tree (AST) compiler guardrail using BeautifulSoup to mathematically guarantee 100% W3C HTML5 compliance."),
                 ("4. Conversational Refinement: ", "Implement an iterative conversational workbench allowing engineers to modify generated code using natural language instructions (e.g., 'Switch to dark mode').")
             ], NAVY)

    add_card(s4, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "Objective 5 & Scope", [
                 ("5. Empirical Benchmarking: ", "Establish an automated evaluation suite measuring syntax validity, mobile responsiveness adaptation, latency, and DOM element extraction density."),
                 ("In Scope: ", "HTML5, Tailwind CSS 3.4+, FontAwesome 6, responsive grids, cross-provider cloud VLM and local offline fallback."),
                 ("Out of Scope: ", "Backend database connections, server routing, and state stores (targeted for future work).")
             ], EMERALD)

    s4.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "To systematically address the problem, our project established five clear engineering objectives: robust visual perception "
        "via OpenCV, spatial-grounded code generation, deterministic AST DOM sanitization, conversational refinement, and quantitative "
        "benchmarking. We deliberately scope our output to responsive HTML5 and Tailwind CSS with modern CDNs to ensure clean, deployable code."
    )

    # ==========================================================
    # SLIDE 5: CHAPTER 2 - THEORETICAL EVOLUTION (MARKOV TO TRANSFORMERS)
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s5)
    add_header(s5, "Chapter 2: Evolution of Generative Sequence Models", "CHAPTER 2: THEORETICAL FOUNDATION & LITERATURE REVIEW")

    add_card(s5, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "1. Discrete Markov Chains", [
                 ("Statistical Foundation: ", "Operates under the Markov assumption: P(c_t | c_1..c_{t-1}) approx P(c_t | c_{t-n+1}..c_{t-1})."),
                 ("Parameter Estimation: ", "Maximum Likelihood Estimation (MLE) counts discrete n-gram transitions in corpus."),
                 ("Fatal Bottleneck: ", "Curse of Dimensionality: parameter space scales exponentially as O(|V|^n)."),
                 ("Outcome: ", "For n >= 5, discrete lookup tables suffer severe data sparsity, causing either Laplace smoothing failure or rigid memorization.")
             ], NAVY)

    add_card(s5, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "2. Recurrent Neural Networks & LSTMs", [
                 ("Continuous Latent Space: ", "Projects discrete vocabulary tokens into dense continuous vectors (embeddings)."),
                 ("Hidden State Memory: ", "Maintains hidden state h_t and cell state c_t regulated by input, forget, and output gating mechanisms."),
                 ("Complexity: ", "Fixed parameter footprint O(d*h + h^2) independent of sequence length."),
                 ("Limitation: ", "Vanishing gradients over extended spatial sequences prevent multi-column UI synthesis.")
             ], ROYAL)

    add_card(s5, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "3. Multimodal Transformers", [
                 ("Attention Mechanism: ", "Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V captures global spatial relationships."),
                 ("Patch Tokenization: ", "Vision Transformer (ViT) partitions input image into 16x16 non-overlapping visual patches."),
                 ("Cross-Attention Alignment: ", "Multimodal projection layer aligns visual patches directly with text decoder token space."),
                 ("Outcome: ", "Enables simultaneous reasoning across visual sketch geometry and structural HTML code.")
             ], EMERALD)

    s5.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Chapter 2 presents the mathematical foundation of sequence modeling. In our baseline project, we studied discrete Markov chains, "
        "which operate under the Markov assumption. However, discrete frequency tables suffer from the curse of dimensionality—scaling as "
        "O(|V|^n)—causing data sparsity. Recurrent networks and LSTMs introduced continuous dense vectors, but struggle with vanishing gradients "
        "across spatial 2D layouts. The modern Multimodal Transformer resolves this by treating image patches and code tokens as a unified "
        "sequence under self-attention."
    )

    # ==========================================================
    # SLIDE 6: CHAPTER 2 - MULTIMODAL VLMs & CRITIQUE OF PRIOR ART
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s6)
    add_header(s6, "Chapter 2: Multimodal VLMs & Analysis of Prior Art", "CHAPTER 2: LITERATURE REVIEW & COMPETITIVE CRITIQUE")

    add_card(s6, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.6),
             "Comparative Analysis of Prior Art", [
                 ("Classical OpenCV Contour Heuristics: ", "Relied on edge detectors and bounding box thresholding. Fails completely on messy handwritten sketches, overlapping strokes, and textured paper."),
                 ("Pix2Code (Beltramelli, 2018): ", "Pioneered CNN-LSTM dual-branch models. However, it was restricted to synthetic, uniform mockups and generated non-responsive custom DSL tokens rather than production code."),
                 ("Commercial Naive LLM Prompting: ", "Sending raw images to generic LLMs produces syntax hallucinations, unclosed tags, missing CSS CDNs, and arbitrary layout distortions."),
                 ("The Sketch2Code Advantage: ", "Couples computer vision preprocessing with spatial grounding prompts and deterministic AST DOM repair, guaranteeing 100% W3C validity.")
             ], NAVY)

    add_card(s6, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.6),
             "The Multimodal VLM Architecture", [
                 ("Visual Patch Projection: ", "Input sketch is partitioned into 16x16 pixel patches, flattened, and projected into a linear embedding space."),
                 ("Spatial Coordinate Grounding: ", "Positional encodings preserve relative 2D coordinate positions (top-left, center, bottom-right)."),
                 ("Cross-Modal Attention: ", "The decoder computes attention weights between visual bounding elements (boxes, icons) and HTML tags (input, button, grid)."),
                 ("Zero-Shot Spatial Mapping: ", "Allows the model to deduce flex-row or grid-cols-3 layout structures directly from drawn geometric proximity.")
             ], ROYAL)

    s6.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Critiquing prior art: Classical OpenCV contour detectors require hand-tuned thresholds and fail on handwriting. Beltramelli's "
        "Pix2Code was limited to synthetic mockups and custom domain-specific languages. Unassisted LLM prompting frequently hallucinates "
        "invalid code. Sketch2Code leverages modern Vision Transformers with patch projection and cross-attention, backed by an AST "
        "compiler guardrail to eliminate probabilistic errors."
    )

    # ==========================================================
    # SLIDE 7: CHAPTER 3 - END-TO-END SYSTEM ARCHITECTURE
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s7)
    add_header(s7, "Chapter 3: End-to-End System Architecture", "CHAPTER 3: SYSTEM ARCHITECTURE & METHODOLOGY")

    add_card(s7, Inches(0.8), Inches(1.4), Inches(2.7), Inches(5.6),
             "Tier 1: CV Preprocessor", [
                 ("Module: ", "sketch_preprocessor.py"),
                 ("Aspect Normalization: ", "Max 1024px, preserving UI aspect ratio."),
                 ("Sensor Denoising: ", "3x3 median filtering."),
                 ("Contrast Scaling: ", "1.8x non-linear expansion."),
                 ("Edge Sharpening: ", "2.0x Laplacian kernel."),
                 ("Binarization: ", "Adaptive threshold T=180.")
             ], ROYAL)

    add_card(s7, Inches(3.8), Inches(1.4), Inches(2.7), Inches(5.6),
             "Tier 2: Generative Engine", [
                 ("Module: ", "ui_vision_generator.py"),
                 ("Vision Backbone: ", "Groq LPU (Qwen 3.8 / LLaMA), Gemini 3.8 Flash."),
                 ("Spatial Prompts: ", "prompt_templates.py"),
                 ("OCR Transcription: ", "Exact verbatim extraction."),
                 ("Styling Engine: ", "Tailwind CSS utility classes.")
             ], NAVY)

    add_card(s7, Inches(6.8), Inches(1.4), Inches(2.7), Inches(5.6),
             "Tier 3: AST Sanitizer", [
                 ("Module: ", "code_sanitizer.py"),
                 ("Markdown Extraction: ", "Regex boundary parsing."),
                 ("AST Parser: ", "BeautifulSoup tree repair."),
                 ("Tag Auto-Closure: ", "Enforces W3C compliance."),
                 ("CDN Injection: ", "Tailwind 3.4 & FontAwesome 6."),
                 ("Guarantee: ", "100% W3C HTML5 validity.")
             ], EMERALD)

    add_card(s7, Inches(9.8), Inches(1.4), Inches(2.7), Inches(5.6),
             "Tier 4: Studio Workbench", [
                 ("Module: ", "app.py (Streamlit)"),
                 ("Live Rendering: ", "Sandboxed browser preview."),
                 ("Code Inspection: ", "Syntax-highlighted editor."),
                 ("Conversational Refine: ", "Delta-prompt revisions."),
                 ("Jury Telemetry: ", "Real-time metrics calculation.")
             ], AMBER)

    s7.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Chapter 3 introduces our 4-tier system architecture. Tier 1 is our Computer Vision preprocessor that normalizes shadows and "
        "sharpens pencil strokes. Tier 2 is our Multimodal Generative Engine running high-speed vision models with spatial prompts. "
        "Tier 3 is our AST DOM Sanitizer that guarantees W3C compliance and injects CDNs. Tier 4 is our Streamlit Interactive Studio "
        "with live side-by-side rendering, code download, and conversational refinement."
    )

    # ==========================================================
    # SLIDE 8: CHAPTER 3 - CV PREPROCESSING & SPATIAL ENGINE
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s8)
    add_header(s8, "Chapter 3: CV Preprocessing & Spatial Grounding", "CHAPTER 3: METHODOLOGY - TIERS 1 & 2")

    add_card(s8, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.6),
             "Tier 1: Computer Vision Preprocessing Pipeline", [
                 ("1. Aspect-Preserving Scaling: ", "Resizes high-res phone photos to max 1024px while strictly maintaining aspect ratio, preventing column distortion."),
                 ("2. 3x3 Median Denoising: ", "Suppresses high-frequency paper texture and camera sensor noise without eroding thin pencil lines."),
                 ("3. Adaptive Contrast Scaling: ", "Applies 1.8x non-linear contrast scaling and 1.05x brightness leveling, separating graphite marks from off-white paper."),
                 ("4. Laplacian Boundary Sharpening: ", "Applies a 2.0x Laplacian kernel to accentuate button borders, input outlines, and dividers."),
                 ("5. Binary Edge Mask Telemetry: ", "Generates an inverted binary mask using adaptive luminance thresholding (T=180) for structural inspection.")
             ], ROYAL)

    add_card(s8, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.6),
             "Tier 2: Spatial Grounding & Component Mapping", [
                 ("Visual Container Mapping: ", "Boxes marked with diagonal crosses ('X') or mountain/sun icons are mapped to styled <img> containers with Unsplash placeholders."),
                 ("Form Control Recognition: ", "Rectangles with interior text labels are instantiated as accessible <input> or <textarea> elements with matching <label> tags."),
                 ("Action Trigger Mapping: ", "Pill-shaped or rounded rectangles with imperative verbs ('Submit', 'Sign Up') map to interactive <button> tags with hover transitions."),
                 ("Responsive Grid Deduction: ", "Horizontal groupings of 3+ cards trigger responsive Tailwind grid classes: 'grid grid-cols-1 md:grid-cols-3 gap-6'."),
                 ("Exact Handwritten OCR: ", "Transcribes handwritten text verbatim, preventing hallucinated marketing copy.")
             ], NAVY)

    s8.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Examining Tiers 1 and 2 in detail: Raw sketches photographed in classrooms or offices contain uneven lighting and faint lines. "
        "Our OpenCV pipeline normalizes dimensions to 1024px, applies median denoising, and enhances contrast by 1.8x. In Tier 2, "
        "our spatial grounding prompts establish strict mapping rules: 'X' marks become image placeholders, labeled boxes become "
        "form inputs, and horizontal groupings automatically become responsive Tailwind grids."
    )

    # ==========================================================
    # SLIDE 9: CHAPTER 3 - AST COMPILER GUARDRAIL & REFINEMENT
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s9)
    add_header(s9, "Chapter 3: AST Compiler Guardrail & Conversational Loop", "CHAPTER 3: METHODOLOGY - TIERS 3 & 4")

    add_card(s9, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.6),
             "Tier 3: Abstract Syntax Tree (AST) Guardrail", [
                 ("Deterministic Compiler Safety: ", "Probabilistic VLMs occasionally omit closing tags or emit markdown chatter. Tier 3 acts as a deterministic compiler guardrail."),
                 ("1. Regex Markdown Boundary Stripping: ", "Extracts raw code from ```html ... ``` blocks, discarding any conversational commentary."),
                 ("2. BeautifulSoup DOM Tree Parsing: ", "Constructs an in-memory Abstract Syntax Tree. Unclosed tags (e.g. <div> without </div>) are automatically repaired per HTML5 standards."),
                 ("3. Head & CDN Auto-Injection: ", "If <head> is missing or incomplete, auto-injects Tailwind CSS 3.4+ CDN script, FontAwesome 6 icons, and Inter Google fonts."),
                 ("4. Format & Beautify: ", "Emits clean, 2-space indented production code.")
             ], EMERALD)

    add_card(s9, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.6),
             "Tier 4: Conversational Iterative Refinement", [
                 ("The Need for Iterative UX: ", "Design is inherently iterative. Developers need to tweak styling without redrawing wireframes."),
                 ("Architectural Delta Prompting: ", "Pairs the current synthesized HTML DOM structure with the user's natural language revision instruction."),
                 ("Preserving Spatial Structure: ", "Instructs the model to modify colors, fonts, or component hierarchies while strictly preserving core layout geometry."),
                 ("Example Prompts Handled: ", "'Change primary theme to emerald dark mode', 'Add a search box to the header', 'Change card buttons to outlined style'."),
                 ("Immediate Feedback: ", "Synthesizes delta updates in under 2 seconds and re-renders the live browser sandbox instantly.")
             ], ROYAL)

    s9.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Tiers 3 and 4 provide enterprise-grade reliability and usability. Tier 3 is our AST DOM compiler guardrail. We pass the generated "
        "code through BeautifulSoup's AST parser, which auto-closes any orphaned tags, enforces W3C syntax, and injects modern Tailwind and "
        "FontAwesome CDNs. Tier 4 provides conversational refinement: developers can type natural language instructions to switch themes "
        "or add widgets, and our delta engine updates the code without touching the original wireframe."
    )

    # ==========================================================
    # SLIDE 10: CHAPTER 4 - MULTI-PROVIDER ARCHITECTURE
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s10)
    add_header(s10, "Chapter 4: Implementation & Multi-Provider Architecture", "CHAPTER 4: ZERO-DOWNTIME DEFENSE ARCHITECTURE")

    # Provider Table from Report Chapter 4
    table_shape = s10.shapes.add_table(5, 4, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.4))
    table = table_shape.table
    table.columns[0].width = Inches(2.6)
    table.columns[1].width = Inches(2.8)
    table.columns[2].width = Inches(2.0)
    table.columns[3].width = Inches(4.333)

    headers = ["Provider Engine", "Primary Model", "Inference Latency", "Academic Defense Role"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER

    data = [
        ("Groq Cloud (LPU)", "qwen/qwen3.8-27b", "< 0.8s (sub-second)", "Primary high-speed free tier engine (zero queue bottleneck)"),
        ("Google AI Studio", "gemini-3.8-flash", "1.5s - 2.5s", "Google Multimodal Vision cloud engine alternative"),
        ("OpenRouter Hub", "llama-3.2-11b:free", "1.8s - 3.0s", "Open-source vision fallback provider"),
        ("Local Heuristics", "Rule-Guided Engine", "< 0.05s (instant)", "100% offline zero-network failover for uninterrupted demo")
    ]

    for row_idx, row in enumerate(data, start=1):
        bg_c = RGBColor(241, 245, 249) if row_idx % 2 == 1 else WHITE
        for col_idx, text in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(10)
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = NAVY
            else:
                p.font.color.rgb = TEXT_DARK
            if col_idx in [1, 2]:
                p.alignment = PP_ALIGN.CENTER

    add_card(s10, Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.9),
             "Engineering Rationale: Zero-Downtime Defense Strategy", [
                 ("The Real-World Academic Risk: ", "Public cloud APIs frequently return 503 high-demand errors or rate limits during live jury presentations."),
                 ("Architectural Mitigation: ", "Sketch2Code abstracts providers behind a unified interface (`src/ui_vision_generator.py`). If cloud networks stall, the system automatically falls back to Groq LPU or our offline local heuristic generator."),
                 ("Result: ", "Zero presentation downtime, verified across hundreds of generation cycles.")
             ], ROYAL)

    s10.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Chapter 4 addresses a crucial engineering consideration: system resilience during high-stakes defense. Cloud APIs often hit "
        "503 traffic spikes or rate limits. To guarantee uninterrupted evaluation, we implemented a multi-provider failover architecture. "
        "Our primary engine is Groq LPU running Qwen 3.8 at sub-second speeds. We maintain secondary pipelines for Google Gemini and "
        "OpenRouter, and an offline rule-guided fallback synthesizer that requires zero internet connection."
    )

    # ==========================================================
    # SLIDE 11: CHAPTER 5 - EXPERIMENTAL EVALUATION TESTBED
    # ==========================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s11)
    add_header(s11, "Chapter 5: Experimental Evaluation & Benchmark Testbed", "CHAPTER 5: EXPERIMENTAL BENCHMARKING METHODOLOGY")

    add_card(s11, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.6),
             "4 Canonical Wireframe Benchmark Scenarios", [
                 ("1. Authentication Screen (`login_wireframe.png`): ", "Centered auth card, dual text inputs (email, password), 'Remember Me' checkbox, primary submit button, and social OAuth pills."),
                 ("2. E-Commerce Showcase (`ecommerce_card.png`): ", "Product card with image placeholder ('X'), discount badge, title, star ratings, price tags, and 'Add to Cart' CTA button."),
                 ("3. Analytics Dashboard (`dashboard_wireframe.png`): ", "Multi-widget layout: navigation sidebar, stat KPI metric cards (revenue, users), chart container, and recent transactions data table."),
                 ("4. SaaS Hero Landing (`saas_landing_wireframe.png`): ", "Header navbar, hero headline, dual CTA buttons, and a responsive 3-column feature grid with icons and descriptions.")
             ], ROYAL)

    add_card(s11, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.6),
             "Quantitative Evaluation Metrics", [
                 ("1. HTML Syntax Validity Score: ", "Evaluated via DOM AST tree parsing. Confirms complete enclosure of <html>, <head>, <body>, and zero orphaned tags. (Target: 100%)."),
                 ("2. Mobile Viewport Responsiveness: ", "Quantifies the ratio of elements utilizing responsive Tailwind breakpoint prefixes ('sm:', 'md:', 'lg:') and fluid flex/grid layouts. (Target: > 80%)."),
                 ("3. End-to-End Generation Latency: ", "Wall-clock time in seconds from input image submission to complete browser DOM rendering."),
                 ("4. DOM Extraction Density: ", "Total HTML tags generated, form inputs recognized, and interactive buttons instantiated."),
                 ("Automated Runner: ", "Executed via `run_benchmark_eval.py` outputting to `evaluation/benchmark_results.csv`.")
             ], NAVY)

    s11.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Chapter 5 outlines our empirical evaluation methodology. To rigorously test the system, we constructed an automated benchmark "
        "testbed across four canonical UI archetypes: an authentication screen, an e-commerce card, a multi-widget analytics dashboard, "
        "and a SaaS landing page. We evaluate each scenario across four quantitative metrics: HTML syntax validity, mobile responsiveness, "
        "end-to-end generation latency, and DOM element density."
    )

    # ==========================================================
    # SLIDE 12: CHAPTER 5 - EMPIRICAL BENCHMARK RESULTS
    # ==========================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s12)
    add_header(s12, "Chapter 5: Empirical Benchmark Telemetry & Results", "CHAPTER 5: EXPERIMENTAL FINDINGS & QUANTITATIVE RESULTS")

    # Table 5.1 from Report
    table_shape_b = s12.shapes.add_table(5, 7, Inches(0.8), Inches(1.4), Inches(11.733), Inches(3.0))
    tb_bench = table_shape_b.table
    tb_bench.columns[0].width = Inches(2.333)
    tb_bench.columns[1].width = Inches(1.5)
    tb_bench.columns[2].width = Inches(1.5)
    tb_bench.columns[3].width = Inches(1.5)
    tb_bench.columns[4].width = Inches(1.5)
    tb_bench.columns[5].width = Inches(1.5)
    tb_bench.columns[6].width = Inches(1.9)

    b_headers = ["Scenario", "Syntax Validity", "Responsiveness", "Latency", "DOM Tags", "Lines", "Tokens"]
    for i, h in enumerate(b_headers):
        cell = tb_bench.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER

    bench_data = [
        ("Login Screen", "100.0%", "85%", "1.12 s", "37", "80", "853"),
        ("Product Card", "100.0%", "90%", "0.98 s", "31", "68", "685"),
        ("Analytics Dashboard", "100.0%", "100%", "1.65 s", "83", "207", "1,717"),
        ("SaaS Landing Page", "100.0%", "100%", "1.42 s", "49", "119", "1,271")
    ]

    for row_idx, row in enumerate(bench_data, start=1):
        bg_c = RGBColor(241, 245, 249) if row_idx % 2 == 1 else WHITE
        for col_idx, text in enumerate(row):
            cell = tb_bench.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(10)
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = NAVY
            elif col_idx in [1, 2]:
                p.font.bold = True
                p.font.color.rgb = EMERALD
                p.alignment = PP_ALIGN.CENTER
            else:
                p.font.color.rgb = TEXT_DARK
                p.alignment = PP_ALIGN.CENTER

    add_metric_callout(s12, Inches(0.8), Inches(4.7), Inches(2.7), Inches(2.2),
                       "100.0%", "Syntax Validity", "Zero broken or unclosed tags via AST guardrail", EMERALD)

    add_metric_callout(s12, Inches(3.8), Inches(4.7), Inches(2.7), Inches(2.2),
                       "< 1.7 s", "Average Latency", "Sub-second on Groq LPU hardware acceleration", ROYAL)

    add_metric_callout(s12, Inches(6.8), Inches(4.7), Inches(2.7), Inches(2.2),
                       "100%", "Complex Responsiveness", "Full md: & lg: grid layout adaptation", EMERALD)

    add_metric_callout(s12, Inches(9.8), Inches(4.7), Inches(2.7), Inches(2.2),
                       "45%", "Token Reduction", "Tailwind utility classes vs verbose custom CSS", AMBER)

    s12.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Here are the empirical benchmark results from Table 5.1 of our report. Every scenario achieved a flawless 100% syntax "
        "validity rate thanks to our BeautifulSoup AST compiler. Complex multi-widget layouts like the Analytics Dashboard and SaaS Landing "
        "achieved 100% mobile responsiveness. Furthermore, average generation latency remained under 1.7 seconds, comfortably below "
        "human interactive limits, while Tailwind utility classes saved 45% in token consumption compared to standard CSS."
    )

    # ==========================================================
    # SLIDE 13: CHAPTER 6 - CHALLENGES & MITIGATIONS
    # ==========================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s13)
    add_header(s13, "Chapter 6: Engineering Challenges & Trade-Offs", "CHAPTER 6: DISCUSSION, CHALLENGES & ARCHITECTURAL MITIGATIONS")

    add_card(s13, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.6),
             "Real-World Engineering Challenges", [
                 ("1. Handwriting & Stroke Ambiguities: ", "Messy pencil handwriting and overlapping line drawings created OCR confusion in early iterations."),
                 ("2. Cloud API Rate Limits & 503 Traffic Spikes: ", "Free-tier cloud endpoints (like Gemini) routinely experience 503 high-demand blocks during peak hours."),
                 ("3. Token Budget Inflation & Generation Lag: ", "Emitting verbose standard CSS stylesheets consumed excessive tokens, causing latency and syntax truncation."),
                 ("4. Hallucinated Phantom UI Elements: ", "Early unconstrained prompting led the model to invent arbitrary navigation links not present in sketches.")
             ], ROSE)

    add_card(s13, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.6),
             "Architectural Mitigations Implemented", [
                 ("Adaptive Contrast Preprocessing: ", "Applying 1.8x non-linear contrast scaling and Laplacian edge sharpening cleanly isolates handwriting from paper shadows."),
                 ("Multi-Provider Failover Matrix: ", "Implemented primary Groq LPU inference backed by Gemini, OpenRouter, and local offline heuristic synthesizers."),
                 ("Tailwind CSS Standardization: ", "Switching to utility-first Tailwind classes reduced output token count by 45%, cutting generation latency in half."),
                 ("Negative Prompt Constraints: ", "Strict negative rules explicitly penalize the model for adding un-drawn UI components, ensuring 1-to-1 layout fidelity.")
             ], EMERALD)

    s13.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "Chapter 6 discusses the engineering trade-offs and challenges encountered. Handwriting ambiguities were mitigated using adaptive "
        "contrast preprocessing. 503 cloud API rate limits were resolved through our multi-provider failover matrix. Verbose CSS token "
        "inflation was solved by standardizing on Tailwind CSS, which cut token consumption by 45%. Finally, negative prompt constraints "
        "prevented the hallucination of phantom UI elements."
    )

    # ==========================================================
    # SLIDE 14: CHAPTER 7 - CONTRIBUTIONS, FUTURE SCOPE & REFERENCES
    # ==========================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_slide_bg(s14)
    add_header(s14, "Chapter 7: Contributions, Roadmap & References", "CHAPTER 7: CONCLUSION & FUTURE SCOPE")

    add_card(s14, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "Summary of Contributions", [
                 ("1. End-to-End Pipeline: ", "Integrated computer vision preprocessing, multimodal VLM reasoning, and compiler guardrails."),
                 ("2. 100% W3C Validity: ", "Proved that AST parsing guarantees deterministic syntax safety for probabilistic generative AI."),
                 ("3. Real-Time Performance: ", "Sub-1.7s average latency for rapid developer prototyping."),
                 ("4. Conversational Refine: ", "Enables natural language iterative UI styling.")
             ], NAVY)

    add_card(s14, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "Future Engineering Roadmap", [
                 ("React & Vue JSX Synthesis: ", "Extend synthesis from static HTML/Tailwind to modular React (JSX), Vue.js, and Svelte component trees with reactive state hooks."),
                 ("IDE & Design Tool Extensions: ", "Build native plugins for VS Code and Figma allowing whiteboard photos to paste directly into project source trees."),
                 ("Automated Mock Backends: ", "Generate mock REST endpoints and JSON fixtures matching recognized form fields.")
             ], ROYAL)

    add_card(s14, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.6),
             "Key Academic Bibliography", [
                 ("Beltramelli (2018): ", "Pix2Code: Generating code from GUI screenshots (ACM EICS)."),
                 ("Vaswani et al. (2017): ", "Attention Is All You Need (NeurIPS)."),
                 ("Dosovitskiy et al. (2020): ", "ViT: Transformers for Image Recognition at Scale (ICLR)."),
                 ("Radford et al. (2021): ", "CLIP: Learning Transferable Visual Models (ICML)."),
                 ("Tailwind Labs (2024): ", "Tailwind CSS Utility-First Documentation."),
                 ("W3C (2023): ", "HTML5 & DOM Living Standard.")
             ], EMERALD)

    s14.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "In Chapter 7, we summarize our contributions: a complete multimodal vision-to-code pipeline with 100% W3C validity and conversational "
        "refinement. For future work, our architecture can be naturally extended to generate modular React JSX components, Figma plugins, "
        "and automated mock REST backends. Our bibliography anchors this work in seminal papers including Pix2Code, Transformers, and ViT."
    )

    # ==========================================================
    # SLIDE 15: CONCLUSION & LIVE DEMONSTRATION TRANSITION
    # ==========================================================
    s15 = prs.slides.add_slide(blank_layout)
    bg15 = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg15.fill.solid()
    bg15.fill.fore_color.rgb = NAVY
    bg15.line.fill.background()

    tb_end = s15.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.333), Inches(5.0))
    tf_e = tb_end.text_frame
    tf_e.word_wrap = True

    pe1 = tf_e.paragraphs[0]
    pe1.text = "CONCLUSION & TRANSITION TO LIVE SYSTEM DEMONSTRATION"
    pe1.font.size = Pt(15)
    pe1.font.bold = True
    pe1.font.color.rgb = RGBColor(147, 197, 253)
    pe1.space_after = Pt(12)

    pe2 = tf_e.add_paragraph()
    pe2.text = "Sketch2Code demonstrates that Multimodal Generative AI can be engineered into a deterministic, production-grade frontend synthesis tool."
    pe2.font.size = Pt(23)
    pe2.font.bold = True
    pe2.font.color.rgb = WHITE
    pe2.space_after = Pt(24)

    pe3 = tf_e.add_paragraph()
    pe3.text = "Now proceeding to:\n" \
               "1. Source Code Walkthrough (`src/` architecture, OpenCV filters & AST compiler guardrail)\n" \
               "2. Live Interactive Studio Demonstration (`http://localhost:8501`)\n" \
               "   • Synthesis of complex Analytics Dashboard & E-Commerce Card in < 3.5s\n" \
               "   • Conversational Prompt Refinement ('Switch to dark mode with emerald accents')\n" \
               "3. Viva Defense & Jury Q&A Examination"
    pe3.font.size = Pt(16)
    pe3.font.color.rgb = RGBColor(224, 231, 255)
    pe3.line_spacing = 1.35

    s15.notes_slide.notes_text_frame.text = (
        "SPEAKER SCRIPT:\n"
        "In conclusion, Sketch2Code proves that Generative AI can be transformed from experimental chat demos into a rigorous, "
        "deterministic software engineering tool. We will now transition to the live demonstration phase. I will guide you through "
        "our Python codebase and compiler guardrails, execute live wireframe synthesis in our Streamlit studio, demonstrate "
        "conversational prompt refinement, and invite your questions for our viva examination. Thank you."
    )

    # Save to all requested paths
    for path in output_filepaths:
        try:
            prs.save(path)
            print(f"Presentation saved successfully: {path}")
        except PermissionError:
            print(f"Notice: {path} is currently open in PowerPoint. Closed file required for overwrite. New file is available at SKETCH2CODE_CAPSTONE_REPORT_PRESENTATION.pptx")
        except Exception as e:
            print(f"Error saving {path}: {e}")


if __name__ == "__main__":
    outputs = [
        "SKETCH2CODE_CAPSTONE_REPORT_PRESENTATION.pptx",
        "FINAL_JURY_PRESENTATION_SKETCH2CODE.pptx"
    ]
    build_presentation(outputs)
