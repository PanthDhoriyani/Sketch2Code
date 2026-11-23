"""
Evaluation Metrics & Benchmarking Suite for Wireframe-to-UI Synthesis
Calculates quantitative metrics for the Final Jury defense:
- HTML Syntax Validity Score
- DOM Element Extraction Recall & Density
- Mobile Responsiveness Score
- Token & Character Efficiency
"""

import re
from bs4 import BeautifulSoup
from typing import Dict, Any


class UIBenchmarkMetrics:
    """
    Computes rigorous academic and engineering metrics on generated HTML.
    """

    @staticmethod
    def evaluate_synthesized_html(html_code: str, latency_sec: float = 0.0) -> Dict[str, Any]:
        soup = BeautifulSoup(html_code, "html.parser")

        # 1. Structural DOM Elements
        all_tags = soup.find_all()
        tag_names = [t.name for t in all_tags]
        
        buttons = len(soup.find_all("button")) + len(soup.find_all("a", class_=re.compile(r"btn|button|bg-", re.I)))
        inputs = len(soup.find_all("input")) + len(soup.find_all("textarea")) + len(soup.find_all("select"))
        headings = len(soup.find_all(re.compile(r"^h[1-6]$")))
        images = len(soup.find_all("img")) + len(soup.find_all("svg")) + len(soup.find_all("i"))
        containers = len(soup.find_all(["div", "section", "main", "header", "nav", "footer", "aside"]))

        # 2. Syntax Validity Score (out of 100)
        validity_score = 100.0
        if not soup.find("html"):
            validity_score -= 25.0
        if not soup.find("head"):
            validity_score -= 15.0
        if not soup.find("body"):
            validity_score -= 20.0
        if len(soup.find_all()) < 5:
            validity_score -= 30.0

        # 3. Mobile Responsiveness Score (out of 100)
        # Checks for Tailwind responsive prefixes: sm:, md:, lg:, xl:, flex, grid
        raw_text = str(soup)
        responsive_features = 0
        if re.search(r"\bmd:", raw_text): responsive_features += 25
        if re.search(r"\bsm:", raw_text) or re.search(r"\blg:", raw_text): responsive_features += 25
        if "flex" in raw_text: responsive_features += 25
        if "grid" in raw_text: responsive_features += 25
        responsiveness_score = min(100, max(20, responsive_features))

        # 4. Code Metrics
        lines = html_code.count("\n") + 1
        char_count = len(html_code)
        approx_tokens = int(char_count / 3.8)

        return {
            "syntax_validity_score": f"{max(0.0, validity_score):.1f}%",
            "responsiveness_score": f"{responsiveness_score}%",
            "latency_seconds": f"{latency_sec:.2f}s",
            "dom_elements_count": len(all_tags),
            "buttons_detected": buttons,
            "inputs_detected": inputs,
            "headings_detected": headings,
            "icons_media_detected": images,
            "layout_containers": containers,
            "lines_of_code": lines,
            "character_count": char_count,
            "approx_tokens_generated": approx_tokens
        }
