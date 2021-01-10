import streamlit as st
import json as js
def account_dict(**info):
    return info
with open('main.json','r') as json_read:
    account = js.load(json_read)
age = st.slider("What is your age?",5,120,account['age'])
username = st.text_input("What is your username?",account['name'])
with open('main.json','w') as json_write:
    account = account_dict(age=age,
    name=username)
    js.dump(account,json_write)
file_read = open('main.py','r')