import PySimpleGUI as sg 

def build() :
    color_fondo = "#45B39D"
    color_botones = "#3498DB"
    choices=[("Mujer","-GEN0-"),("Hombre","-GEN1-"),("Otro","-GEN2-")]
    layout = [[sg.Text("Nick name: ",background_color=color_fondo)],
        [sg.InputText(size=(30,2),background_color=color_botones,tooltip="El nombre debe tener al menos 3 carácteres, menos de 15 y no debe ser numérico.",key="-NICKNAME-")],
        [sg.Text("Edad: ",background_color=color_fondo)],
        [sg.InputText(size=(30,2),background_color=color_botones,tooltip="La edad debe ser un número menor que 99",key="-AGE-")],
        [sg.Text(" ",background_color=color_fondo)],
        [sg.Text("Género autopercibido: ",background_color=color_fondo)],
        [sg.Radio(i[0], 1, default=False, background_color=color_fondo, key=i[1]) for i in choices],
        [sg.Button("Guardar",font=("Helvetica",20),key="-SAVE-"),sg.Button("Cancelar",font=("Helvetica",20),key="-SALIR-")]
    ]
    return sg.Window("Registrarse",layout,margins=(100,100),return_keyboard_events=True,background_color=color_fondo,button_color=color_botones)