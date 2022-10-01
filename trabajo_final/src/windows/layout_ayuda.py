import PySimpleGUI as sg

def build(color_fondo,color_botones) :
    layout=[
        [sg.Text("""
            Las reglas son sencillas: consiste en una cuadrícula de tamaño variable,
            en la cual se esconden pares, ternas, etc. de objetos: en este caso imágenes o 
            nombres de animes. Los jugadores deben ir descubriendo las celdas de a una
            e ir recordando dónde está cada pieza del par, para así reunirlos y sumar puntos.
            El objetivo es lograr reunir la mayor cantidad de pares. Concluye cuando todos los 
            pares de la cuadrícula son formados.

            La puntuación de cada partida ganada se calcula con la siguiente fórmula:

            { [ (cantidad de cartas encontradas ) ^ 3 ] / ( tiempo usado ) } * [ 0.7 ^ (cantidad de ayudas) ]
                        
            De manera que se obtendrá mayor cantidad de puntos cuanto mas grande sea el tablero.
            Sin embargo, si te toma mucho tiempo ganar, o usas muchas ayudas, tu puntaje se 
            verá reducido considerablemente.
        """,background_color=color_fondo,font=("Helvetica",20))],
        [sg.Button("Volver",key="-VOLVER-",font=("Helvetica",20))],
    ]
    return sg.Window("Ayuda",layout,margins=(50,50),background_color=color_fondo,button_color=color_botones)