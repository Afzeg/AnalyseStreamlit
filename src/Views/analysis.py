import streamlit as st
import pandas as pd
from src.Views.component import figure
from src.Views.dataset import open_csv
import matplotlib.pyplot as plt
import seaborn as sns
import utils as utl


df = open_csv()[0]
df2 = open_csv()[1]
df2.drop(1310, axis=0, inplace=True)



st.set_option('deprecation.showPyplotGlobalUse', False)


def page1():
    st.title("**Quels sont les pays les plus et les moins heureux du monde ?**")

    #figure.ranking_country()
    
    figure.top10_happy()
    st.markdown("On voit que les pays les plus heureux du monde sont en Europe occidentale (9 sur les 10 premiers). Et la majorité de ces pays du top 10 sont du Nord de l'Europe.")
    
    figure.top10_unhappiness()
    st.markdown("""
    Dans les pays les moins heureux du monde, on voit que 7 d'entre eux sont d'Afrique subsaharienne. L'Afghanistan arrive dernier, avec un score de 2.523.\n
    Dans les deux graphes suivant, on a fait un top 20 et un bottom 20 par rapport à la moyenne des notes reçus par ces pays depuis 2005.
    On pourra suivre l'évolution ou la régression de ces pays au cours des années passées.
    """)

    # création d'un input interactif pour changer l'année dans le graphe
    # création de la liste des années présentes dans le dataset
    list_year=[]

    for years in df2["year"]:
        list_year.append(years)
    list_year = sorted(set(list_year))

    with st.container():

        # création du slider pour choisir l'année
        year = st.select_slider("", options = list_year + [2021])
        
        st.write("""
        Les points gris réprésentent les scores des autres années.\n
        Les points bleus réprésentent la moyenne de tout les scores reçus pour chaque pays.\n
        Les points rouges représentes l'année choisie ci-dessus.\n
        Il y a des valeurs manquantes pour certains pays sur certaines années. L'étude n'a pas été réalisé dans ce pays cette année là.
        """)
    
        # graphe
        top_20 = df2.groupby("Country name")["Life Ladder"].mean().sort_values(ascending=False).reset_index()[:20].sort_values(by="Life Ladder", ascending=True)
        fig, ax = plt.subplots(1,1, figsize=(6, 4))

        a=1
        for country in top_20["Country name"]:
            mean_country = df2[df2['Country name'] == country].groupby('Country name')['Life Ladder'].mean()
    
            hist = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x='Life Ladder', color="gray") #place un point gris pour chaque année
    
            m = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x=mean_country, color="blue", s=75) #point bleu pour la moyenne de tout les scores

            if year == 2021:
                actual = sns.scatterplot(data=df[df['Country name'] == country], y=a, x='Ladder score', color="red", s=75) #si année=2021, prend la donnée de le 1er dataset
            else:    
                actual = sns.scatterplot(data=df2[(df2['Country name'] == country) & (df2['year']==year)], y=a, x='Life Ladder', color="red", s=75) #sinon prend la donnée de l'année dans le 2ème dataset
            a+=1

        #définition des labels de l'axe y, index de top_20 puis les labels 
        ax.set_yticks(top_20.index+1)
        ax.set_yticklabels(top_20['Country name'][::-1], fontdict={'horizontalalignment': 'right'})

        #tracer des lignes horizontales pour chaque y entre xmin et xmax
        ax.hlines(y=top_20.index+1, xmin=6.25, xmax=8.1, color='gray', alpha=0.5, linewidth=0.5, linestyles='-')

        plt.xlabel("Score du bonheur")
        plt.title("Les pays les plus heureux en "+ str(year), fontsize=15)
        st.pyplot(fig)
    

    
        bottom_20 = df2.groupby("Country name")["Life Ladder"].mean().sort_values(ascending=True).reset_index()[:20].sort_values(by="Life Ladder", ascending=True)
        fig, ax = plt.subplots(1,1, figsize=(6, 4))

        a=1
        for country in bottom_20["Country name"]:
            mean_country = df2[df2['Country name'] == country].groupby('Country name')['Life Ladder'].mean()

            hist = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x='Life Ladder', color="gray")

            m = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x=mean_country, color="blue", s=75)

            if year == 2021:
                actual = sns.scatterplot(data=df[df['Country name'] == country], y=a, x='Ladder score', color="red", s=75)
            else:
                actual = sns.scatterplot(data=df2[(df2['Country name'] == country) & (df2['year']==year)], y=a, x='Life Ladder', color="red", s=75)
            a+=1

        #définition des labels de l'axe y, index de top_20 puis les labels 
        ax.set_yticks(bottom_20.index+1)
        ax.set_yticklabels(bottom_20['Country name'][0:], fontdict={'horizontalalignment': 'right'})

        #tracer des lignes horizontales pour chaque y entre xmin et xmax
        ax.hlines(y=bottom_20.index+1, xmin=2, xmax=6.5, color='gray', alpha=0.5, linewidth=0.5, linestyles='-')

        plt.xlabel("Score du bonheur")
        plt.title("Les pays les moins heureux en " + str(year), fontsize=15)
        st.pyplot(fig)

    st.markdown("""
    On peut voir que sur toutes ces années, l'Europe Occidentale occupe une grande partie de ce top 20 et continue d'avoir des scores de plus en plus élevé comme c'est le cas de l'Allemagne.\n
    Au contraire, dans les 20 pays les plus malheureux on retrouve une majorité de pays d'Afrique. On peut voir que certains de ces pays arrivent à améliorer leur score, comme le Bénin, mais d'autre régressent comme c'est le cas de l'Afghanistan.\n
    On va observer les différences entre l'Europe Occidentale et le reste du monde. Qu'est-ce qui fait que l'Europe soit omniprésente dans le haut de ce classement ?
    """)

def page2():
    st.title("**Quelles sont les différences entre l'Europe occidentale et le reste du monde ?**")

    option = st.selectbox(
        "Pour répondre à cette problématique, on va analyser chacun des critères par rapport au score du bonheur et ressortir la région 'Europe Occidentale'. Pour celà veuillez choisir un critère :",
        ('PIB par habitant', 'Perception de la corruption', 'Liberté de faire des choix', 'Support social'))

    if option == 'PIB par habitant':


        figure.happiness_life_GDP()
        st.markdown("""
        On voit que les habitants des pays les plus heureux sont ceux avec un PIB haut et une longue espérance de vie en bonne santé. Et c'est aussi en majorité des pays d'Europe occidentale.

        Les pays les moins heureux sont aussi ceux avec l'espérance de vie en bonne santé la plus courte, on pourra regarder plus en détail de quelle(s) région(s) il s'agit.
        """)

    elif option == 'Perception de la corruption':

        figure.happiness_corrup_GDP()
        st.markdown("""
        Dans les pays où les habitants ont une grosse perception de corruption, on retrouve de tout ; des petits et gros PIB et des pays plus ou moins heureux. 

        Pour les pays les moins corrompus, on retrouve encore en majorité l'Europe occidentale et si on fouille, on retrouve en grand nombre les pays nordiques comme la Finlande, l'Irlande, le Danemark, etc. 

        On notera aussi qu'une moitié de cette région a une haute perception de corruption.
        """)

    elif option == 'Liberté de faire des choix':

        figure.happiness_GDP_freedom()
        st.markdown("""
        Pour ce qui est de la liberté, on retrouve encore en grand nombre les pays d'Europe occidentale faisant parti des pays avec le plus liberté de choix. Tout les pays de cette région ne sont pas dans le haut du classement. 
        Dans les pays avec le moins de liberté, on a un peu de tout. On voit tout de même que les pays avec un PIB par habitant faible n'ont pas autant de liberté que ceux en ayant un haut.
        """)

    else:
        figure.happiness_social_support()
        st.markdown("""
        Ici on retrouve à nouveau l'Europe Occidentale en haut du classement, le score minimum du support social pour cette région est de 0.8. Soit 80% des sondés ont répondu "oui" à la question : 
        "Si vous êtes en difficulé, avez-vous des parents ou des amis sur lesquels vous pouvez compter pour vous aider lorsque vous en avez besoin ou non ?" 
        """)


def page3():
    st.title("**Que se passe-t-il dans le reste du monde ?**")


    figure.subplot_world()
    st.markdown("""
    On distingue 3 groupes assez distincts :

    - Amérique du Nord, Australie, Nouvelle Zélande et l'Europe de l'Ouest 

    - L'Afrique subsaharienne et le Sud de l'Asie

    - Les régions restantes

    On remarque quelques points isolés du reste :

    - l'espérance de vie en Afrique subsaharienne

    - la liberté en Afrique du Nord, au Moyen-Orient et au Sud-Est de l'Asie

    - la générosité au Sud-Est de l'Asie

    - la perception de corruption en Europe de l'Ouest, on a vu qu'il y avait beaucoup de différences au sein de cette région

    On va regarder plus en détails ces points là.
    """)

    st.subheader("**La liberté des choix en Afrique du Nord et au Moyen-Orient.**")

    figure.pie()
    st.markdown("""
    La différence n'est très grande mais les habitants du Moyen-Orient semble être plus libre dans leurs choix de vie.
    """)

    figure.square1()
    st.markdown("""
    La population du Liban et de l'Algérie sont insatisfaits dans leur liberté de choix de vie, une personne sur deux, des sondés, a voté non à la question  "Êtes-vous satisfait ou insatisfait de votre liberté de choisir ce que vous faites de votre vie ?".

    On a vu sur la vue globale que cette région avait une haute perception de la corruption au en son sein, on pourrait se demander s'il y a un lien entre la liberté et la corruption. On répondra à cette question dans le prochain chapitre.
    """)     

    st.subheader("**La générosité au Sud-Est de l'Asie.**")

    figure.subplot_southasia()
    st.markdown("""
    La générosité de l'Indonésie et de Myanmar (Birmanie) est très haute, 75% des sondés ont fait un acte généreux le mois précédent cette étude. La Thailande a aussi un grosse score de 0.3. Les autres pays se trouvent dans une fourchette de -0.1 - 0.13 qui montre qu'à peu près la moitié des sondés n'ont pas fait d'acte de générosité au cours du dernier mois.

    En comparant les scores précédents avec le PIB par habitant, on remarque que les populations les plus généreuses de cette région sont celles qui ont le moins d'argent. Notamment Myanmar qui a un PIB par habitant autour de 8.5.

    On regardera un peu plus loin si cette caractéristique est présente dans les autres régions du monde.
    """)

    st.subheader("**Le nombre d'années moyen en bonne santé en Afrique subsaharienne**")

    figure.fig_subsaharan()
    st.markdown("""
    Comme on a pu le voir plus haut, l'Afrique subsaharienne a l'expérance de vie en bonne santé la plus basse du monde. Avec le Chad qui a une espérance de vie moyenne de 48.5 ans, qui est la valeur la plus basse tout pays confondu de cette étude. 
    L'Île Maurice est le pays avec l'espérance vie la plus haute de cette région, soit 66.7 ans en moyenne en bonne santé.
    """)

    st.subheader("**La corruption au sein de l'Europe occidentale.**")

    figure.square_corrup_europe()
    st.markdown("""
    Comme on a pu voir dans la première analyse, il existe de grandes disparités au sujet de la perception de corruption au sein de l'Europe occidentale. En regardant plus en détail, on peut voir que les populations des pays nordiques estiment avoir très peu de corruption chez eux. 
    Ce qui n'est pas le cas pour beaucoup d'autre pays comme l'Italie, le Portugal, la Grêce ou encore Chypre, où plus de 80% des sondés disent qu'il y a de la corruption au sein de leur pays.

    On a vu sur quelques graphiques, qu'une corrélation semble se faire entre certains critères, on va étudier ça.
    """)
    
    
def page4():
    st.title("**Y a t-il un lien entre ces critères ?**")

    st.subheader("**La pauvreté d'un pays augmente-t-elle la corruption en son sein ? La liberté est-t-elle limitée par la corruption ?**")

    figure.corrup_GDP_freedom()
    st.markdown("""
    - La première chose qu'on remarque c'est que moins il y a de liberté, plus ça tend vers une haute corruption dans le pays.

    - Deuxième chose, les pays avec le moins de corruption font partis de ceux avec un PIB par habitant élevé.

    - Troisième chose, le facteur PIB par habitant ne change pas la perception de corruption de ce pays, on retrouve de tout dans le haut du graphique.
    """)

    st.subheader("**La pauvreté empêche-t-elle les personnes d'être généreuse ?**")

    figure.GDP_generosity()
    st.markdown("""
    On a vu plus tôt qu'au Sud Est de l'Asie les populations sont très généreuses alors qu'elles ne font pas parties des plus aisées. 

    En suivant le graphe si dessus, on remarque qu'une majorité des pays de cette étude se situent entre 0 et -0.2. 
    Ce qui signifie qu'un peu plus de la moitié des habitants de ces pays n'ont pas fait d'acte de générosité sur le mois précédent cette étude.

    En remarque aussi que les populations des pays pauvres sont en général plus généreuses que les plus riches.
    """)

    st.subheader("**Le support social est toujours présent dans les pays moins heureux ?**")

    figure.social_happiness()
    st.markdown("""
    On peut voir une tendance, plus le score de support social est haut plus le score du bonheur augmente. Ce qui montre que dans les pays moins heureux, la présence de proches est de plus en plus faible
    """)

def tab():

    tab1, tab2, tab3, tab4 = st.tabs(["Les plus ou moins heureux", "L'Europe contre le monde",
"Le reste du monde", "Le lien entre tout ces critères"])

    with tab1:
        page1()
    
    with tab2:
        page2()
    
    with tab3:
        page3()
    
    with tab4:
        page4()

"""
def summary():
    summary = st.sidebar.radio("Sommaire", ("Quels sont les pays les plus et les moins heureux du monde ?", "Quelles sont les différences entre l'Europe occidentale et le reste du monde ?", 
    "Que se passe-t-il dans le reste du monde ?", "Existe-t-il des liens entre ces critères ?"))

    if summary == "Quels sont les pays les plus et les moins heureux du monde ?":
        analysis_page(1)

    elif summary == "Quelles sont les différences entre l'Europe occidentale et le reste du monde ?":
        analysis_page(2)

    elif summary == "Que se passe-t-il dans le reste du monde ?":
        analysis_page(3)

    else:
        analysis_page(4)
"""  


def load_analysis():   

    col1, col2, col3 = st.columns([1, 5, 1])

    with col1:
        st.empty()
    with col2:
        st.image("src/Views/component/object/happiness-2901750_1920.png")
        utl.inject_custom_css()
        utl.navbar_component()
        tab()
    with col3:
        st.empty()

    
