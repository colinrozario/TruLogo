from PIL import Image
import io
import os
from datetime import datetime

class MetadataService:
    def extract_metadata(self, image_bytes: bytes, filename: str) -> dict:
        """
        Extracts metadata from the uploaded image.
        """
        try:
            image = Image.open(io.BytesIO(image_bytes))
            
            # Basic attributes
            width, height = image.size
            format = image.format
            mode = image.mode
            
            # File size in KB
            file_size_kb = len(image_bytes) / 1024
            
            # Color palette (simplified to dominant color for now)
            # In a real app, we'd use k-means clustering
            dominant_color = self._get_dominant_color(image)
            
            # EXIF Data (if available)
            exif_data = image.getexif()
            exif_info = {}
            if exif_data:
                for tag_id, value in exif_data.items():
                    # We could decode tag_id here, but keeping it simple for now
                    exif_info[tag_id] = str(value)

            # Metadata object
            return {
                "filename": filename,
                "width": width,
                "height": height,
                "format": format,
                "mode": mode,
                "file_size_kb": round(file_size_kb, 2),
                "aspect_ratio": round(width / height, 2),
                "dominant_color": dominant_color,
                "has_exif": bool(exif_info), # Flag if EXIF is present
                "timestamp": datetime.now().isoformat(),
                # "exif_raw": exif_info # avoiding huge payload
            }
        except Exception as e:
            print(f"Error extracting metadata: {e}")
            return {}

    def _get_dominant_color(self, image: Image.Image):
        """
        Resize image to 1x1 and get the color.
        """
        try:
            img = image.copy()
            img = img.convert("RGB")
            img = img.resize((1, 1), resample=0)
            color = img.getpixel((0, 0))
            return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
        except:
            return "#000000"

metadata_service = MetadataService()
