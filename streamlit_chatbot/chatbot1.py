import streamlit as st
import pandas as pd
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyBpH-3qnM7eQFq-ooTjmYREJG2ce-NdUBg")

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")  # safer to use stable model

# Sidebar for user context
st.sidebar.title("👗 Outfit Preferences")
weather = st.sidebar.selectbox("Weather", ["Sunny", "Rainy", "Cloudy", "Cold", "Hot"])
time_of_day = st.sidebar.radio("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
color_theme = st.sidebar.selectbox("Color Theme", ["Neutral", "Bright", "Dark", "Pastel"])

# Sidebar persona selection
st.sidebar.title("🧑‍🎨 Chatbot Persona")
persona_choice = st.sidebar.selectbox(
    "Choose your stylist:",
    ["Minimalist", "Maximalist", "Luxurious"]
)

def main():
    st.title("Mirrah picks out your fits!")
    st.write("Ask me for outfit suggestions tailored to weather, time, and color theme!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("What do you feel like wearing?")
    if user_input:
        st.session_state.chat_history.append(("You", user_input))

        # Define personas
        if persona_choice == "Minimalist":
            persona = """
            You are a minimalist stylist 🌱 who loves keeping it simple.
            Speak casually but clearly. Focus on timeless, easy outfits.
            """
        elif persona_choice == "Maximalist":
            persona = """
            You are a maximalist stylist 🎨 who loves bold layers and accessories.
            Speak with excitement and energy. Recommend colorful, standout outfits.
            """
        elif persona_choice == "Luxurious":
            persona = """
            You are an elegant luxury stylist 💎.
            Keep answers professional and confident.
            Recommend sophisticated outfits with a touch of glam.
            """

        # Build prompt for Gemini
        prompt = f"""
        {persona}

        Suggest 3 outfit ideas.
        Weather: {weather}
        Time: {time_of_day}
        Color theme: {color_theme}
        User request: {user_input}
        Keep each suggestion short (max 2 sentences).
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