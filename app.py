import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Bi-Directional Translator", page_icon="🔄")

st.title("🔄 Arabic ↔ English Translator")

# Sidebar for direction selection
direction = st.sidebar.radio(
    "Select Translation Direction:",
    ("Arabic to English", "English to Arabic")
)

# Set language codes based on selection
if direction == "Arabic to English":
    source_lang, target_lang = 'ar', 'en'
    input_label = "Arabic Text:"
    placeholder = "أدخل النص هنا..."
else:
    source_lang, target_lang = 'en', 'ar'
    input_label = "English Text:"
    placeholder = "Enter text here..."

# Text Input
source_text = st.text_area(input_label, placeholder=placeholder, height=200)

if st.button("Translate"):
    if source_text.strip() == "":
        st.warning("Please enter text to translate.")
    else:
        try:
            translation = GoogleTranslator(source=source_lang, target=target_lang).translate(source_text)
            
            st.subheader("Result:")
            # Adding 'rtl' (Right-to-Left) support for Arabic output
            if target_lang == 'ar':
                st.markdown(f'<p style="text-align: right; direction: rtl; font-size: 20px;">{translation}</p>', unsafe_content_bit=True)
            else:
                st.success(translation)
                
            st.download_button("Download Result", translation, file_name="translated_text.txt")
        except Exception as e:
            st.error(f"Error: {e}")

st.sidebar.markdown("---")
st.sidebar.info("This tool is useful for translating customer queries or optimizing multi-lingual backend keywords.")
