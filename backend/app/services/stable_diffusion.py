import torch
from diffusers import DiffusionPipeline
import io

class LogoGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LogoGenerator, cls).__new__(cls)
            cls._instance.pipeline = None
        return cls._instance

    def initialize(self):
        if self.pipeline is None:
            print("Loading Segmind Tiny-SD model...")
            # Detect device: CUDA > MPS > CPU
            if torch.cuda.is_available():
                device = "cuda"
                dtype = torch.float16
            elif torch.backends.mps.is_available():
                device = "mps"
                dtype = torch.float32
            else:
                device = "cpu"
                dtype = torch.float32

            try:
                self.pipeline = DiffusionPipeline.from_pretrained(
                    "segmind/tiny-sd",
                    torch_dtype=dtype
                )
                self.pipeline.to(device)
                # Enable optimizations for lower memory usage
                if device == "cpu":
                    # On CPU, we can't use some optimizations, but tiny-sd is small enough.
                    pass
                else:
                    self.pipeline.enable_attention_slicing()
                
                print(f"Model loaded successfully on {device}")
            except Exception as e:
                print(f"Failed to load model: {e}")
                raise e

    def generate(self, prompt: str, negative_prompt: str = "") -> bytes:
        if self.pipeline is None:
            self.initialize()

        # Enhance prompt for logo generation
        enhanced_prompt = f"{prompt}, centered vector logo, white background, minimal, professional, high quality, 2d, flat design"
        enhanced_negative_prompt = f"{negative_prompt}, blurry, low quality, watermarks, text, realistic photo, complex details, 3d render, gradient background, noisy"

        image = self.pipeline(
            prompt=enhanced_prompt,
            negative_prompt=enhanced_negative_prompt,
            num_inference_steps=20, # 20 is usually enough for Tiny-SD
            guidance_scale=7.5,
            height=512,
            width=512
        ).images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return img_byte_arr.getvalue()

# Global instance
logo_generator = LogoGenerator()
