try:
    import streamlit as st
except ModuleNotFoundError:
    pass
import json as js
def account_dict(**info):
    return info
json_read = open('main.json','r')
json_write = open('main.json','w')
age = st.slider("What is your age?",5,120)
js.dump(age,json_write)