import PySimpleGUI as sg
from src.functions import elementos_por_criterio, descargar_imagenes, funcionalidades_tablero
import random
import os
import time as t
import csv 

class Tablero :
    """ Contiene la funcionalidad y los atributos que hacen funcionar
    la ventana del tablero. Es el elemento principal del juego.
    """
    def __init__(self,usuario,layout)  :
        self._tablero = layout
        self._genero = usuario["Género"]
        self._edad = usuario["Edad"]
        self._nombre = usuario["Nick"]
        self._config = usuario["Configuracion"]
        self._tiempo = self._config["Tiempo"]
        self._largo = self._config["Ancho"]
        self._alto = self._config["Alto"]
        self._coincidencias = int(self._config["Coincidencias"][0])
        # self._matches contiene el indice en la lista de imagenes en el que se encuentran
        # las cartas seleccionadas en cada paso/turno.
        self._matches = []
        self._start = False
        self._tiempo_actual = 0     
        self._elementos_encontrados = 0
        self._path_file = os.path.join(os.getcwd(), "src", "files", "" )
        #El siguiente número debe ser un integer porque es usado como índice, y aunque la cuenta nunca va a retornar un 
        #número real, los números que la componen si lo son
        self._cant_cartas_unicas = int(self._largo * self._alto / self._coincidencias)
        #self._images contiene las cartas representadas por tuplas (ver docstring mostrar_carta)
        self._images = self.crear_lista_imagenes()
        self._tablero["-GENERO-"].update(self._generos[0].capitalize() + ", " + self._generos[1].capitalize())
        self._tablero["-DESCARGA-"].update("")
        self._tablero["-NIVEL-"].update(self._get_nivel() if self._get_nivel() != 0 else "Personalizado")
        self._cant_cartas = len(self._images)
        # self._estado_cartas es una lista de booleanos que indica que cartas están dadas vuelta.
        self._estado_cartas = [False for i in range(self._cant_cartas)]
        self._penalizacion = 1
        self._cant_ayudas = 0


    def reiniciar_tablero(self) :
        """Resetea el tablero, dando vuelta las cartas, mezclándolas, poniendo los contadores en 0, etc.
        """
        for i in  range(self._largo * self._alto) :
            self._tablero[str(i)].update("",disabled=True,image_filename=self._path_file+"default.png",image_subsample=4,image_size=(160,160))
            self._tablero["-AVANCE-"].update("Avance: 0 %")
        
        self._tablero["-TIMER-"].update("00:00")
        self._tablero["-START-"].update(disabled=False) 
        self._tablero["-AYUDAR-"].update(disabled=True) 
        self._tiempo_actual = 0 
        self._tablero.refresh()        
        self._tiempo_inicio = t.time()                                            
        self._start = False
        self._elementos_encontrados = 0
        self._cant_cartas = len(self._images)
        random.shuffle(self._images)
        self._estado_cartas = [False for i in range(self._cant_cartas)]
        self._penalizacion = 1
        self._cant_ayudas = 0
        self._tablero["-RESET-"].update(disabled=True)
        self._tablero["-DESCUENTO-"].update("-0 %", text_color="blue")
        self._matches.clear()

    def mostrar_carta(self,event) :
        """ Recibe un identificador de la carta elegida y la da vuelta en función de la modalidad
        de juego. Cada carta está representada por una tupla de 3 elementos, el primer elemento contiene la url
        de la imagen de la carta. El segundo elemento contiene el nombre del anime. Y el 
        tercer elemento contiene un string que, en caso de que la modalidad de juego sea palabra/imagen, 
        indica si la carta debe mostrar la imagen o el nombre (palabra).
        """
        opcion = self._config["Tipo_coincidencias"]
        if opcion == "Imagen/Imagen" :
            self._tablero[event].update(image_filename=self._images[int(event)][0],image_subsample=4,image_size=(160,160))
        elif opcion == "Imagen/Palabra" :
            if self._images[int(event)][2] == "imagen" :
                self._tablero[event].update(image_filename=self._images[int(event)][0],image_subsample=4,image_size=(160,160))
            else :   
                texto = funcionalidades_tablero.ajustar_texto(self._images[int(event)][1]) 
                self._tablero[event].update(texto,image_filename=self._path_file+"bottom.png",image_subsample=4,image_size=(160,160))
        else :
            texto = funcionalidades_tablero.ajustar_texto(self._images[int(event)][1]) 
            self._tablero[event].update(texto,image_filename=self._path_file+"bottom.png",image_subsample=4,image_size=(160,160))

        self._tablero.refresh() 
        self._matches.append(int(event)) 
        self._estado_cartas[int(event)] = True
 
    def comenzar(self) :
        """ Habilita al usuario a jugar, da inicio al cronómetro y
        habilita la ayuda en caso de corresponder.
        """
        self._guardar_jugada_inicio()
        self._tiempo_inicio = t.time()
        self._start = True                
        for i in range(self._largo * self._alto) :
            self._tablero[str(i)].update(disabled=False)
        self._tablero["-START-"].update(disabled=True)    
        if self._config["Ayuda"] :    
            self._tablero["-AYUDAR-"].update(disabled=False)
        self._tablero["-RESET-"].update(disabled=False)

    def actualizar_timers(self) :
        """ Actualiza el timer en la ventana.
        """
        self._tiempo_actual = t.time() - self._tiempo_inicio
        self._tablero["-TIMER-"].update(f"{round(self._tiempo_actual // 60):02d}:{round(self._tiempo_actual % 60):02d}")
        self._tablero.refresh()

    def evaluar_cartas_seleccionadas(self) :
        """ Evalúa si los elementos en la lista imagenes, en las posiciones indicadas
        por la lista matches son o no iguales (Si las cartas seleccionadas son iguales o no).
        Registra el evento y actualiza el % avance si corresponde.
        """
        if funcionalidades_tablero.validar(self._matches,self._images) :
            # las cartas coinciden
            self._guardar_jugada_intento("ok",self._images[self._matches[0]][1])
            self._cant_cartas-= self._coincidencias
            for j in self._matches :
                self._tablero[str(j)].update(disabled=True,image_subsample=4,image_size=(160,160))  
            self._elementos_encontrados += self._coincidencias
            self._tablero["-AVANCE-"].update(f"Avance: {round(self._elementos_encontrados * 100 / (self._largo * self._alto),ndigits=2)} %")              
            self._matches.clear()
        else :
            self._guardar_jugada_intento("error",self._images[self._matches[0]][1])              

    def ocultar_cartas(self) :
        """ Oculta las cartas seleccionadas según indica matches.
        """
        for j in self._matches :
            self._tablero[str(j)].update("",image_filename=self._path_file+"default.png",image_subsample=4,image_size=(160,160))
        for j in self._matches :
            self._estado_cartas[int(j)] = False 
        self._matches.clear()

    def crear_lista_imagenes(self) :
        """ Descarga las imagenes que corresponde segun el criterio del dia/hora.
        Genera
        """
        while True:
            rdo, self._generos = elementos_por_criterio.load()
            random.shuffle(rdo)
            if len(rdo) > self._cant_cartas_unicas:
                descargar_imagenes.descargar_todas(rdo[:self._cant_cartas_unicas]) 
                break

        return funcionalidades_tablero.generar_lista(rdo[:self._cant_cartas_unicas],self._coincidencias)  

    def _get_nivel(self) :
        """ Retorna el numero del nivel segun los parametros del tablero.
        """
        nivel = 0
        if self._config["Alto"]*self._config["Ancho"] == 12 and self._config["Tiempo"] == 50 :
            nivel = 1
        elif self._config["Alto"]*self._config["Ancho"] == 24 and self._config["Tiempo"] == 80 :
            nivel = 2
        elif self._config["Alto"]*self._config["Ancho"] == 30 and self._config["Tiempo"] == 120 :
            nivel = 3
        return nivel

    def guardar_puntajes(self) :
        """Guarda de manera persistente los puntajes de las partidas ganadas.
        """     
        if os.path.exists(self._path_file+"puntajes.csv") :
            with open(self._path_file+"puntajes.csv", "a", newline='', encoding="utf-8") as puntajes:
                writer = csv.writer(puntajes,delimiter=',')
                writer.writerow([self._nombre, self._puntaje, self._largo * self._alto,
                    f"{round(self._tiempo_actual // 60):02d}:{round(self._tiempo_actual % 60):02d}",f"{round(self._config['Tiempo'] // 60):02d}:{round(self._config['Tiempo'] % 60):02d}",
                    self._coincidencias,self._get_nivel(),self._cant_ayudas , t.strftime("%d/%m/%y")])
        else: 
            with open(self._path_file+"puntajes.csv","w", newline='', encoding="utf-8") as puntajes :
                writer = csv.writer(puntajes,delimiter=',')
                writer.writerow(["Jugador", "Puntaje", "Tamaño_tablero", "Duración", "Tiempo_total", "Coincidencias","Nivel","Ayudas" ,"Fecha"])
                writer.writerow([self._nombre, self._puntaje, self._largo * self._alto,
                f"{round(self._tiempo_actual // 60):02d}:{round(self._tiempo_actual % 60):02d}", f"{round(self._config['Tiempo'] // 60):02d}:{round(self._config['Tiempo'] % 60):02d}",
                self._coincidencias,self._get_nivel(),self._cant_ayudas, t.strftime("%d/%m/%y") ])

    def _guardar_jugada_inicio(self) :
        """ Registra el evento de inicio de partida.
        """
        if os.path.exists(self._path_file+"datos_jugadas.csv") :
            #Abre el archivo recupera el primer elemento de la última línea, lo incrementa y lo guarda en una variable
            with open(self._path_file+"datos_jugadas.csv", "r", newline='', encoding="utf-8") as jugadas:
                self._num_partida = int(list(csv.reader(jugadas)).pop()[0]) + 1 
            with open(self._path_file+"datos_jugadas.csv", "a", newline='', encoding="utf-8") as jugadas:
                writer = csv.writer(jugadas,delimiter=',')
                writer.writerow([self._num_partida,t.time(),self._cant_cartas_unicas,"inicio_partida",self._nombre,self._genero,self._edad,"","",self._get_nivel()])
        else: 
            with open(self._path_file+"datos_jugadas.csv","w", newline='', encoding="utf-8") as jugadas :
                writer = csv.writer(jugadas,delimiter=',')
                writer.writerow(["Partida", "Tiempo", "Cantidad_palabras_a_adivinar", "Nombre_del_evento", "Nick", "Genero", "Edad", "Estado", "Palabra", "Nivel"])
                writer.writerow([0,t.time(),self._cant_cartas_unicas,"inicio_partida",self._nombre,self._genero,self._edad,"","",self._get_nivel()])     
                self._num_partida = 0           

    def _guardar_jugada_intento(self,estado,nombre_carta) :
        """ Registra el evento del intento.
        """
        with open(self._path_file+"datos_jugadas.csv", "a", newline='', encoding="utf-8") as jugadas:
                writer = csv.writer(jugadas,delimiter=',')
                writer.writerow([self._num_partida,t.time(),self._cant_cartas_unicas,"intento",self._nombre,self._genero,self._edad,estado,nombre_carta,self._get_nivel()])

    def guardar_jugada_fin(self,razon) :
        """ Registra el evento de
        """
        if razon == "abandonada" :
            # Cuando se abandona la partida, se reinicis o se cierra la ventana, guardamos el tiempo actual. 
            self._tiempo_final = t.time()
        with open(self._path_file+"datos_jugadas.csv", "a", newline='', encoding="utf-8") as jugadas:
                writer = csv.writer(jugadas,delimiter=',')
                writer.writerow([self._num_partida,self._tiempo_final,self._cant_cartas_unicas,"fin",self._nombre,self._genero,self._edad,razon,"",self._get_nivel()])

    def ayuda(self) :
        """ Muestra todas las cartas ocultas por un breve tiempo que depende
        del tamaño del tablero. Además se actualiza la penalización por ayuda.
        """
        # cada ayuda reduce un 30% el puntaje total
        self._penalizacion *= 0.7
        self._tablero["-DESCUENTO-"].update(f"-{round(( 1 - self._penalizacion) * 100)} %", text_color="red")
        self._cant_ayudas += 1
        cartas_mostradas = list()
        for i in range(len(self._estado_cartas)) :
            if not self._estado_cartas[i] :
                self.mostrar_carta(str(i))
                cartas_mostradas.append(i)
        # la idea es que a mayor tamaño del tablero dure más la ayuda
        t.sleep( 0.5 + (self._largo * self._alto)/90 )
        for j in cartas_mostradas :
            self._tablero[str(j)].update("",image_filename=self._path_file+"default.png",image_subsample=4,image_size=(160,160))
            self._estado_cartas[j] = False
            self._matches.pop()
    
    def partida_en_curso(self) :
        return self._start

    def se_termino_el_tiempo(self) :
        return self._tiempo_actual > self._tiempo

    def se_encontraron_todas_las_cartas(self) :
        return self._cant_cartas == 0 

    def carta_fue_levantada(self,event) :
        """Retorna true si la carta correspondiende al evento ya fue seleccionada.
        """
        return int(event) in self._matches

    def cant_select_igual_a_coincidencias(self) :
        """ Retorna True si la cantidad de cartas seleccionadas es igual a la
        cantidad de ocurrencia de las mismas."""
        return len(self._matches) == self._coincidencias

    def mostrar_cartel_ganaste(self) :
        self._tiempo_final = t.time()
        tiempo = self._tiempo_final - self._tiempo_inicio
        self._puntaje = funcionalidades_tablero.calcular_puntajes(self._largo * self._alto,self._tiempo_actual,self._penalizacion)       
        duracion = f"{round( tiempo // 60)} minutos y {round( tiempo % 60)} segundos" if tiempo > 60 else f"{round( tiempo % 60)} segundos"
        sg.popup(self._config["Mensaje_ganaste"]+"\n"+f"Ganaste en {duracion}"+"\n"+"Obtuviste "+self._puntaje +" puntos"
        ,title="Ganaste",font=("Helvetica",20),background_color=self._config["Color_fondo"],button_color = self._config["Color_botones"],keep_on_top=True)

    def mostrar_cartel_perdiste(self) :
        self._tiempo_final = t.time()
        puntaje = funcionalidades_tablero.calcular_puntajes(self._elementos_encontrados,self._tiempo_actual,self._penalizacion)
        sg.popup(self._config["Mensaje_perdiste"]+"\n"+"Se acabó el tiempo :(" + "\n"+"Obtuviste "+ puntaje + " puntos", font=("Helvetica",20)
        ,title="Perdiste", background_color=self._config["Color_fondo"],button_color = self._config["Color_botones"],keep_on_top=True)  