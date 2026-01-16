import streamlit as st
from deep_translator import GoogleTranslator, MyMemoryTranslator

# Page Configuration
st.set_page_config(page_title="Arabic ↔ English Translator", page_icon="🌐", layout="centered")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stTextArea textarea {
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Arabic ↔ English Translator")
st.markdown("Professional translation tool for text and e-commerce listings.")

# Sidebar Settings
st.sidebar.header("Settings")
direction = st.sidebar.radio(
    "Select Translation Direction:",
    ("Arabic to English", "English to Arabic")
)

st.sidebar.info("Tip: Use 'English to Arabic' for generating localized product keywords or descriptions.")

# Language Logic
if direction == "Arabic to English":
    source_lang, target_lang = 'ar', 'en'
    input_label = "Arabic Text"
    placeholder = "أدخل النص هنا..."
    btn_text = "Translate to English"
else:
    source_lang, target_lang = 'en', 'ar'
    input_label = "English Text"
    placeholder = "Enter English text here..."
    btn_text = "Translate to Arabic"

# Text Input Area
source_text = st.text_area(f"Enter {input_label}:", placeholder=placeholder, height=200)

col1, col2 = st.columns([1, 5])
with col1:
    translate_btn = st.button(btn_text, type="primary")
with col2:
    if st.button("Clear"):
        st.rerun()

# Translation Logic
if translate_btn:
    if not source_text.strip():
        st.warning("Please enter text to translate.")
    else:
        with st.spinner('Translating...'):
            try:
                # Primary Translation Attempt (Google)
                translation = GoogleTranslator(source='auto', target=target_lang).translate(source_text)
                
                # Validation: If Google returns empty or errors, try MyMemory
                if not translation:
                    translation = MyMemoryTranslator(source=source_lang, target=target_lang).translate(source_text)
                
                st.subheader("Result:")
                
                # Display logic based on language
                if target_lang == 'ar':
                    # Right-to-Left formatting for Arabic
                    st.markdown(
                        f"""
                        <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; 
                        border: 1px solid #ddd; text-align: right; direction: rtl; 
                        font-size: 24px; font-family: 'Arial';">
                            {translation}
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                else:
                    # Standard formatting for English
                    st.success(translation)
                
                # Download Option
                st.download_button(
                    label="Download Translation",
                    data=translation,
                    file_name="translated_output.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}. Please try again in a moment.")

st.divider()
st.caption("Powered by Deep-Translator | Built for Ecommerce Workflow")
