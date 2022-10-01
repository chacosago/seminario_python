import PySimpleGUI as sg

def build():
    color_fondo = "#45B39D"
    color_botones = "#3498DB"
    layout = [[sg.Text("Ingresa tu nick:",background_color=color_fondo,font=("Helvetica,20"),size=(15,1))],
        [sg.InputText(size=(30,3),background_color=color_botones,key="-NICK-")],
        [sg.Button("Entrar",key="-ENTER-",font=("Helvetica,20"),size=(15,1),bind_return_key="-ENTER-")],
        [sg.Text("",background_color=color_fondo)],
        [sg.Button("Registrarse",key="-REGISTER-",font=("Helvetica,20"),size=(15,1)),
            sg.Button("Salir",key="-EXIT-",font=("Helvetica,20"),size=(15,1))],
        [sg.Button("Ayuda",key="-HELP-",font=("Helvetica,20"),size=(15,1))],
        [sg.Text("",size=(28,3), font=("Helvetica",15), text_color="red", background_color=color_fondo,key="-ADVERTENCIA-")]        
    ]
    return sg.Window("Login",layout,margins=(100,60),return_keyboard_events=True,background_color=color_fondo,button_color=color_botones).finalize()