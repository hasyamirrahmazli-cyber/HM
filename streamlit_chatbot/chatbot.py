import streamlit as st
import google.generativeai as genai

# Configure Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# Initialize session state
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

# Function to get response from Gemini
def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# Main Streamlit app
def main():
    st.title("🧶 Crochet Helper")
    st.write("Tell me what you'd like to crochet for!")

    initialize_session_state()

    # Display previous chat messages
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    if user_input := st.chat_input("Tell me what you want to crochet for!"):
        # Show user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Save user message
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Generate AI response
        prompt = (
            f"You are a crochet expert assistant. ONLY give crochet project ideas. "
            f"Do not suggest store-bought gifts. Keep it fun, creative, and simple. "
            f"User request: {user_input}\n\n"
            "Give 2-3 short project ideas (title + 1-line description each)."
        )
        ai_reply = get_gemini_response(prompt)

        # Show AI response
        with st.chat_message("assistant"):
            st.markdown(ai_reply)

        # Save AI message
        st.session_state["messages"].append({"role": "assistant", "content": ai_reply})

    # Optional: Sidebar
    with st.sidebar:
        st.title("About")
        st.markdown("This is a crochet idea generator powered by Gemini AI!")

# Run the app
if __name__ == "__main__":
    main()



        
  

    