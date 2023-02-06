import streamlit as st
from src.Controllers.auth import valid_mail, login, signin, mail_exist, valid_password
from src.router import redirect
from src.Views import home
import base64

def login_page():   

    with st.form("login"):

        st.write("Veuillez vous connecter :")

        mail = st.text_input(label="Identifiant", placeholder="Entrer votre email", help="Votre email doit être au format dupont@mail.fr.")
        password = st.text_input(label="Mot de passe", placeholder="Entrer votre mot de passe", type="password", help="Votre mot de passe doit avoir au moins 8 caractères et doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial (#?!@$%^&*)")

        if st.form_submit_button("Se connecter"): #si appuie sur le bouton passe à la suite
            if valid_mail(mail) and valid_password(password): #si le mail et mdp sont valide (voir auth) passe à la suite
                if login(mail, password): #si mail et mdp sont dans la basse de donnée -> se connecte
                    redirect("/home", reload=True)
                else: #si mail et mdp inexistant -> pas de connection
                    st.text("Erreur de connexion")
            elif not valid_mail:
                st.text("Mail invalide") #si le mail n'est pas valide 
            elif not valid_password:
                st.text("Mot de passe invalide") #si le mdp n'est pas valide

def signin_page():

    with st.form("signup"):

        st.write("Si vous n'avez pas de compte, veuillez remplir le formulaire d'inscription :")

        nom = st.text_input(label="Nom", placeholder="Entrer votre nom")
        prénom = st.text_input(label="Prénom", placeholder="Entrer votre prénom")
        mail = st.text_input(label="Identifiant", placeholder="Entrer votre email", help="Votre email doit être au format dupont@mail.fr.")
        password = st.text_input(label="Mot de passe", placeholder="Entrer votre mot de passe", type="password", help="Votre mot de passe doit avoir au moins 8 caractères et doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial (#?!@$%^&*)")
        confirm_password = st.text_input(label="Confirmation du mot de passe", placeholder="Entrer votre mot de passe", type="password")

        if st.form_submit_button("S'inscrire"): #si appuie sur le bouton
            if valid_mail(mail) and (password==confirm_password) and valid_password(password): #vérification mail et mot de passe
                if mail_exist(mail): #est-ce que le mail existe déjà ?
                    signin(mail, password) #si non ajoute les identifiants à la table users
                    st.text("Vous êtes inscris, vous pouvez maintenant vous connecter")
                else:
                    st.text("Mail déjà existant")
            elif not valid_mail(mail):
                st.text("Mail invalide")
            elif not valid_password(password):
                st.text("Mot de passe invalide")
            elif not password == confirm_password:
                st.text("Mot de passe incorrect")


def load_log():

    col1, col2, col3 = st.columns([1,5,1])
    
    with col1:
        st.empty()
    
    with col2:
        st.image("src/Views/component/object/happiness-2901750_1920.png", use_column_width="always" )
        with st.container():
            login_page()

        with st.container():
            st.empty()

        with st.container():
            signin_page()

    with col3:
        st.empty()



