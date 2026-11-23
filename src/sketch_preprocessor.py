"""
Image Preprocessing and Enhancement for Hand-Drawn & Digital Wireframes
Part of the Wireframe Sketch-to-Live UI Capstone Project
"""

import numpy as np
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from typing import Tuple, Dict, Any


class SketchPreprocessor:
    """
    Cleans, contrast-enhances, and standardizes wireframe sketches
    before feeding them into the Multimodal Vision-to-Code generator.
    """

    @staticmethod
    def enhance_sketch(
        image: Image.Image,
        contrast_factor: float = 1.8,
        sharpness_factor: float = 2.0,
        brightness_factor: float = 1.05,
        denoise: bool = True
    ) -> Image.Image:
        """
        Enhances pencil/ink strokes on paper sketches and removes paper grain/shadows.
        """
        # Ensure RGB mode
        if image.mode != "RGB":
            image = image.convert("RGB")

        # 1. Subtle denoising if requested
        if denoise:
            image = image.filter(ImageFilter.SMOOTH_MORE)

        # 2. Adjust brightness & contrast
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness_factor)

        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast_factor)

        # 3. Enhance stroke sharpness
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(sharpness_factor)

        return image

    @staticmethod
    def binarize_sketch(image: Image.Image, threshold: int = 180) -> Image.Image:
        """
        Converts the image to high-contrast black-and-white to isolate
        structural wireframe bounding lines.
        """
        grayscale = image.convert("L")
        # Apply threshold
        table = [0 if i < threshold else 255 for i in range(256)]
        binarized = grayscale.point(table, "1")
        return binarized.convert("RGB")

    @staticmethod
    def auto_standardize(
        image: Image.Image,
        max_size: int = 1024
    ) -> Tuple[Image.Image, Dict[str, Any]]:
        """
        Resizes large camera/scanner photos while preserving aspect ratio
        and extracts image metadata.
        """
        orig_width, orig_height = image.size

        # Compute scaling
        scale = min(max_size / orig_width, max_size / orig_height, 1.0)
        new_width = int(orig_width * scale)
        new_height = int(orig_height * scale)

        if scale < 1.0:
            resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        else:
            resized_image = image

        metadata = {
            "original_resolution": f"{orig_width}x{orig_height}",
            "processed_resolution": f"{new_width}x{new_height}",
            "scaling_ratio": round(scale, 3),
            "aspect_ratio": round(orig_width / orig_height, 2)
        }

        return resized_image, metadata
