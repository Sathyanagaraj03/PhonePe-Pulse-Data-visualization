# Importing Libraries
import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
import os
import json

from streamlit_navigation_bar import st_navbar
#from streamlit_option_menu import option_menu
from PIL import Image
from git.repo.base import Repo
st.set_page_config(page_title= "Phonepe Pulse Data Visualization & Exploration",
                   
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   )

mydb = sql.connect(host="localhost",
                   user="root",
                   password="",
                   database= "guvi_db"
                  )
mycursor = mydb.cursor(buffered=True)
styles = {
    "nav": {
        "background-color": "purple",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "white",
        "font-weight": "normal",
        "padding": "14px",
    }
}
page = st_navbar(["Explore Data", "Reports", "Examples", "Community", "Insights"])
st.write(page)