import streamlit as st
import os
from pathlib import Path
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import json
import logging
from dotenv import load_dotenv

# Load modules
from ocr_utils import extract_text_from_image
from translate_utils import safe_translate
from ai_analysis import analyze_with_ai
from document_generation import create_word_document, create_pdf_document

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="متن‌ یار هوشمند", page_icon="📝", layout="wide")

# Sidebar menu
with st.sidebar:
    selected = option_menu("متن‌ یار هوشمند", ["📄 آپلود", "🌐 ترجمه", "🤖 تحلیل"],
                           icons=['cloud-upload', 'globe', 'robot'], menu_icon="app-indicator", default_index=0)

if selected == "📄 آپلود":
    # Upload section
    uploaded_file = st.file_uploader("آپلود فایل")
    if uploaded_file:
        file_type = uploaded_file.type
        if "image" in file_type:
            from PIL import Image
            image = Image.open(uploaded_file)
            st.image(image)
            extracted_text = extract_text_from_image(image)
            if extracted_text:
                st.session_state["extracted_text"] = extracted_text
elif selected == "🌐 ترجمه":
    if "extracted_text" in st.session_state:
        lang = st.selectbox("زبان مقصد", ["en", "fa", "ar"])
        if st.button("ترجمه کن"):
            translated = safe_translate(st.session_state["extracted_text"], lang)
            st.session_state["translated_text"] = translated
elif selected == "🤖 تحلیل":
    if "extracted_text" in st.session_state:
        model = st.selectbox("مدل هوشمند", ["OpenAI", "Claude"])
        api_key = st.secrets[model]["api_key"]
        if st.button("تحلیل کن"):
            result = analyze_with_ai(st.session_state["extracted_text"], model, api_key)
            st.session_state["analysis_text"] = result

# Display results and downloads
...