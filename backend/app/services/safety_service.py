class SafetyService:
    def check_safety(self, metadata: dict) -> dict:
        """
        Checks for potential safety violations or risks.
        """
        flags = []
        
        # 1. Aspect Ratio check (extreme ratios are often banners, not logos)
        ar = metadata.get("aspect_ratio", 1.0)
        if ar > 3.0 or ar < 0.33:
            flags.append({
                "type": "format",
                "severity": "Low",
                "message": "Extreme aspect ratio detected. Ensure this is a logo, not a banner."
            })
            
        # 2. File Size check (too small = low quality)
        size_kb = metadata.get("file_size_kb", 0)
        if size_kb < 5:
             flags.append({
                "type": "quality",
                "severity": "Medium",
                "message": "Image file size is very small. Higher resolution is recommended for trademark filing."
            })

        # 3. Format check
        fmt = metadata.get("format", "").upper()
        if fmt not in ["PNG", "JPEG", "JPG", "SVG"]:
             flags.append({
                "type": "format",
                "severity": "Low",
                "message": f"Format {fmt} is less common. PNG or SVG is recommended."
            })

        # 4. Sensitive content (Placeholder - would use a classifier model here)
        # For now, we assume safe unless we detect specific keywords risk keywords in filename (heuristic)
        filename = metadata.get("filename", "").lower()
        if "emblem" in filename or "govt" in filename or "india" in filename:
             flags.append({
                "type": "content",
                "severity": "High",
                "message": "Potential use of restricted National symbols or names. Please verify under Emblems and Names Act."
            })

        return {
            "is_safe": not any(f['severity'] == "High" for f in flags),
            "flags": flags
        }

safety_service = SafetyService()
