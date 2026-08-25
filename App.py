import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "😊 Positive"
    elif compound <= -0.05:
        sentiment = "😢 Negative"
    else:
        sentiment = "😐 Neutral"

    return sentiment, scores


# ⚫ dark grey Background
st.markdown("""
<style>
.stApp {
    background-color: #121212;
}
</style>
""", unsafe_allow_html=True)


# Website
st.title("🤖 SENTIMENT AI")

text = st.text_input("Enter a sentence:")

if st.button("Analyze Sentiment"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")

    else:
        sentiment, scores = analyze_sentiment(text)

        st.subheader("Result")

        st.write("Text:", text)
        st.write("Sentiment:", sentiment)
        st.write("Compound Score:", scores["compound"])
