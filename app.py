from bardapi import Bard 
import streamlit as st 
from streamlit_chat import message
import os 

os.environ["_BARD_API_KEY"] = "Zgh_FEkwHdIc9JrbI9Beo32MSUGGzHKIBhgUPP73tMj1TcJn4mKuhOfFzZaUwIL4nDpghw."

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
    return st.text_input("enter your prompt:")

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

if st.session_state['generate']:
    for i, (past_text, generated_text) in enumerate(reversed(zip(st.session_state['past'], st.session_state['generate']))):
        message(past_text, is_user=True, key=f"{i}_user")
        message(generated_text, key=str(i))
