import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis Tool")
st.write("Enter some text below to analyze its sentiment!")

user_input = st.text_area("Enter text here:")

if st.button("Analyze"):
    if user_input:
        analysis = TextBlob(user_input)
        if analysis.sentiment.polarity > 0:
            st.success(f"Positive Sentiment: {analysis.sentiment.polarity:.2f}")
        elif analysis.sentiment.polarity < 0:
            st.error(f"Negative Sentiment: {analysis.sentiment.polarity:.2f}")
        else:
            st.warning(f"Neutral Sentiment: {analysis.sentiment.polarity:.2f}")
    else:
        st.write("Please enter some text.")
        