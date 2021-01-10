try:
    import streamlit as st
except ModuleNotFoundError:
    pass
import json as jn
def build_account_dict(**info):
    return info
jfile_read = open("main.json","r")
jfile_write = open("main.json","w")
age  = st.slider("What is your age?",1,120)
name = st.text_input("What is your username?")
account = build_account_dict(age=age,username=name)
jn.dump(account,jfile_write)
"""
[View now on github](https://github.com/gorenbk/streamlit)
"""