import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="Language Translator")

st.title("🌍 Language Translation Tool")

translator = Translator()

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

text = st.text_area("Enter Text")

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    try:
        translated = translator.translate(
            text,
            src=languages[source],
            dest=languages[target]
        )

        st.success("Translation Completed")
        st.write("### Translated Text")
        st.write(translated.text)

    except Exception as e:
        st.error(f"Error: {e}")