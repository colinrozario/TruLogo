import sys
try:
    import easyocr
    print("EasyOCR imported successfully")
    reader = easyocr.Reader(['en'], gpu=False)
    print("EasyOCR initialized successfully")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
