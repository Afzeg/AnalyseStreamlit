import streamlit as st
from src.Controllers.auth import login, open_access
from src.router import redirect
from streamlit.components.v1 import html
from src.Views import login

def home_page(): 
    
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image("src\Views\component\object\happiness-2901750_1920.png", use_column_width=True)

    st.subheader("Bienvenu sur le rapport du bonheur dans le monde !")
    st.markdown("""
    Vous trouverez ici une analyse du bonheur dans le monde qui a été faite à partir d'une étude lancé par le Gallup World Poll depuis 2005 sur une majorité des pays du monde.
    Ce projet a été réalisé par Mr Salesse Erwan, en vu de passer la certification pour le titre de Concepteur Développeur d'Application (CDA).

    **Pourquoi ce thème ?**

    En cherchant un sujet pour mon projet, je suis tombé sur une liste de dataset représentant le classement de pays par le bonheur. La première question que je me suis posé en
    voyant ça c'était comment on pouvait définir le bonheur d'un pays. Sur quels critères cette étude se base pour définir si quelqu'un est heureux ou non ?
    Et donc je me suis lancé dans une analyse du rapport du bonheur sur l'année 2021 pour répondre à ma curiosité.
    """)

    if open_access():
        st.markdown("Pour pouvoir accéder à l'analyse, veuillez vous connecter.")
        if st.button("Se connecter"):
            redirect("/login", reload=True)

        if st.button("S'inscrire"):
            redirect("/signin", reload=True)


