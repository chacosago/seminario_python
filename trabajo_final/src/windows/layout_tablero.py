import PySimpleGUI as sg 
import os 

def build(usuario) :
    """Esta funcion construte el tablero y el resto de elementos a mostrar"""
    
    path_file = os.path.join(os.getcwd(), "src", "files", "" )
    rango = [0,usuario["Configuracion"]["Ancho"]]

    def get_layout(rango,largo) :
        """Esta funcion genera los botones de cada columna"""
        layout = [sg.Button("",size=(20,7),image_size=(160,160),auto_size_button=False,image_subsample=4,
                    image_filename=path_file+"default.png",disabled=True,key=str(x),button_color=usuario["Configuracion"]["Color_fondo"],
                    font=("Helvetica", 15))
                     for x in range(rango[0],rango[1])]

        rango[0] = rango[1]
        rango[1] += largo
        return layout     
    
    # Genero layout-botones de las filas usando las columnas, y el resto de elemontos a mostrar
    
    layout_cartas=[get_layout(rango,usuario["Configuracion"]["Ancho"]) for x in range(usuario["Configuracion"]["Alto"])]
    
    layout_info=[
        [sg.Text(f"Jugador: {usuario['Nick']}",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue")],
        [sg.Text(f"Tiempo transcurrido: ",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue"),
            sg.Text("00:00",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue", key="-TIMER-")],
        [sg.Text(f"Avance: 0 %",size=(15,1),background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue", key="-AVANCE-")],
        [sg.Text(f"Coincidencias: {usuario['Configuracion']['Coincidencias'][0]}",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue")],
        [sg.Text(f"Tamaño del tablero: {usuario['Configuracion']['Alto']}x{usuario['Configuracion']['Ancho']}",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue")],
        [sg.Text(f"Tiempo total: {int(usuario['Configuracion']['Tiempo'] // 60)}:{int(usuario['Configuracion']['Tiempo'] % 60)} minutos",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue")],
        [sg.Text(f"Tipo de elementos: {usuario['Configuracion']['Tipo_coincidencias']}",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue")],
        [sg.Text(f"Penalización por ayudas:",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue"),
            sg.Text("-0 %",size=(20,1),background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue", key="-DESCUENTO-")],
        [sg.Text(f"Géneros de anime:",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue"),
            sg.Text("",size=(20,1),background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue", key="-GENERO-")],
        [sg.Text(f"Nivel:",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue"),
            sg.Text("",size=(20,1),background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",15),text_color="blue", key="-NIVEL-")]               
    ]
    layout = [[sg.Frame("",layout_cartas,background_color=usuario["Configuracion"]["Color_fondo"]),sg.Frame("",layout_info,background_color=usuario["Configuracion"]["Color_fondo"])],
        [sg.Text("",background_color=usuario["Configuracion"]["Color_fondo"])],
        [sg.Button("Comenzar",font=("Helvetica",20),key="-START-"),
        sg.Button("Reiniciar partida",disabled=True,font=("Helvetica",20),key="-RESET-"),
        sg.Button("Abandonar partida",font=("Helvetica",20),key="-EXIT-")
        ,sg.Button("Ayuda",font=("Helvetica",20),disabled=True,key="-AYUDAR-"),
        sg.Text("Descargando imágenes...",background_color=usuario["Configuracion"]["Color_fondo"],font=("Helvetica",25),text_color="blue",key="-DESCARGA-")]
        ]
    if usuario["Configuracion"]["Alto"] > 4 :
        ventana = sg.Window("Memotest",layout,background_color=usuario["Configuracion"]["Color_fondo"]
                    ,button_color=usuario["Configuracion"]["Color_botones"],margins=(50,50),location=(0,0)).finalize()
    else :
        ventana = sg.Window("Memotest",layout,background_color=usuario["Configuracion"]["Color_fondo"]
                    ,button_color=usuario["Configuracion"]["Color_botones"],margins=(50,50)).finalize()
    return ventana