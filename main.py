#import os
#print(os.getcwd())
#print(os.system("ls"))

import streamlit as st
from src.Views import login, home, dataset, analysis, conclusion
from src.router import redirect, get_route
from src.Controllers.auth import open_access, logout
import utils as utl

st.set_page_config(layout="wide", page_title='Rapport du bonheur dans le monde')
st.set_option('deprecation.showPyplotGlobalUse', False)


def navigation():
    route = get_route() # récupère la route actuelle

    if open_access() and (route != "/login"): 
        redirect("/login", reload=True)
    
    if route == "/login":
        login.load_log() # on charge la vue login      
    
    elif route == "/home":
        home.load_home()

    elif route == "/dataset":
        dataset.load_dataset()

    elif route == "/analysis":
        analysis.load_analysis()

    elif route =="/conclusion":
        conclusion.load_conclusion()

    elif route =="/logout":
        logout()
        redirect("/login", reload=True)
    
    else:                   # si la route n'existe pas
        redirect("/home")   # renvoie à home
        home.home_page()

navigation()


