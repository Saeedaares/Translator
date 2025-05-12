import openai
from anthropic import Anthropic
import logging

logging.basicConfig(level=logging.INFO)

def analyze_with_ai(text, model_name, api_key):
    """تحلیل متن با استفاده از OpenAI یا Claude"""
    try:
        if model_name == "OpenAI":
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[{"role": "user", "content": text}]
            )
            return response.choices[0].message.content
        elif model_name == "Claude":
            client = Anthropic(api_key=api_key)
            response = client.messages.create(
                model="claude-3-opus-20240229",
                messages=[{"role": "user", "content": text}]
            )
            return response.content[0].text
    except Exception as e:
        logging.error(f"AI analysis error: {e}")
        return None