import os
import pandas as pd
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


st.set_page_config(
    page_title="Panada AI  Analysis",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

system_openai_api_key = os.environ.get('OPENAI_API_KEY')
system_openai_api_key = st.text_input(":key: Step 1: Enter your OpenAI Key :", value=system_openai_api_key)
os.environ["OPENAI_API_KEY"] = system_openai_api_key


llm = OpenAI(api_token=system_openai_api_key)

# enforce_privacy — when set to True, PandasAI only sends the column names.
pandas_ai = PandasAI(llm, enforce_privacy = True)
st.caption("Step 2 : Input the Sample Insurance CSV file")
if st.button("Import"):
    df = pd.read_csv('insurance.csv')
    st.write(df)


