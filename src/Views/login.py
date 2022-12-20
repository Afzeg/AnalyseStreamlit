import streamlit as st
from src.Controllers.auth import valid_mail, login, signin, mail_exist, valid_password
from src.router import redirect
from src.Views import home
import base64


                

def login_page():   

    st.subheader("Page de connexion")

    with st.form("my_form"):
        col1, col2 = st.columns(2)
    
    
        with col1:
            st.image("src\Views\component\object\smiley-2979107_1920.jpg")

        with col2:
            mail = st.text_input(label="Identifiant", placeholder="Entrer votre email", help="Votre email doit être au format dupont@mail.fr.")
            password = st.text_input(label="Mot de passe", placeholder="Entrer votre mot de passe", type="password", help="Votre mot de passe doit avoir au moins 8 caractères et doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial (#?!@$%^&*-)")

    
            if st.form_submit_button("Se connecter"): #si appuie sur le bouton passe à la suite
                if valid_mail(mail) and valid_password(password): #si le mail est valide (voir auth) passe à la suite
                    if login(mail, password): #si mail et mdp sont dans la basse de donnée -> se connecte
                        print(login(mail, password))
                        st.text("Vous êtes connecté")
                        redirect("/home", reload=True)
                    else: #si mail et mdp inexistant -> pas de connection
                        print(login(mail, password))
                        st.text("Erreur de connexion")
                else:
                    st.text("Mail invalide") #si le mail est pas valide 
            

def signin_page():

    st.subheader("Page d'inscription")
    with st.form("signup"):

        col1, col2 = st.columns(2)

        with col1:
            st.image("src\Views\component\object\pexels-pixabay-207983.jpg")
        
        with col2:
        
            nom = st.text_input(label="Nom", placeholder="Entrer votre nom")
            prénom = st.text_input(label="Prénom", placeholder="Entrer votre prénom")
            mail = st.text_input(label="Identifiant", placeholder="Entrer votre email", help="Votre email doit être au format dupont@mail.fr.")
            password = st.text_input(label="Mot de passe", placeholder="Entrer votre mot de passe", type="password", help="Votre mot de passe doit avoir au moins 8 caractères et doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial (#?!@$%^&*-)")
            confirm_password = st.text_input(label="Confirmation du mot de passe", placeholder="Entrer votre mot de passe", type="password")

            if st.form_submit_button("S'inscrire"):
                if valid_mail(mail) and (password==confirm_password) and valid_password(password):
                    if mail_exist(mail):
                        signin(mail, password)
                        st.text("Vous êtes inscris, vous pouvez maintenant vous connecter")
                        redirect("/login", reload=True)
                    else:
                        st.text("Mail déjà existant")
                elif not valid_mail(mail):
                    st.text("Mail invalide")
                elif not valid_password(password):
                    st.text("Mot de passe invalide")
                elif not password == valid_password:
                    st.text("Mot de passe incorrect")


