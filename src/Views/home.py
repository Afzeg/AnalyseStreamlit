import streamlit as st
from src.Controllers.auth import login, open_access
from src.router import redirect
from streamlit.components.v1 import html
from src.Views import login
import utils as utl



def home_page(): 


    st.title("Bienvenu sur le rapport du bonheur dans le monde !")
    
    st.subheader("Qui suis-je ?")
    st.markdown("""
    Je m'appelle **Erwan Salesse**, j'ai 26 ans. J'ai passé 3 années à l'université de La Garde en Physique-Chimie suivi de 5 ans de travail dans la logistique.
    
    J'ai créé ce site pour cloturer ma formation de **Data Analyst** effectuée avec l'organisme de formation **DATAROCKSTARS** et valider ma certification de **concepteur développeur 
    d'application**. Je me suis lancé dans cette formation afin d'acquérir de nouvelles compétences dans un domaine en plein expansion.
    """)

    st.subheader("Quel est ce site ?")
    st.markdown("""
    Ici vous retrouverez une analyse de classement du bonheur des pays pour l'année 2021. Ce classement a été réalisé à travers l'étude faite par le **Gallup World Poll**. 
    
    Projet de recherche sur plus de 140 pays qui représentent à peu près 95% de la population mondiale adulte (5 milliards). Dans la plupart des pays étudiés, 
    1000 questionnaires ont été complété par un échantillon représentatif d’individu vivant à travers leur pays. La couverture se fait à travers tout le pays, 
    zones rurales incluses. 
    
    La base de sondage représente l'ensemble de la population civile, non institutionnalisée, âgée de 15 ans et plus,  du pays.

    Dans les grands pays comme la Chine et la Russie, les sondages se sont faits sur un échantillon de 2000 individus quant aux pays plus petits, cela s’est fait sur un échantillon de 500 à 1000 individus, mais ça reste le même échantillon représentatif pour chaque pays.

    Les enquêtes ont été faites par téléphone ou en face à face suivant la couverture téléphonique du pays.
    """)

    st.subheader("Pourquoi ce thème ?")
    st.markdown("""
    En cherchant un sujet pour mon projet, je suis tombé sur une liste de dataset représentant le classement de pays par le bonheur. 
    
    La première question que je me suis posé en voyant ça c'était comment on pouvait définir le bonheur d'un pays. Sur quels critères cette étude se base pour définir si 
    quelqu'un est heureux ou non ?
    
    Et donc je me suis lancé dans une analyse du rapport du bonheur sur l'année 2021 pour répondre à ma curiosité.
    """)


    #if open_access():
    #    st.markdown("Pour pouvoir accéder à l'analyse, veuillez vous connecter.")
    #    if st.button("Se connecter"):
    #        redirect("/login", reload=True)

    #    if st.button("S'inscrire"):
    #        redirect("/signin", reload=True)


def load_home():
    col1, col2, col3 = st.columns([1,5,1])

    with col1:
        st.empty()
    with col2:
        st.image("src/Views/component/object/happiness-2901750_1920.png")
        utl.inject_custom_css()
        utl.navbar_component()
        home_page()
    with col3:
        st.empty()

