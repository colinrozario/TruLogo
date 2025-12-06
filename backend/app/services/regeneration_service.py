import random
import base64
from PIL import Image, ImageDraw, ImageFont
import io

class RegenerationService:
    def generate_alternatives(self, original_image_bytes: bytes, risk_score: float) -> list:
        """
        Generates alternative logo concepts.
        In a real production environment, this would call Stable Diffusion / Replicate API.
        For this MVP, we will return mock generated images (simple variations).
        """
        
        # If risk is low, we might not need to regenerate, but user can force it.
        # We'll generate 2 variants.
        
        variants = []
        
        try:
            original = Image.open(io.BytesIO(original_image_bytes)).convert("RGB")
            
            # Variant 1: Grayscale / Minimalist
            # In real AI, this would be prompt: "minimalist vector logo, b&w"
            var1 = original.convert("L").convert("RGB")
            # Enhance contrast
            # ...
            
            variants.append({
                "type": "Minimalist",
                "description": "A simplified, cleaner version to reduce visual clutter and similarity.",
                "image_b64": self._img_to_b64(var1)
            })
            
            # Variant 2: Inverted / Color Shift
            # In real AI, this would be "modern logo, different color palette"
            var2 = original.copy()
            pixels = var2.load()
            for i in range(var2.size[0]):
                for j in range(var2.size[1]):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = (255-r, 255-g, 255-b)
            
            variants.append({
                "type": "Inverted Contrast",
                "description": "High contrast variation with inverted colors for distinctiveness.",
                "image_b64": self._img_to_b64(var2)
            })

        except Exception as e:
            print(f"Error generating variants: {e}")
            
        return variants

    def _img_to_b64(self, img: Image.Image) -> str:
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

regeneration_service = RegenerationService()
