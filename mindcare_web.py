import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="MindCare", page_icon="🧠", layout="centered")

st.title("🧠 MindCare - Emotional Support App")

try:
    st.write("Welcome to MindCare! Tell us your name and how you feel today 💬")

    user_name = st.text_input("Enter your name:")
    user_input = st.text_area("How are you feeling?")

    if st.button("Analyze Emotion"):
        if not user_name.strip():
            st.warning("Please enter your name first 😊")
        elif not user_input.strip():
            st.warning("Please type something to analyze your mood.")
        else:
            blob = TextBlob(user_input)
            polarity = blob.sentiment.polarity

            if polarity > 0:
                st.success(f"{user_name}, you seem to be feeling positive! Keep it up 🌞")
            elif polarity < 0:
                st.error(f"{user_name}, you seem to be feeling low 😔 Remember, tough times don’t last!")
            else:
                st.info(f"{user_name}, you seem neutral today. Take some time to relax 🧘‍♂")

except Exception as e:
    st.error("⚠ Oops! Something went wrong. Please try again later.")
    st.write("If this keeps happening, the developer might be updating the app.")

# Footer (Your Name)
st.markdown(
    """
    <hr>
    <div style='text-align: center; color: gray; font-size: 13px;'>
        © 2025 MindCare | Created by <b>Vinay Patil</b> 💻
    </div>
    """,
    unsafe_allow_html=True
)
