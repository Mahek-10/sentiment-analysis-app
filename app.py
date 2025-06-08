import streamlit as st
from textblob import TextBlob

st.title("Simple Sentiment Analysis")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip():
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            st.success("Positive Sentiment 😊")
        elif polarity < 0:
            st.error("Negative Sentiment 😞")
        else:
            st.info("Neutral Sentiment 😐")
    else:
        st.warning("Please enter some text.")
