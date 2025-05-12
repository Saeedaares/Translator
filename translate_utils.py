from deep_translator import GoogleTranslator
import textwrap
import time
import logging

logging.basicConfig(level=logging.INFO)

def safe_translate(text, target_lang, max_retries=3):
    """ترجمه متن با مدیریت rate limit"""
    for attempt in range(max_retries):
        try:
            paragraphs = text.split('\n')
            translated_paragraphs = []
            for paragraph in paragraphs:
                if not paragraph.strip():
                    continue
                chunks = textwrap.wrap(paragraph, width=1000)
                translator = GoogleTranslator(source='auto', target=target_lang)
                translated_chunks = [translator.translate(chunk) or chunk for chunk in chunks]
                translated_paragraphs.append(' '.join(translated_chunks))
            return '\n'.join(translated_paragraphs)
        except Exception as e:
            if attempt == max_retries - 1:
                logging.error(f"Translation failed after {max_retries} attempts: {e}")
                return None
            time.sleep(2 ** attempt)