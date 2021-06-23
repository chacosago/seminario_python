# Enunciado 5:  dado el archivo de registros de jugadas (eventos) de MemPy,
# mostrar un gráfico con los usuarios que más veces jugaron el juego 
# (independientemente del resultado de la partida).
import pandas as pd
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# VSCode:
path_arch = os.path.join(os.getcwd(), "Drive", "Facultad", "Informatica", "Python", "TP", "actividad2_teoria_pyplus", "datos_de_prueba.csv")
df = pd.read_csv(path_arch, encoding='utf-8')
print(df)
print(df.columns)
df.rename(columns={"Usuarie - nick" : "usuario","Nombre de evento" : "nombre_de_evento", "Partida" : "partida"},inplace=True)
print(df.columns)
df = df[df["nombre_de_evento"] == "inicio_partida"]
df = df[["partida", "usuario",  "nombre_de_evento"]]
print(df)
df = df.groupby("usuario")["partida"].count().sort_values(ascending=False).plot(kind="bar")
print(df)
print(type(df))
#plt.show()

# Enunciado adicional: dado alguno de los datasets elegidos para el trabajo integrador,
# mostrar una nube de palabras (con la librería wordcloud) con las palabras elegidas para
# el juego de acuerdo a alguno de los criterios elegidos en su trabajo. Considerar
# utilizar la opción de que se puedan repetir las palabras.

path_arch_animes = os.path.join(os.getcwd(), "Drive", "Facultad", "Informatica", "Python", "TP", "actividad2_teoria_pyplus", "animes.csv")
df = pd.read_csv(path_arch_animes, encoding='utf-8')
print(df)
print(df.describe())
print(df.columns)
print(df.dtypes)
print("-"*50)
df = df[["anime", "rate"]]
print(df.isnull().sum())

media = df["rate"].mean()
print("-"*50+"\nMedia: ",media)

df_procesado = df[df["rate"] > media]
print("-"*50+"\ndf_procesado:\n",df_procesado)

palabras = df_procesado["anime"].to_numpy()
print("-"*50+"\nPalabras: ", palabras)
print("-"*50+"\nTipo palabras: ",type(palabras))

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(1920/100, 1080/100))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off")


text = str(palabras)

# Generate wordcloud
wordcloud = WordCloud(width = 1920, height = 1080, random_state=1, background_color='black',
                         colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(text)
# Plot
plot_cloud(wordcloud)
plt.show()

