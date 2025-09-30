import streamlit as st
import pandas as pd


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Crochet helper🧶")
    
    initialize_session_state()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add simple bot response
        response = f"You said: {prompt}"
        with st.chat_message("assistant"):
            st.write(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

    with st.sidebar:
          st.title("Sidebar") 
   
import streamlit as st
import google.generativeai as genai



# Configure Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("Crochet helper🧶")
    st.write("Tell me what you'd like to crochet for!")
        
        
    if "messages" not in st.session_state:
      st.session_state["messages"] = []

# Show past chat
    for msg in st.session_state["messages"]:
      with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
    if user_input := st.chat_input("Tell me what you want to crochet for!"):
    # Save user message
      st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response (crochet-focused)
    response = model.generate_content(
        f"You are a crochet expert assistant. ONLY give crochet project ideas. "
        f"Do not suggest store-bought gifts. Keep it fun, creative, and simple. "
        f"User request: {user_input}\n\n"
         "Give 2-3 short project ideas (title + 1-line description each)." "Give 2-3 short project ideas (title + 1-line description each)."
    )

    

    # Save AI reply
   
    st.session_state["messages"].append({"role": "assistant", "content": ai_reply})
    

    
if __name__ == "__main__":
    main()
