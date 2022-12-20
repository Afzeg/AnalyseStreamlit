import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.Views.dataset import open_csv
import squarify
import matplotlib


df = open_csv()[0]
df2 = open_csv()[1]
df2.drop(1310, axis=0, inplace=True)

for column in df.columns:
    df.rename(columns = {column:column.replace(" ", "_")}, inplace = True)


def ranking_country():
    fig = plt.figure(figsize=(10,30))
    ax = sns.barplot(df, x="Ladder_score", y="Country_name", palette="flare")
    plt.title("Classement des pays par leur score du bonheur", fontsize = 15)
    ax.set(xlabel="Score du bonheur", ylabel=None)
    st.pyplot(fig)


def top10_happy():
    fig = plt.figure(figsize=(7,5))
    ax = sns.barplot(data=df.head(10), y="Country_name", x="Ladder_score", hue="Regional_indicator", dodge = False)
    plt.title("Top 10 des pays les plus heureux en 2021")
    ax.set(xlabel="Score du bonheur", ylabel=None)
    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[0].set_text("Europe occidentale")
    i.get_texts()[1].set_text("Amérique du Nord, Australie et Nouvelle-Zélande")
    st.pyplot(fig)


def top10_unhappiness():
    fig = plt.figure(figsize=(7,5))
    ax = sns.barplot(data=df.iloc[-10:], y="Country_name", x="Ladder_score", hue="Regional_indicator", dodge = False)
    plt.title("Top 10 des pays les moins heureux en 2021")
    ax.set(xlabel="Score du bonheur", ylabel=None)
    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[0].set_text('Afrique subsaharienne')
    i.get_texts()[1].set_text("Moyen-Orient et Afrique du Nord")
    i.get_texts()[2].set_text('Amérique latine et Caraïbes')
    i.get_texts()[3].set_text("Sud de l'Asie")
    st.pyplot(fig)


def top_20_years():
    top_20 = df2.groupby("Country name")["Life Ladder"].mean().sort_values(ascending=False).reset_index()[:20].sort_values(by="Life Ladder", ascending=True)
    fig, ax = plt.subplots(1,1, figsize=(10, 7))

    a=1
    for country in top_20["Country name"]:
        mean_country = df2[df2['Country name'] == country].groupby('Country name')['Life Ladder'].mean()
        
        hist = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x='Life Ladder', color="gray")
        
        m = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x=mean_country, color="blue", s=75)
        
        actual = sns.scatterplot(data=df[df['Country_name'] == country], y=a, x='Ladder_score', color="red", s=75)
        a+=1

    #définition des labels de l'axe y, index de top_20 puis les labels 
    ax.set_yticks(top_20.index+1)
    ax.set_yticklabels(top_20['Country name'][::-1], fontdict={'horizontalalignment': 'right'})

    #tracer des lignes horizontales pour chaque y entre xmin et xmax
    ax.hlines(y=top_20.index+1, xmin=6.25, xmax=8.1, color='gray', alpha=0.5, linewidth=0.5, linestyles='-')

    plt.xlabel("Score du bonheur")
    plt.title("Score du bonheur à travers les années", fontsize=15)
    plt.legend(["Anciens scores", "Score moyen", "Score en 2021"])
    st.pyplot(fig)

def bottom_20_years():

    bottom_20 = df2.groupby("Country name")["Life Ladder"].mean().sort_values(ascending=True).reset_index()[:20].sort_values(by="Life Ladder", ascending=True)
    fig, ax = plt.subplots(1,1, figsize=(10, 7))

    a=1
    for country in bottom_20["Country name"]:
        mean_country = df2[df2['Country name'] == country].groupby('Country name')['Life Ladder'].mean()
    
        hist = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x='Life Ladder', color="gray")
    
        m = sns.scatterplot(data=df2[df2['Country name'] == country], y=a, x=mean_country, color="blue", s=75)
    
        actual = sns.scatterplot(data=df[df['Country_name'] == country], y=a, x='Ladder_score', color="red", s=75)
        a+=1

    #définition des labels de l'axe y, index de top_20 puis les labels 
    ax.set_yticks(bottom_20.index+1)
    ax.set_yticklabels(bottom_20['Country name'][::-1], fontdict={'horizontalalignment': 'right'})

    #tracer des lignes horizontales pour chaque y entre xmin et xmax
    ax.hlines(y=bottom_20.index+1, xmin=2, xmax=6.5, color='gray', alpha=0.5, linewidth=0.5, linestyles='-')

    plt.xlabel("Score du bonheur")
    plt.title("Score du bonheur à travers les années", fontsize=15)
    plt.legend(["Anciens scores", "Score moyen", "Score en 2021"])
    st.pyplot(fig)


def happiness_life_GDP():
    fig = plt.figure(figsize=(8,6))
    ax = sns.scatterplot(data=df, x='Healthy_life_expectancy', y='Ladder_score',hue=df['Regional_indicator'] == 'Western Europe', size=df["Logged_GDP_per_capita"]*1000, legend=True, sizes=(5, 500))
    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[1].set_text('Autres régions')
    i.get_texts()[2].set_text("Europe occidentale")
    i.get_texts()[0].set_text('Indicateur régional')
    i.get_texts()[3].set_text('PIB par habitant')
    ax.set(xlabel="Expérance de vie en bonne santé", ylabel="Score du bonheur")
    plt.title("Score du bonheur, expérance de vie en bonne santé et PIB par habitant", fontsize=15)
    st.pyplot(fig)


def happiness_corrup_GDP():
    fig = plt.figure(figsize=(8,6))
    ax = sns.scatterplot(data=df, x='Perceptions_of_corruption', y='Ladder_score',hue=df['Regional_indicator'] == 'Western Europe', size=df["Logged_GDP_per_capita"]*1000, legend=True, sizes=(5, 500))
    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[1].set_text('Autres régions')
    i.get_texts()[2].set_text("Europe occidentale")
    i.get_texts()[0].set_text('Indicateur régional')
    i.get_texts()[3].set_text('PIB par habitant')
    ax.set(xlabel="Perception de la corruption", ylabel="Score du bonheur")
    plt.title("Score de bonheur, perception de la corruption et PIB par habitant", fontsize=15)
    st.pyplot(fig)


def happiness_GDP_freedom():
    fig = plt.figure(figsize=(8,6))
    ax = sns.scatterplot(data=df, x='Freedom_to_make_life_choices', y='Ladder_score',hue=df['Regional_indicator'] == 'Western Europe', size=df["Logged_GDP_per_capita"]*1000, legend=True, sizes=(5, 500))
    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[1].set_text('Autres régions')
    i.get_texts()[2].set_text("Europe occidentale")
    i.get_texts()[0].set_text('Indicateur régional')
    i.get_texts()[3].set_text('PIB par habitant')
    ax.set(xlabel="Liberté des choix de vie", ylabel="Score du bonheur")
    plt.title("Score du bonheur, PIB par habitant et liberté des choix de vie", fontsize=15)
    st.pyplot(fig)

def happiness_social_support():
    fig = plt.figure(figsize=(8,6))
    ax = sns.scatterplot(data=df, x='Social_support', y='Ladder_score',hue=df['Regional_indicator'] == 'Western Europe', size=df["Logged_GDP_per_capita"]*1000, legend=True, sizes=(5, 500))

    i = ax.legend(loc="upper left", bbox_to_anchor=(1,1))
    i.get_texts()[1].set_text('Autres régions')
    i.get_texts()[2].set_text("Europe occidentale")
    i.get_texts()[0].set_text('Indicateur régional')
    i.get_texts()[3].set_text('PIB par habitant')

    ax.set(xlabel="Support social", ylabel="Score du bonheur")
    plt.title("Score du bonheur, PIB par habitant et support social", fontsize=15)
    st.pyplot(fig)
    

def subplot_world():
    df_groupby_region = df.groupby("Regional_indicator")['Ladder_score', 'Logged_GDP_per_capita', 'Social_support', 
    'Healthy_life_expectancy','Freedom_to_make_life_choices', 'Generosity', 'Perceptions_of_corruption'].mean().reset_index().sort_values(by='Ladder_score', ascending=False)

    variable = ['Logged GDP per capita', 'Social support', 'Healthy life expectancy',
    'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']

    for column in df_groupby_region.columns:
        df_groupby_region.rename(columns = {column:column.replace("_", " ")}, inplace = True)
    
    fig, ax = plt.subplots(3, 2, figsize=(12,11), sharey=True)
    a=0
    b=0
    for i in variable:
        if a <= 2:
            sns.scatterplot(df_groupby_region, y=df_groupby_region['Ladder score'],hue="Regional indicator",
            x=i, ax=ax[a,b], legend=False, s=200)
            a += 1
        else:
            b=1
            a=0
            if a <= 2:
                sns.scatterplot(df_groupby_region, y=df_groupby_region['Ladder score'], x=i, ax=ax[a,b], 
                hue="Regional indicator", legend=True, s=200)
                a += 1

    i = ax[0,1].legend(loc='upper left', bbox_to_anchor=(1,1))
    i.get_texts()[0].set_text('Amérique du Nord, Australie et Nouvelle-Zélande')
    i.get_texts()[1].set_text("Europe occidentale")
    i.get_texts()[2].set_text("Europe centrale et orientale")
    i.get_texts()[3].set_text("Amérique latine et Caraïbes")
    i.get_texts()[4].set_text("Asie de l'Est")
    i.get_texts()[5].set_text("Etats indépendants du Commonwealth")
    i.get_texts()[6].set_text("Asie du Sud Est")
    i.get_texts()[7].set_text("Moyen-Orient et Afrique du Nord")
    i.get_texts()[8].set_text("Afrique subsaharienne")
    i.get_texts()[9].set_text("Asie du Sud")

    ax[0,0].set(xlabel="PIB par habitant")
    ax[0,1].set(xlabel="Liberté des choix de vie")
    ax[1,0].set(xlabel="Support social")
    ax[1,1].set(xlabel="Générosité")
    ax[2,0].set(xlabel="Expérance de vie en bonne santé")
    ax[2,1].set(xlabel="Perception de la corruption")
    st.pyplot(fig)


#création des dataset pour chaque région du monde

df_western_europe = df[df["Regional_indicator"] == "Western Europe"]
df_north_america_anz = df[df["Regional_indicator"] == "North America and ANZ"]
df_middle_east_north_africa = df[df["Regional_indicator"] == "Middle East and North Africa"]
df_latin_america_caraibbean = df[df["Regional_indicator"] == "Latin America and Caribbean"]
df_central_eastern_europe = df[df["Regional_indicator"] == "Central and Eastern Europe"]
df_east_asia = df[df["Regional_indicator"] == "East Asia"]
df_southeast_asia = df[df["Regional_indicator"] == "Southeast Asia"]
df_commonwealth = df[df["Regional_indicator"] == "Commonwealth of Independent States"]
df_subsaharan_africa = df[df["Regional_indicator"] == "Sub-Saharan Africa"]
df_south_asia = df[df["Regional_indicator"] == "South Asia"]
    
df_middle_east_north_africa = df_middle_east_north_africa.reset_index()
list_middle_east = []
list_north_africa = []

for i in df_middle_east_north_africa["Country_name"]:
    if (i == "Morocco" or i == "Algeria" or i == "Tunisia"):
        list_north_africa.append(i)
    else:
        list_middle_east.append(i)

#création de la colonne "Region" en fonction des pays 
df_middle_east_north_africa["Region"] = 0
loc = 0
for i in df_middle_east_north_africa["Country_name"]:
    if (i == "Morocco" or i == "Algeria" or i == "Tunisia"):
        df_middle_east_north_africa["Region"].iloc[loc] = "North Africa" 
    else:
        df_middle_east_north_africa["Region"].iloc[loc] = "Middle East" 
    loc += 1   


def pie():
    df_1 = df_middle_east_north_africa.groupby("Region")["Freedom_to_make_life_choices"].mean().reset_index()
    fig = plt.figure(figsize=(7,3))
    plt.pie(df_1["Freedom_to_make_life_choices"], labels = df_1["Region"], autopct='%1.01f%%')
    plt.title("Proportion de la liberté des choix de vie entre le Moyen-Orient et l'Afrique du Nord")
    st.pyplot(fig)


def square1():
    fig = plt.figure(figsize=(6,3))
    squarify.plot(sizes=df_middle_east_north_africa['Freedom_to_make_life_choices'],label=df_middle_east_north_africa['Country_name'],alpha=0.8,pad=1,color=sns.color_palette("Spectral",17))
    plt.title("Liberté des choix de vie au Moyen-Orient et en Afrique du Nord")
    plt.axis("off")
    st.pyplot(fig)


def subplot_southasia():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9,7))

    ax1=sns.barplot(df_southeast_asia.sort_values(by=["Generosity"], ascending=False),
    x="Generosity", y="Country_name", palette="flare", ax=ax1)

    ax2=sns.scatterplot(df_southeast_asia, y="Generosity", x="Logged_GDP_per_capita", hue="Country_name", s=100, ax=ax2)
    ax2.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.axhline(y=0, color="red")

    ax1.set(xlabel="Générosité", ylabel=None)
    ax2.set(xlabel="Générosité", ylabel="PIB par habitant")
    st.pyplot(fig)


def fig_subsaharan():
    fig = plt.figure(figsize=(10,10))
    ax = sns.barplot(df_subsaharan_africa.sort_values(by=["Healthy_life_expectancy"], ascending=False),
    x="Healthy_life_expectancy", y="Country_name", palette="flare")
    ax.set(xlabel="Expérance de vie en bonne santé", ylabel=None)
    plt.title("L'espérance de vie en bonne santé en Afrique Subsaharienne")
    st.pyplot(fig)


def square_corrup_europe():
    fig = plt.figure(figsize=(10,6))
    squarify.plot(sizes=df_western_europe['Perceptions_of_corruption'],label=df_western_europe['Country_name'],alpha=0.8,pad=1,color=sns.color_palette("Spectral",17))
    plt.title("Perception de la corruption en Europe occidentale")
    plt.axis("off")
    st.pyplot(fig)


def corrup_GDP_freedom():
    fig = plt.figure(figsize=(7, 5))
    ax = sns.scatterplot(df, x="Freedom_to_make_life_choices", y="Perceptions_of_corruption",
    size="Logged_GDP_per_capita", sizes=(50, 500))
    ax.legend(loc='upper left', bbox_to_anchor=(1,1), title="PIB par habitant")
    ax.set(xlabel="Liberté des choix de vie", ylabel="Perception de la corruption")
    plt.title("Liberté des choix de vie, perception de la corruption et PIB par habitant")
    st.pyplot(fig)


def GDP_generosity():
    fig = plt.figure(figsize=(7,6))
    ax = sns.scatterplot(df, x="Logged_GDP_per_capita", y="Generosity", hue="Regional_indicator", s=100)
    plt.axhline(y=0, color="red")
    ax.set(xlabel="PIB par habitant", ylabel="Générosité")
    plt.title("PIB par habitant et la générosité")
    
    i = ax.legend(loc='upper left', bbox_to_anchor=(1,1))
    i.get_texts()[1].set_text('Amérique du Nord, Australie et Nouvelle-Zélande')
    i.get_texts()[0].set_text("Europe occidentale")
    i.get_texts()[4].set_text("Europe centrale et orientale")
    i.get_texts()[3].set_text("Amérique latine et Caraïbes")
    i.get_texts()[5].set_text("Asie de l'Est")
    i.get_texts()[7].set_text("Etats indépendants du Commonwealth")
    i.get_texts()[6].set_text("Asie du Sud Est")
    i.get_texts()[2].set_text("Moyen-Orient et Afrique du Nord")
    i.get_texts()[8].set_text("Afrique subsaharienne")
    i.get_texts()[9].set_text("Asie du Sud")
    st.pyplot(fig)


def social_happiness():
    fig = plt.figure(figsize=(7,6))
    ax = sns.scatterplot(df, y="Ladder_score", x="Social_support", hue="Regional_indicator", s=100)
    ax.set(xlabel="Support social", ylabel="Score du bonheur")
    plt.title("Support social et score du bonheur")

    i = ax.legend(loc='upper left', bbox_to_anchor=(1,1))
    i.get_texts()[1].set_text('Amérique du Nord, Australie et Nouvelle-Zélande')
    i.get_texts()[0].set_text("Europe occidentale")
    i.get_texts()[4].set_text("Europe centrale et orientale")
    i.get_texts()[3].set_text("Amérique latine et Caraïbes")
    i.get_texts()[5].set_text("Asie de l'Est")
    i.get_texts()[7].set_text("Etats indépendants du Commonwealth")
    i.get_texts()[6].set_text("Asie du Sud Est")
    i.get_texts()[2].set_text("Moyen-Orient et Afrique du Nord")
    i.get_texts()[8].set_text("Afrique subsaharienne")
    i.get_texts()[9].set_text("Asie du Sud")
    st.pyplot(fig)