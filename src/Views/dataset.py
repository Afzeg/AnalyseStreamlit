import streamlit as st
import pandas as pd


def open_csv():
    a = pd.read_csv("src\Views\component\dataset\happiness2021.csv")
    b = pd.read_csv("src\Views\component\dataset\world-happiness-report.csv")
    return [a, b]

def dataset_page():

    df1 = open_csv()[0]
    df2 = open_csv()[1]

    st.header("Présentation des dataset")

    tab1, tab2 = st.tabs(["Classement du bonheur des pays en 2021", "Score du bonheur des années précédentes"])

    with tab1:
        st.subheader("Classement du bonheur des pays en 2021")
        st.dataframe(df1)

        st.markdown("""
        Ce dataset contient le score de bonheur, sur l'année 2021, de 149 pays ainsi que les facteurs utilisés pour exprimer le bonheur. 
        
        Projet de recherche sur plus de 140 pays qui représentent à peu près 95% de la population mondiale adulte (5 milliards). Dans la plupart des pays étudiés, 1000 questionnaires ont été complété par un échantillon représentatif d’individu vivant à travers leur pays. La couverture se fait à travers tout le pays, zones rurales incluses. 

        La base de sondage représente l'ensemble de la population civile, non institutionnalisée, âgée de 15 ans et plus,  du pays.

        Dans les grands pays comme la Chine et la Russie, les sondages se sont faits sur un échantillon de 2000 individus quant aux pays plus petits, cela s’est fait sur un échantillon de 500 à 1000 individus, mais ça reste le même échantillon représentatif pour chaque pays.

        Les enquêtes ont été faites par téléphone ou en face à face suivant la couverture téléphonique du pays.

        Il y a une marge d’erreur dans les résultats de chaque pays qui a été calculé par Gallup autour d’une proportion de 95% du niveau de confidence.

        """)

        expander = st.expander("Voir la description des variables :")
        expander.write("""
        **Nom du pays (Country Name)** : pays étudié

        **Indicateur régionale (Regional indicator)** : région du monde (ANZ étant l'Australie et la Nouvelle-Zélande) à laquelle le pays est rattaché

        **Score du bonheur (Ladder score)** : évaluation de vie pour chaque pays, réponse moyenne à la question sur l'échelle de Cantril (10 à 0, 10 étant la "la meilleure vie possible" et 0 "la pire vie possible") demandant aux personnes d'évaluer la qualité de leur vie actuelle 

        **PIB par habitant (Logged GDP per capita)** : logarithme du PIB par habitant

        **Générosité (Generosity)** : résidu de la régression moyenne nationale des réponses du GWP à la question : "Avec-vous donné de l'argent à une association caritative au cours du dernier mois ?" sur le PIB par habitants

        **Support social (Social support)** : moyenne nationale des réponses binaires (0 ou 1) à la question du Gallup World Poll (GWP) : "Si vous êtes en difficulé, avez-vous des parents ou des amis sur lesquels vous pouvez compter pour vous aider lorsque vous en avez besoin ou non ?"

        **Expérance de vie en bonne santé (Healthy life expectancy)** : nombre moyen d’années en bonne santé

        **Liberté de faire des choix de vie (Freedom to make life choices)** : moyenne nationale des réponses binaires (0 ou 1) à la question du GWP : "Êtes-vous satisfait ou insatisfait de votre liberté de choisir ce que vous faites de votre vie ?"

        **Perception de la corruption (Perceptions of corruption)** : moyenne des réponses binaires à deux questions du GWP :

        - "La corruption est-elle répandue ou non dans l'ensemble du gouvernement ?"

        - "La corruption est-elle répandue ou non dans les entreprises ?

        Si les données sur la corruption gouvernementale sont manquantes, la perception de la corruption des entreprises est prise comme mesure globale de la perception de la corruption

        **Score du bonheur de Dystopia (Ladder score in Dystopia)** : Dystopia est un pays imaginaire qui comptent les personnes les moins heureuses au monde. Le but de cet établissement est d'avoir une référence par rapport à laquelle tous les pays pourront être comparés favorablement (il n'est pas possible pour un pays d'avoir un ladder score inférieur à celui de Dystopia) sur chacun des 6 critères clés. Les scores les plus bas observés pour ces 6 critères caractérisent Dystopia. Étant donné que la vie serait désagréable dans un pays avec les revenus les plus bas du monde, l'espérance de vie la plus faible, la générosité la plus faible, le plus de corruption, le moins de liberté et le moins de soutien social, on appelle donc ce pays "Dystopia" à l'inverse de "Utopia". Son score est fixé à 2.43 en 2021.

        **Explained by : [critères définis précedemment]** ; calcul de la valeur :

        - On récupère la valeur du critère du pays concerné (dans la colonne social support par exemple)

        - On retire à cette valeur celle de Dystopia (le score le moins bon de tout les pays) de ce même critère

        - On multiplie le résultat par le coefficient estimé de ce critère

        **Dystopia + Residual** : les résidus diffèrent pour chaque pays, reflétant la mesure dans laquelle les 6 critères sur ou sous-expliquent les évaluations moyennes de la vie. On combine ces résidus avec l'estimation de l'évaluation de la vie dans Dystopia (2.43).
        
        """)

    with tab2:
        st.subheader("Score du bonheur des années précédentes")
        st.dataframe(df2)

        st.markdown("""
        Ce dataset contient les scores des années précédentes pour chaque pays et pour chaque critère. 
        """)
        
        expander = st.expander("Voir la description des variables :")
        expander.write("""
        **Nom du pays** (Country name) : pays étudié

        **Année (year)** : année de l'étude

        **Score du bonheur (Life Ladder)** : le score de chaque pays par année
        
        """)


        
