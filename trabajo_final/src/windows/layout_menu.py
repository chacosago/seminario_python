import PySimpleGUI as sg 

def build (usuario) :
    bienvenida = "Bienvenida"
    if usuario["Género"] == "Hombre" :
        bienvenida = "Bienvenido"
    elif usuario["Género"] == "Otro":
        bienvenida = "Bienvenide" 
    layout = [[sg.Text(bienvenida+" "+usuario["Nick"],background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue")],
        [sg.Button("Jugar",key="-PLAY-",font=("Helvetica", 20),size=(15,1),border_width=5)],
        [sg.Button("Configuración",key="-CONFIG-",font=("Helvetica", 20),size=(15,1),border_width=5)],
        [sg.Button("Puntajes",key="-PUNTAJES-",font=("Helvetica", 20),size=(15,1),border_width=5)],
        [sg.Button("Estadísticas",key="-STATS-",font=("Helvetica", 20),size=(15,1),border_width=5)],
        [sg.Button("Ayuda",key="-HELPMENU-",font=("Helvetica", 20),size=(15,1),border_width=5)],
        [sg.Button("Cerrar Sesión",key="-SALIR-",font=("Helvetica", 20),size=(15,1),border_width=5)]
    ]

    return sg.Window("Menu principal",layout,margins=(100,60),background_color=usuario["Configuracion"]["Color_fondo"]
            ,button_color=usuario["Configuracion"]["Color_botones"],finalize=True)

