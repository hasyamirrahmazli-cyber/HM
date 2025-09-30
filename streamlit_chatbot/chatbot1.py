import streamlit as st
import pandas as pd
import streamlit as st
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyBpH-3qnM7eQFq-ooTjmYREJG2ce-NdUBg")

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")

# Sidebar for user context
st.sidebar.title("👗 Outfit Preferences")
weather = st.sidebar.selectbox("Weather", ["Sunny", "Rainy", "Cloudy", "Cold", "Hot"])
time_of_day = st.sidebar.radio("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
color_theme = st.sidebar.selectbox("Color Theme", ["Neutral", "Bright", "Dark", "Pastel"])

# Chat interface
def main():
 st.title("Mirrah picks out your fits!")
 st.write("Ask me for outfit suggestions tailored to weather, time, and color theme!")

 if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

 user_input = st.chat_input("What do you feel like wearing?")
 if user_input:
    # Store user input
    st.session_state.chat_history.append(("You", user_input))

    # Sidebar persona selection
 st.sidebar.title("🧑‍🎨 Chatbot Persona")
 persona_choice = st.sidebar.selectbox(
    "Choose your stylist:",
    ["Minimalist", "Maximalist ", "luxurious"]
)

# Define personas
 if persona_choice == "Minimalist":
    persona = """
    You are a minimalist nd who loves fashion but loves keeping it simple.
    Speak in a casual, fun, and supportive tone.
    Use emojis, keep it short, and make outfits exciting but easy to wear.
    """
 elif persona_choice == "Maximalist":
    persona = """
    You are a Maximalist who loves layering and going to the max.
    Speak confidently and excitingly.
    Recommend layering, accesorries and unique styles that still is fashionable
    Keep responses polished but not too long.
    """
 elif persona_choice == "luxurious":
    persona = """
    You are an elegant luxury stylist.
    Keep answers professional and confident.
    Recommed sophiscated outfits with a touch of glam.
    Focus on elegant,rich, timeless outfit choices.
    """
    
    # Build prompt for Gemini
    prompt = f"""
    Suggest a stylish outfit.
    Weather: {weather}
    Time: {time_of_day}
    Color theme: {color_theme}
    User request: {user_input}
    Keep each suggestion short (max 2 sentences).
    Make it easy to compare quickly.
    """
    
    
    response = model.generate_content(prompt)
    bot_reply = response.text
    
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display conversation
 for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

 if __name__ == "__main__":
  main()