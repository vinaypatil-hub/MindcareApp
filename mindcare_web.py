import streamlit as st
from textblob import TextBlob

# ---------------- APP TITLE ----------------
st.set_page_config(page_title="MindCare", page_icon="💚", layout="centered")

st.title("💚 MindCare")
st.subheader("Your friendly mental wellness companion")

# ---------------- ASK NAME ----------------
user_name = st.text_input("What's your name? 🙂", "")

if user_name:
    st.write(f"Hi {user_name}! I'm glad you're here 💚")
else:
    st.write("Please tell me your name so I can chat with you personally 💬")

st.write("Tell me how you're feeling today, and I’ll try to help you feel better 🌿")

# ---------------- USER INPUT ----------------
user_input = st.text_area("What's on your mind?")

# ---------------- FUNCTION TO ANALYZE MOOD ----------------
def analyze_mood(text):
    if not text.strip():
        return "neutral", "Please share something so I can understand how you feel."

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.5:
        return "happy", "That’s awesome! Keep spreading positivity 😊"
    elif sentiment > 0:
        return "calm", "That sounds nice. Stay peaceful and keep going 🌿"
    elif sentiment < -0.5:
        return "sad", "I'm sorry to hear that. It’s okay to feel this way sometimes 💙"
    elif sentiment < 0:
        return "worried", "Try to relax — take a deep breath, you got this 🌼"
    else:
        return "neutral", "Thanks for sharing. Let’s talk more if you’d like 💬"

# ---------------- SMART REPLY GENERATOR ----------------
def smart_reply(mood, name):
    replies = {
        "happy": [f"That's great, {name}! What made your day so good?", f"Keep shining, {name}! 🌟"],
        "calm": [f"That’s nice, {name}. Have you tried meditating lately?", "Peaceful moments are the best 🌿"],
        "sad": [f"{name}, do you want to talk about what’s making you sad?", "Remember, you’re not alone 💙"],
        "worried": [f"{name}, maybe try a small walk or listening to music 🎧", "Want me to suggest some stress-busters?"],
        "neutral": [f"Hmm... {name}, maybe we can do something fun!", "How was your day overall?"]
    }
    return replies.get(mood, [f"I’m here for you, {name} ❤"])[0]

# ---------------- ANALYZE AND REPLY ----------------
if st.button("Analyze My Mood"):
    if not user_name.strip():
        st.warning("Please enter your name first 😊")
    else:
        mood, response = analyze_mood(user_input)
        st.success(f"*Detected mood:* {mood.capitalize()}")
        st.info(response)

        st.write("💭 Smart reply suggestion:")
        st.write(smart_reply(mood, user_name))
