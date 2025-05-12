from docx import Document
from docx.shared import Pt
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import logging

logging.basicConfig(level=logging.INFO)

def create_word_document(text, filename):
    """ایجاد فایل Word"""
    try:
        doc = Document()
        style = doc.styles['Normal']
        style.font.name = 'Vazir'
        style.font.size = Pt(12)
        for para in text.split('\n'):
            p = doc.add_paragraph(para)
            p.style = style
            p.paragraph_format.rtl = True
        doc_buffer = BytesIO()
        doc.save(doc_buffer)
        return doc_buffer
    except Exception as e:
        logging.error(f"Word generation error: {e}")
        return None

def create_pdf_document(text, filename):
    """ایجاد فایل PDF"""
    try:
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer)
        font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Vazir.ttf')
        try:
            pdfmetrics.registerFont(TTFont('Vazir', font_path))
            font_name = 'Vazir'
        except Exception:
            font_name = 'Helvetica'
        c.setFont(font_name, 12)
        y = 800
        for line in text.split('\n'):
            if y < 50:
                c.showPage()
                c.setFont(font_name, 12)
                y = 800
            c.drawRightString(550, y, line)
            y -= 20
        c.save()
        pdf_buffer.seek(0)
        return pdf_buffer
    except Exception as e:
        logging.error(f"PDF generation error: {e}")
        return None