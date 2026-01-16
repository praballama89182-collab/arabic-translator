import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Pro Translator", page_icon="🌐")

st.title("🌐 Universal to Arabic/English Translator")

# Direction Selection
direction = st.sidebar.radio(
    "Select Target Language:",
    ("To English", "To Arabic")
)

if direction == "To English":
    target_lang = 'en'
    input_label = "Source Text (Any Language):"
    placeholder = "e.g., Maison de L'Avenir"
else:
    target_lang = 'ar'
    input_label = "Source Text (Any Language):"
    placeholder = "e.g., Maison de L'Avenir"

source_text = st.text_area(input_label, placeholder=placeholder, height=150)

if st.button("Translate"):
    if source_text.strip():
        with st.spinner('Detecting language and translating...'):
            try:
                # Use 'auto' for source to catch French, English, etc.
                translator = GoogleTranslator(source='auto', target=target_lang)
                translation = translator.translate(source_text)
                
                st.subheader("Result:")
                if target_lang == 'ar':
                    # Professional RTL display
                    st.markdown(
                        f'<div style="text-align: right; direction: rtl; font-size: 24px; '
                        f'padding: 20px; border: 1px solid #ddd; border-radius: 10px; background: white;">'
                        f'{translation}</div>', 
                        unsafe_allow_html=True
                    )
                else:
                    st.success(translation)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter text.")

st.sidebar.markdown("---")
st.sidebar.info("Note: Brand names like 'Maison de L'Avenir' are detected as French and translated accordingly.")
