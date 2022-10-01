import json
import os
from src.functions import funcionalidades_tablero as ft

class Configuracion :
    """ Contiene la funcionalidad y los atributos que hacen funcionar
    la ventana de configuración. 
    """
    def __init__(self,usuario,layout) :        
        self._ventana_configuracion = layout
        self._usuario = usuario
        self._tipo_coincidencias = [("Imagen/Imagen", "-TIPO1-"), ("Imagen/Palabra", "-TIPO2-"), ("Palabra/Palabra", "-TIPO3-")]

    def set_parametros(self,alto,ancho,tiempo) :
        """ Hace que al seleccionar un nivel se establezcan los valores asociados al
        mismo y se muestren dichos parámentros en la ventana.
        """
        self._usuario["Configuracion"]["Alto"] = alto
        self._usuario["Configuracion"]["Ancho"] = ancho
        self._usuario["Configuracion"]["Tiempo"] = tiempo
        self._ventana_configuracion["-ALTO-"].update(str(alto))
        self._ventana_configuracion["-ANCHO-"].update(str(ancho))
        self._ventana_configuracion["-TIEMPO-"].update(str(tiempo))
        self._ventana_configuracion.refresh()

    def actualizar_usuario(self,values) :
        """En caso de que se quieran conservar los cambios realizados, este método
        actualiza la variable usuario con dichos cambios.
        """
        #Se guardan en usuario los valores de tamaño y tiempo elegidos en la pantalla de configuración
        self._usuario["Configuracion"]["Ancho"] = int(values["-ANCHO-"])                     
        self._usuario["Configuracion"]["Alto"] = int(values["-ALTO-"])                
        self._usuario["Configuracion"]["Tiempo"] = int(values["-TIEMPO-"])
        #Se guardan en usuario los mensajes que se muestran al ganar o perder elegidos en la pantalla de configuración
        if values["-WIN-"] is not None :
            self._usuario["Configuracion"]["Mensaje_ganaste"] = values["-WIN-"]
        if values["-LOSE-"] is not None :
            self._usuario["Configuracion"]["Mensaje_perdiste"] = values["-LOSE-"]
        #Se guarda la opcion elegida con respecto a la ayuda desntro del juego        
        self._usuario["Configuracion"]["Ayuda"] = values["-CON-"]        
        #Se guardan en usuario los colores elegidos en la pantalla de configuración
        if values["-COLORFONDO-"] != "" and values["-COLORFONDO-"] != "None" :
            self._usuario["Configuracion"]["Color_fondo"] = values["-COLORFONDO-"]
        if values["-COLORBOTONES-"] != "" and values["-COLORBOTONES-"] != "None" :
            self._usuario["Configuracion"]["Color_botones"] = values["-COLORBOTONES-"]

        #Se guarda en usuario la cantidad de coicidencias seleccionada en la pantalla de configuración
        self._usuario["Configuracion"]["Coincidencias"] = values["-COIN-"]

        #Se gurda en usuario el tipo de coincidencia seleccionado en la pantalla de configuración 
        
        for h in self._tipo_coincidencias :
            if values[h[1]] : 
                self._usuario["Configuracion"]["Tipo_coincidencias"] = h[0]

    def guardar_configuracion(self,values) :
        """Guarda los cambios de la configuración de manera persistente en el archivo
        de usuarios.
        """
        path_file = os.path.join(os.getcwd(), "src", "files", "usuarios.json" )
        with open(path_file,"r") as usuarios:
            lista_usuarios = json.load(usuarios)
        # Busco el usuario que si o si esta:
        for i in lista_usuarios :
            if i["Nick"] == self._usuario["Nick"] :
                i["Configuracion"]["Ancho"] = int(values["-ANCHO-"])
                i["Configuracion"]["Alto"] = int(values["-ALTO-"])
                #Estos dos campos necesitan ser chequeados porque pueden guardar valores nulos blancos
                #en caso de cikcear el boton y no cambiar cambiar el color
                if values["-COLORFONDO-"] != "" and values["-COLORFONDO-"] != "None" :
                    i["Configuracion"]["Color_fondo"] = values["-COLORFONDO-"]
                if values["-COLORBOTONES-"] != "" and values["-COLORBOTONES-"] != "None" :
                    i["Configuracion"]["Color_botones"] = values["-COLORBOTONES-"]
                i["Configuracion"]["Tiempo"] = values["-TIEMPO-"]
                i["Configuracion"]["Coincidencias"] = values["-COIN-"]
                i["Configuracion"]["Mensaje_ganaste"] = values["-WIN-"]
                i["Configuracion"]["Mensaje_perdiste"] = values["-LOSE-"]
                i["Configuracion"]["Ayuda"] = values["-CON-"]  
                for j in self._tipo_coincidencias :
                    if values[j[1]] : 
                        i["Configuracion"]["Tipo_coincidencias"] = j[0]
                break
        
        with open(path_file,"w") as usuarios:
            json.dump(lista_usuarios,usuarios,indent=4)

    def actualizar_coincidencias(self,values) :
        """ Actualiza la cantidad de coincidencias con las que es posible jugar,
        en base al tamaño del tablero en tiempo real.
        """
        tupla = ft.calcular_coincidencias(values["-ANCHO-"]*values["-ALTO-"])
        if values["-COIN-"] in tupla :
            self._ventana_configuracion["-COIN-"].update(values["-COIN-"],tupla,size=(20, 3))
        else:
            self._ventana_configuracion["-COIN-"].update(tupla[0],tupla,size=(20, 3))            
        self._ventana_configuracion.refresh()
    
    def get_usuario(self) :
        return self._usuario