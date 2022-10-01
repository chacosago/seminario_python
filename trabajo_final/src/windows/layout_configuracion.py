import PySimpleGUI as sg 
from src.functions import funcionalidades_tablero as ft

def build(usuario,mensajes) :  
    tipo1 = False
    tipo2 = False
    tipo3 = False
    if usuario["Configuracion"]["Tipo_coincidencias"] == "Imagen/Imagen" :
            tipo1 = True
    if usuario["Configuracion"]["Tipo_coincidencias"] == "Imagen/Palabra" :
            tipo2 = True
    if usuario["Configuracion"]["Tipo_coincidencias"] == "Palabra/Palabra" :
            tipo3 = True


    #[sg.Text("Tamaño del tablero",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",20))],
    layout_personalizar = [[sg.Text("",background_color=usuario["Configuracion"]["Color_fondo"])],
        [sg.Text("Ancho del tablero",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",18)),
            sg.Slider(range=(2, 8), orientation='h',trough_color=usuario["Configuracion"]["Color_botones"],background_color=usuario["Configuracion"]["Color_fondo"], size=(34, 20)
            , default_value=usuario["Configuracion"]["Ancho"],key="-ANCHO-")],
        [sg.Text("Alto del tablero",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",18)),
            sg.Slider(range=(2, 5), orientation='h',trough_color=usuario["Configuracion"]["Color_botones"],background_color=usuario["Configuracion"]["Color_fondo"], size=(34, 20)
            , default_value=usuario["Configuracion"]["Alto"],key="-ALTO-")],
        [sg.Text("Tiempo de juego (seg)",font=("Helvetica",18),background_color=usuario["Configuracion"]["Color_fondo"]),
            sg.Slider(range=(10,180), orientation='h',trough_color=usuario["Configuracion"]["Color_botones"],background_color=usuario["Configuracion"]["Color_fondo"], size=(34, 20)
            , default_value=usuario["Configuracion"]["Tiempo"],key="-TIEMPO-")],
        [sg.Text("\n"*4,background_color=usuario["Configuracion"]["Color_fondo"])],
        [sg.Text("Cartel al ganar:    ",font=("Helvetica",18),background_color=usuario["Configuracion"]["Color_fondo"]),sg.InputCombo(mensajes[0],default_value=usuario["Configuracion"]["Mensaje_ganaste"],enable_events=True,font=("Helvetica",20),
            background_color=usuario["Configuracion"]["Color_botones"],readonly=True, size=(20, 3),key="-WIN-")],   
        [sg.Text("Cartel al perder:   ",font=("Helvetica",18),background_color=usuario["Configuracion"]["Color_fondo"]),sg.InputCombo(mensajes[1],default_value=usuario["Configuracion"]["Mensaje_perdiste"],enable_events=True,font=("Helvetica",20),
            background_color=usuario["Configuracion"]["Color_botones"],readonly=True, size=(20, 3),key="-LOSE-")],
        [sg.Text("\n"*4,background_color=usuario["Configuracion"]["Color_fondo"])],
        [sg.ColorChooserButton("Cambiar color de fondo", size=(36, 1),font=("Helvetica",20),key="-COLORFONDO-")],
        [sg.ColorChooserButton("Cambiar color de botones", size=(36, 1),font=("Helvetica",20),key="-COLORBOTONES-")]                         
    ]    
    layout_niveles = [
            [sg.Radio("Nivel 1",1,enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-NIVEL1-")],
            [sg.Radio("Nivel 2",1,enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-NIVEL2-")],
            [sg.Radio("Nivel 3",1,enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-NIVEL3-")],
            [sg.Text("",font=("Helvetica",19),background_color=usuario["Configuracion"]["Color_fondo"])],
            [sg.Radio("Jugar con ayudas",3,default=usuario["Configuracion"]["Ayuda"],enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-CON-")],
            [sg.Radio("Jugar sin ayudas",3,default=not(usuario["Configuracion"]["Ayuda"]),enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-SIN-")], 
            [sg.InputCombo(ft.calcular_coincidencias(usuario["Configuracion"]["Ancho"]*usuario["Configuracion"]["Alto"]),usuario["Configuracion"]["Coincidencias"],font=("Helvetica",20)
                ,background_color=usuario["Configuracion"]["Color_botones"],key="-COIN-",readonly=True, size=(20, 3))],
            [sg.Text("",background_color=usuario["Configuracion"]["Color_fondo"])],       
            [sg.Text("Tipos de elemenos a encontrar",font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"])],
            [sg.Radio("Imagen / Imagen",2,default=tipo1,enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-TIPO1-")],
            [sg.Radio("Imagen / Palabra",2,default=tipo2,enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-TIPO2-")],
            [sg.Radio("Palabra / Palabra",2,default=tipo3,enable_events=True,font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"],key="-TIPO3-")] 
    ]
    layout = [[sg.Frame("Personalizar tablero",layout_personalizar,vertical_alignment="top",element_justification="right",title_color="black",font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"])
                ,sg.Frame("Modalidad de juego",layout_niveles,vertical_alignment="top",title_color="black",font=("Helvetica",20),background_color=usuario["Configuracion"]["Color_fondo"])],        
                [sg.Text("",background_color=usuario["Configuracion"]["Color_fondo"])],
                [sg.Button("Guardar cambios",font=("Helvetica",20),key="-SAVE-"),sg.Button("Salir",key="-EXIT-",font=("Helvetica",20))]         
                ]
    return sg.Window("Configuración",layout,margins=(100,70),button_color=usuario["Configuracion"]["Color_botones"],background_color=usuario["Configuracion"]["Color_fondo"])
