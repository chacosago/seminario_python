import PySimpleGUI as sg
import os

path_images = os.path.join(os.getcwd(), "src", "images", "" )

def build (color_fondo,color_botones,data,header_list,criterios) :  

    niveles = ["Nivel 1","Nivel 2","Nivel 3","Todas las partidas"]
    layout =[                 
        [
            [sg.Frame(
                niveles[i],
                [[sg.Table(values=data[i],
                    key=str(i),
                    font=("Helvetica",12),
                    selected_row_colors=("white",color_botones),
                    background_color=color_fondo,
                    headings=header_list,
                    max_col_width=6,
                    auto_size_columns=False,
                    justification='center',
                    num_rows=min(len(data[i]), 5))
                ]],
                font=("Helvetica",20),
                background_color=color_fondo
            )] 
        ] for i in range(len(data))
    ]
    layout_2 = [
        [sg.Text("Filtrar por jugador: ",background_color=color_fondo,font=("Helvetica",15)),
        sg.InputText("",key="-INPUT-",background_color=color_fondo,font=("Helvetica",15)),
        sg.Button("Buscar",bind_return_key="-INPUT-",font=("Helvetica",15),key="-BUSCAR-"),
        sg.Text("Ordenar por: ",background_color=color_fondo,font=("Helvetica",15)),
        sg.InputCombo(criterios,default_value="Puntaje",readonly=True,enable_events=True,background_color=color_botones,
        size=(7,1),font=("Helvetica",20),key="-CRITERIO-")
        ],    
         
    ]
    layout = layout_2 + layout + [[sg.Button("Salir",font=("Helvetica",15),key="-SALIR-")]]
    
    return sg.Window("Puntajes",layout,background_color=color_fondo,button_color=color_botones,return_keyboard_events=True)


 