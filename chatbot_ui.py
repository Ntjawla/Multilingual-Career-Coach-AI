
import streamlit as st
from core_llm import get_llama_response
from translator import detect_lang, translate_text
from resume_analysis import analyze_resume

st.set_page_config(page_title="LLaMA Career Coach", layout="centered")
st.title("Multilingual Career Coach AI")
st.caption("Powered by LLaMA 3.2, NLLB, and Streamlit")

st.markdown("Enter your career question in any language, or upload your resume for suggestions.")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
if uploaded_file:
    with st.spinner("Analyzing resume..."):
        feedback = analyze_resume(uploaded_file)
    st.subheader("📄 Resume Feedback")
    st.write(feedback)

st.subheader("💬 Ask a Career Question")
user_input = st.text_area("Type your question:", height=150)

if st.button("Get Advice"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            src_lang = detect_lang(user_input)
            translated_input = translate_text(user_input, src_lang, "eng_Latn") if src_lang != "eng_Latn" else user_input
            reply_en = get_llama_response(translated_input)
            final_reply = translate_text(reply_en, "eng_Latn", src_lang) if src_lang != "eng_Latn" else reply_en
        st.success("🧠 Career Advice:")
        st.write(final_reply)
