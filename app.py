import streamlit as st
from textblob import TextBlob
import pandas as pd

st.title("AI-Assisted Brand Perception Analytics Dashboard")

st.write("Analyse customer sentiment and brand perception alignment.")

review = st.text_area("Enter a customer review:")

def get_sentiment(review):
    analysis = TextBlob(review)

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity < 0:
        return "Negative"

    else:
        return "Neutral"

if st.button("Analyse Review"):

    sentiment = get_sentiment(review)

    st.subheader("Sentiment Result")
    st.write(sentiment)

    if sentiment == "Negative":
        st.error("Potential brand perception misalignment detected.")

    elif sentiment == "Positive":
        st.success("Customer perception aligns positively with the brand.")
