import os
print(os.getcwd())
print(os.system("ls"))

import streamlit as st
from src.Views import login, home, dataset, analysis, conclusion
from src.router import redirect, get_route
from src.Controllers.auth import open_access, logout
import utils as utl



st.set_page_config(layout="wide", page_title='Rapport du bonheur dans le monde')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = get_route() # récupère la route actuelle

    if open_access() and (route != "/login") and (route != "/signin") and (route != "/home"):
        redirect("/home", reload=True)
    
    if route == "/login":
        if not open_access():
            redirect("/home", reload=True)
        else:
            login.login_page() # on charge la vue login      
    
    elif route == "/home":
        home.home_page()

    elif route == "/dataset":
        dataset.dataset_page()

    elif route == "/analysis":
        analysis.analysis_page()

    elif route =="/conclusion":
        conclusion.conclusion_page()

    elif route =="/logout":
        logout()
        redirect("/home", reload=True)
    
    elif route =="/signin":
        login.signin_page()
    
    else:                   # si la route n'existe pas
        redirect("/home")   # renvoie à home
        home.home_page()

navigation()


