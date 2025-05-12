⌄
# 📝 متن‌یار هوشمند

**متن‌یار هوشمند** یک ابزار تعاملی و قدرتمند برای **استخراج، ترجمه و تحلیل متن** از تصاویر، PDF و فایل‌های Word است.  
این برنامه با استفاده از **OCR (Tesseract)**، **Google Translator** و هوش مصنوعی (**GPT-4 و Claude**) قابلیت پردازش متن را در قالب‌های مختلف فراهم می‌کند.

## ✨ قابلیت‌ها

- 🔍 **استخراج متن** از:
  - تصاویر (PNG, JPG, JPEG)
  - فایل‌های PDF
  - فایل‌های Word (DOCX)
- 🌐 **ترجمه هوشمند** به چندین زبان:
  - انگلیسی (en)
  - فارسی (fa)
  - عربی (ar)
  - چینی (zh)
  - ژاپنی (ja)
  - و بیشتر...
- 🤖 **تحلیل هوشمند** با استفاده از:
  - OpenAI GPT-4 Turbo
  - Anthropic Claude 3 Opus
- 📎 **خروجی قابل دانلود**:
  - فایل Word (.docx)
  - فایل PDF (.pdf)

---

## 🧰 فناوری‌های استفاده شده

| فناوری | نقش |
|--------|------|
| **Streamlit** | UI تعاملی |
| **Tesseract OCR** | تشخیص متن در تصاویر |
| **Deep Translator** | ترجمه هوشمند |
| **OpenAI / Anthropic API** | تحلیل هوشمند |
| **python-docx & reportlab** | ایجاد فایل Word و PDF |
| **Streamlit Option Menu & Lottie** | رابط کاربری جذاب و انیمیشن |

---

## 🚀 نحوه راه‌اندازی محلی
a
### ۱. کلون کردن پروژه

```bash
git clone https://github.com/your-username/text-yar.git 
cd text-yar
۲. نصب وابستگی‌ها
ابتدا تمام وابستگی‌ها را نصب کنید:

bash



pip install -r requirements.txt
۳. تنظیم کلید API
الف) در محیط توسعه:
ایجاد یک فایل .env در ریشه پروژه:




OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_claude_key_here
ب) در Streamlit Cloud:
تنظیم secrets.toml در تنظیمات برنامه:

toml


[openai]
api_key = "your-openai-key"

[anthropic]
api_key = "your-anthropic-key"
۴. اجرای برنامه
bash



streamlit run main.py
🌐 دیپلوی روی Streamlit Cloud
۱. ارسال پروژه به GitHub
فایل‌های زیر را در ریپوزیتوری خود قرار دهید:

main.py
requirements.txt
fonts/Vazir.ttf (فونت فارسی)
README.md
۲. دیپلوی در Streamlit Cloud
به Streamlit Cloud بروید.
گزینه New app را بزنید.
URL ریپوزیتوری خود را وارد کنید.
در صورت لزوم، secrets.toml را تنظیم کنید.
📦 وابستگی‌ها (requirements.txt)
txt



streamlit
pytesseract
deep-translator
python-docx
PyPDF2
openai
anthropic
reportlab
requests
python-dotenv
textwrap3
streamlit-option-menu
streamlit-lottie
📁 ساختار پروژه

text-yar/
├── main.py                  # کد اصلی برنامه
├── fonts/
│   └── Vazir.ttf            # فونت فارسی
├── .env                     # کلید API برای development
├── README.md                # مستندات
└── requirements.txt         # لیست وابستگی‌ها
💡 نحوه استفاده
از طریق سایدبار، نوع عملیات را انتخاب کنید: آپلود , ترجمه یا تحلیل
یک فایل آپلود کنید (تصویر، PDF یا Word)
متن استخراج شده را مشاهده کنید
اگر می‌خواهید، متن را ترجمه یا تحلیل کنید
در نهایت فایل را به صورت Word یا PDF دانلود کنید
❤️ مشارکت در پروژه
اگر می‌خواهید در بهتر شدن این پروژه کمک کنید:

Fork کنید
Branch جدید بسازید: git checkout -b feature/new-feature
تغییرات خود را اعمال کنید و commit کنید
Push کنید: git push origin feature/new-feature
Pull request بزنید
📬 پشتیبانی
اگر سوالی داشتید یا با مشکلی مواجه شدید:

ایجاد Issue در GitHub
ایمیل: saeed.norouzi23@gmail.com
❤️ متشکریم!
این پروژه با ❤️ ساخته شده است.
اگر از آن استفاده کردید یا ایده‌هایی برای بهبود آن دارید، خوشحال می‌شویم اطلاع دهید!
