import PySimpleGUI as sg
from src.windows import layout_tablero
from src.objects import tablero            

def generar_tablero(usuario) :  
    """Genera la ventana del tablero de juego y le da funcionalidad
    haciendo uso del objeto tablero.
    """
    ventana_tablero = layout_tablero.build(usuario)
    obj_tablero = tablero.Tablero(usuario,ventana_tablero)     

    while True :
        event,_values = ventana_tablero.read(timeout=900)          

        if event in (sg.WINDOW_CLOSED,"-EXIT-") :
            if obj_tablero.partida_en_curso() :
                obj_tablero.guardar_jugada_fin("abandonada") 
            break

        if obj_tablero.cant_select_igual_a_coincidencias() :
            obj_tablero.ocultar_cartas()

        if event == "-START-" :
            obj_tablero.comenzar()

        if event == "-AYUDAR-" :
            obj_tablero.ayuda()
        
        if event == "-RESET-" :
            if obj_tablero.partida_en_curso() :
                obj_tablero.guardar_jugada_fin("abandonada") 
                obj_tablero.reiniciar_tablero()

        if event.isnumeric() and not obj_tablero.carta_fue_levantada(event) :
            obj_tablero.mostrar_carta(event)  

        if obj_tablero.partida_en_curso() :
            obj_tablero.actualizar_timers()  

        if obj_tablero.cant_select_igual_a_coincidencias() :
            obj_tablero.evaluar_cartas_seleccionadas()                        
        
        if  obj_tablero.se_termino_el_tiempo() :
            obj_tablero.mostrar_cartel_perdiste()              
            obj_tablero.reiniciar_tablero()      
            obj_tablero.guardar_jugada_fin("timeout")          

        if obj_tablero.se_encontraron_todas_las_cartas() :
            obj_tablero.mostrar_cartel_ganaste()
            obj_tablero.guardar_jugada_fin("finalizada")
            obj_tablero.guardar_puntajes()                
            obj_tablero.reiniciar_tablero()  
            
    ventana_tablero.close()