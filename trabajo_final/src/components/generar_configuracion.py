import PySimpleGUI as sg
from src.windows import layout_configuracion
from src.objects import configuracion


def generar_configuracion(usuario) :
    """Genera la ventana de configuración haciendo uso
    del objeto configuración. 
    """
    mensajes = [
            ["¡Felicidades!","¡Enhorabuena!","¡Genial!"],
            ["¡Que lástima!","¡Seguí participando!","¡Que macana!"]
        ]   
    ventana_configuracion = layout_configuracion.build(usuario,mensajes)
    obj_configuracion = configuracion.Configuracion(usuario,ventana_configuracion)    
    while True :
        event,values = ventana_configuracion.read(timeout=500)    

        if event in (sg.WINDOW_CLOSED,"-EXIT-") :
            break
        if values is not None : 
            obj_configuracion.actualizar_coincidencias(values)        
        if event == "-NIVEL1-" :
            obj_configuracion.set_parametros(3,4,50)
        if event == "-NIVEL2-" :
            obj_configuracion.set_parametros(4,6,80)
        if event == "-NIVEL3-" :
            obj_configuracion.set_parametros(5,6,120)
        if event == "-SAVE-":                    
            obj_configuracion.actualizar_usuario(values)  
            obj_configuracion.guardar_configuracion(values)                
            break
    ventana_configuracion.close()

    return obj_configuracion.get_usuario()