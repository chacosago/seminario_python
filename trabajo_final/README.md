# Juego de la Memoria

Desarrollado por Facundo Lede y Facundo Sago

## Requerimientos mínimos

Instalar las librerías, para ello ejecutar en la consola:
```python
pip install -r requirements.txt
```
Si tenés Linux, necesitás instalar TKinter, para ello ejecutar en la terminal:
```python
sudo apt-get install python3-tk
```

## ¿De qué se trata el jugo?

Las reglas son sencillas: consiste en una grilla o cuadrícula de tamaño variable,
en la cual se esconden pares de objetos: pueden ser animales, capitales y países, 
números y sus dobles, etc. Los jugadores deben ir descubriendo las celdas de a una
e ir recordando dónde está cada pieza del par, para así reunirlos y sumar puntos.
El objetivo es lograr reunir la mayor cantidad de pares. El jugador que reúne la
mayor cantidad de pares es el ganador. Concluye cuando todos los pares de la grilla
son formados.

fuente: https://www.bebesymas.com/juegos-y-juguetes/el-memotest-un-clasico

## ¿Cómo correr la aplicación?

Para iniciar el programa se debe ejecutar el archivo mem_py.py que está en la carpeta trabajo.
  Para ello, situarse en dicho directorio haciendo uso la instrucción "cd" y ejecutar el siguiente 
comando:

```python
python3 mem_py.py
```

## Tema del juego
La temática del juego son los animes contenidos en un data set generada a partir de la base de datos 
de Crunchyroll, que se encuentra en:

https://www.kaggle.com/filipefilardi/crunchyroll-anime-ratings

