"""
Automated Benchmarking Suite for Wireframe-to-UI Synthesis
Runs the pipeline across all benchmark samples and saves metrics to CSV.
"""

import os
import pandas as pd
from PIL import Image

from src.sketch_preprocessor import SketchPreprocessor
from src.ui_vision_generator import UIVisionGenerator
from src.code_sanitizer import CodeSanitizer
from src.sketch_metrics import UIBenchmarkMetrics


def run_benchmark():
    os.makedirs("evaluation", exist_ok=True)
    samples = [
        ("Login Screen", "samples/login_wireframe.png", "login auth form"),
        ("E-Commerce Card", "samples/ecommerce_card.png", "product showcase card"),
        ("Analytics Dashboard", "samples/dashboard_wireframe.png", "analytics dashboard with metrics"),
        ("SaaS Landing Page", "samples/saas_landing_wireframe.png", "modern saas hero landing page")
    ]

    generator = UIVisionGenerator()
    results = []

    print("Running automated benchmark on wireframe samples...")

    for name, path, notes in samples:
        if not os.path.exists(path):
            continue

        raw_img = Image.open(path)
        enhanced_img = SketchPreprocessor.enhance_sketch(raw_img)

        # Generate UI
        raw_html, gen_meta = generator.generate_ui_from_sketch(enhanced_img, style_preset="Modern Clean", user_notes=notes)
        sanitized_html, san_meta = CodeSanitizer.clean_and_sanitize(raw_html)

        # Compute metrics
        latency = gen_meta.get("latency_sec", 0.0)
        metrics = UIBenchmarkMetrics.evaluate_synthesized_html(sanitized_html, latency_sec=latency)
        
        row = {
            "Benchmark Sample": name,
            "Syntax Validity": metrics["syntax_validity_score"],
            "Responsiveness": metrics["responsiveness_score"],
            "Latency (s)": metrics["latency_seconds"],
            "DOM Elements": metrics["dom_elements_count"],
            "Buttons": metrics["buttons_detected"],
            "Inputs": metrics["inputs_detected"],
            "Lines of Code": metrics["lines_of_code"],
            "Tokens Generated": metrics["approx_tokens_generated"],
            "Engine Mode": gen_meta.get("mode", "Standard")
        }
        results.append(row)

    df = pd.DataFrame(results)
    csv_path = "evaluation/benchmark_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved benchmark results to {csv_path}")
    print("\n" + df.to_string(index=False))


if __name__ == "__main__":
    run_benchmark()
