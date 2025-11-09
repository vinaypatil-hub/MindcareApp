import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="MindCare by Vinay Patil 💚", page_icon="💚", layout="centered")

st.markdown("<h1 style='text-align:center; color:green;'>🧠 MindCare by Vinay Patil 💚</h1>", unsafe_allow_html=True)
st.write("Welcome! Type how you feel below and let me respond to your mood 🌱")

user_input = st.text_area("How are you feeling today?")

if st.button("Analyze Mood"):
    if user_input.strip() == "":
        st.warning("Please write something first 💬")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Determine mood based on polarity
        if polarity > 0.5:
            mood = "Very Happy"
            responses = [
                "Wow! You're shining today 😄✨",
                "Keep that big smile, Vinay would be proud of you!",
                "Happiness looks amazing on you 💚"
            ]
        elif 0 < polarity <= 0.5:
            mood = "Happy"
            responses = [
                "That’s great! Keep spreading positivity 🌼",
                "Glad to hear you’re doing well!",
                "Enjoy your good mood and share it 💫"
            ]
        elif -0.3 <= polarity <= 0:
            mood = "Neutral"
            responses = [
                "Hmm, just another day, huh?",
                "Sometimes peace is all we need ☁",
                "Quiet days are important too 🌙"
            ]
        elif -0.6 < polarity < -0.3:
            mood = "Sad"
            responses = [
                "It’s okay to not feel okay 💙",
                "Take a deep breath. Tomorrow will be kinder 🌤",
                "Hey, don’t be hard on yourself — you’re doing your best 🌱"
            ]
        else:
            mood = "Angry"
            responses = [
                "Take it slow. Breathe in... and out 🌿",
                "Let’s calm that fire — you’re stronger than you think 💪",
                "It’s okay to feel angry. Let it out gently 🌸"
            ]

        st.subheader(f"Detected Mood: {mood}")
        st.info(random.choice(responses))
