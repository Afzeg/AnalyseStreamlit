import streamlit as st
import base64
import utils as utl


def conclusion_page():

    st.subheader("Conclusions :")

    st.markdown("""
    Nous avons vu qu'il y a pas mal de distinctions entre les pays heureux et malheureux, du moins aux extrêmes.\n
    Généralement, les populations des pays heureux ont tendance à :
    - être plus riche
    - vivre plus longtemps
    - être en bonne santé
    - être plus libre dans leurs choix
    - avoir beaucoup de support social (famille et amis)
    - vivre dans un pays moins corrompu

    On sait aussi que généralement les plus heureux le reste et les malheureux le deviennent de plus en plus vu que leurs conditions s'amériolent pas. Cependant on a vu quelques cas où
    le score du bonheur montait au cours des années, il y a encore du chemin, mais les pays les moins heureux peuvent briser cette tendance et offrir à leurs habitants une meilleure vie qui entrainera une hausse de leur bonheur.
    """)

def load_conclusion():   

    col1, col2, col3 = st.columns([1, 5, 1])

    with col1:
        st.empty()
    with col2:
        st.image("src/Views/component/object/happiness-2901750_1920.png")
        utl.inject_custom_css()
        utl.navbar_component()
        conclusion_page()
    with col3:
        st.empty()
