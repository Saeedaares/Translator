from PIL import Image
import pytesseract
import logging

logging.basicConfig(level=logging.INFO)

def enhance_image_before_ocr(image):
    """پیش‌پردازش تصویر قبل از OCR"""
    try:
        img = Image.fromarray(image)
        img = img.convert('L')  # تبدیل به سیاه و سفید
        img = img.point(lambda x: 0 if x < 128 else 255)  # افزایش کنتراست
        return img
    except Exception as e:
        logging.error(f"Error enhancing image: {e}")
        raise

def extract_text_from_image(image):
    """استخراج متن از تصویر با Tesseract"""
    try:
        text = pytesseract.image_to_string(enhance_image_before_ocr(image))
        return text.strip()
    except Exception as e:
        logging.error(f"OCR error: {e}")
        return None