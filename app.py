import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator")

st.title("🌍 Language Translation Tool")

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
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed")
        st.write("### Translated Text")
        st.write(translated)

    except Exception as e:
        st.error(f"Error: {e}")