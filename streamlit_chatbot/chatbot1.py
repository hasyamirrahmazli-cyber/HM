import streamlit as st
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyBpH-3qnM7eQFq-ooTjmYREJG2ce-NdUBg")

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")

def main():
    # 🎀 Main title
    st.title(" Mirrah Picks Out Your Fits! ")
    st.write("Ask me for outfit suggestions tailored to **weather, time, and color theme** 👗")

    # Sidebar outfit preferences
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

    # Define personas
    if persona_choice == "Minimalist":
        persona = """
        You are a minimalist stylist who loves fashion but keeps it simple.
        Speak casually and supportively, use emojis, and suggest easy, stylish outfits.
        """
    elif persona_choice == "Maximalist":
        persona = """
        You are a maximalist stylist who loves layering and bold fashion.
        Speak confidently and excitingly, recommend accessories and creative combos.
        """
    else:  # Luxurious
        persona = """
        You are an elegant luxury stylist.
        Speak professionally and confidently, suggest timeless and glamorous outfits.
        """

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat input
    user_input = st.chat_input("What do you feel like wearing?")
    if user_input:
        st.session_state.chat_history.append(("You", user_input))

        # Build prompt for Gemini
        prompt = f"""
        {persona}
        Suggest a stylish outfit.
        Weather: {weather}
        Time: {time_of_day}
        Color theme: {color_theme}
        User request: {user_input}
        Keep each suggestion short (max 2 sentences).
        """

        # Gemini response
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