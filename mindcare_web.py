import streamlit as st
from PIL import Image
import os

# Set page title, icon, and layout
st.set_page_config(page_title="MindCare by Vinay Patil", page_icon="🧠", layout="centered")

# Display logo if it exists
logo_path = "logo.jpg"  # Change this if your file name is different
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150)
else:
    st.write("🧠 MindCare")  # Fallback if logo not found

# App title
st.title("MindCare by Vinay Patil")

# Input box for user mood
user_input = st.text_input("How are you feeling today?")

# Function to generate smart reply
def get_reply(user_input):
    user_input = user_input.lower()
    
    if "sad" in user_input:
        return "It’s okay to feel sad, Everything will be fine 💙"
    elif "happy" in user_input:
        return "That’s awesome! Keep smiling 😄"
    elif "angry" in user_input:
        return "Take a deep breath, calm down… You’ve got this 💪"
    elif "tired" in user_input:
        return "Please take some rest. Your health matters 🌿"
    elif "anxious" in user_input or "anxiety" in user_input:
        return "I know it feels hard, take a deep breath. You are strong 💚"
    elif "stressed" in user_input or "stress" in user_input:
        return "Try to relax for a while. Small steps help you feel better 🌟"
    elif "lonely" in user_input:
        return "You are never alone, Vinay. I’m always here for you 🤝"
    elif "sleepy" in user_input or "can't sleep" in user_input:
        return "Try to rest your mind and body. Sleep is important 💤"
    elif "frustrated" in user_input:
        return "It’s okay to feel frustrated. Take a short break and calm down 🌿"
    else:
        return "I’m here for you always 🤝"

# Display smart reply if user types something
if user_input:
    st.success(get_reply(user_input))
