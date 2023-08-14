from bardapi import Bard
import streamlit as st
from streamlit_chat import message
import os

# Set the Bard API key using the environment variable
os.environ["_BARD_API_KEY"] = "Zgh_FEkwHdIc9JrbI9Beo32MSUGGzHKIBhgUPP73tMj1TcJn4mKuhOfFzZaUwIL4nDpghw."

# Function to get the response from the Bard API based on the user's input prompt
def response_api(prompt):
    try:
        # Use the Bard API to get the answer based on the user's prompt
        response = Bard().get_answer(str(prompt))
        # Extract the content from the response
        message_content = response['content']
        return message_content
    except Exception as e:
        # Print the full exception traceback for debugging purposes
        import traceback
        traceback.print_exc()
        return "Error: Unable to get response from Bard API."

# Function to get user input using a Streamlit text input widget
def user_input():
    # Create a text input field for the user to enter their prompt
    input_text = st.text_input("Enter your prompt:")
    return input_text

# Initialize session_state to store past inputs and generated outputs
if 'generate' not in st.session_state:
    st.session_state['generate'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get user input
user_text = user_input()

# If the user enters a prompt, get the response using the Bard API and store the input and output in session_state
if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

# Display the chat history (past inputs and generated outputs) in reverse order
if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        # Display past user input with 'is_user=True' to indicate that it's the user's message
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        # Display the generated response
        message(st.session_state["generate"][i], key=str(i))
