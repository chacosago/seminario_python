import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
from numpy import fix
matplotlib.use('TkAgg')
import os
import pandas as pd
from src.windows import layout_estadisticas, layout_no_hay_partidas_jugadas

def tiempo_promedio_por_nivel(df) :
    """Esta función recibe el data frame de registro de eventos
    por parámetro y genera un gráfico de barras que indica el tiempo
    promedio por nivel.     
    """
    try: 
        partida_duracion = df.groupby("Partida").last()
        partida_duracion["Duracion"] = df.groupby("Partida").agg({"Tiempo" : "max"}) - df.groupby("Partida").agg({"Tiempo" : "min"})
        partida_duracion = partida_duracion[partida_duracion["Estado"] == "finalizada"] 
        partida_duracion["Nivel"] = partida_duracion["Nivel"].replace({ 0 : "Personalizado"})
        promedio_por_nivel = partida_duracion.groupby("Nivel").agg({"Duracion" : "mean"})
        promedio_por_nivel.rename(columns={"Duracion" : "Duracion promedio"},inplace=True)
        promedio_por_nivel.plot(kind="bar")
        plt.xticks(rotation="horizontal")

    except :
        # Si no hay partidas ganadas registradas tira error
        pass
def porcentaje_generos(df) :
    """Esta función recibe el data frame de registro de eventos
    por parámetro y genera un gráfico de pie que muestra el
    porcentaje de partidas terminadas según cada género.
    """
    etiquetas = ["Hombre","Mujer", "Otro"]
    l = [len(df[(df["Nombre_del_evento"] == "fin") & (df["Genero"] == i)]) for i in etiquetas]
    explode2 = ( 0, 0, 0)
    plt.pie(l,explode=explode2,autopct='%1.2f%%',shadow=True,startangle=90,labeldistance=1.1)
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Partidas finalizadas por género")    

def porcentaje_dias_semana(df) :
    """Esta función recibe el data frame de registro de eventos
    por parámetro y genera un gráfico de pie que muestra el porcentaje
    de partidas que se juegan para cada día de la semana.
    """
    df["dia"] = pd.to_datetime(df["Tiempo"],unit='s').dt.weekday
    data_grafico = [ len(df[["Tiempo", "Partida", "dia"]].groupby("Partida").apply(lambda x: x)[df["dia"] == i]) for i in range(7)]
    etiquetas = ["lunes","martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    explode2 = ( 0, 0, 0, 0, 0, 0, 0)
    plt.pie(data_grafico,explode=explode2,shadow=True,startangle=90,labeldistance=1.1,autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '')
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Porcentaje de partidas finalizadas por día")

def top_diez_palabras(df) :
    """Esta función recibe el data frame de registro de eventos
    por parámetro y genera un gráfico de barras que muestra el top 
    diez de palabras que se encontraron primero.
    """
    try :    
        df = df[df["Estado"] == "ok"].groupby("Partida").first().groupby("Palabra").count()
        df = df.rename(columns={"Tiempo" : "Cantidad"})
        df = df.drop(["Nick","Edad","Estado","Genero","Nivel","Nombre_del_evento","Cantidad_palabras_a_adivinar"], axis=1)
        df = df.sort_values("Cantidad").tail(10)
        df.plot.barh()
    except :
        #Cuando no hay estados ok se rompería, con este try, en lugar de romperse retorna un gráfico vacío
        pass

def porcentaje_por_estado(df) :
    """Esta función recibe el data frame de registro de eventos
    por parámetro y genera un gráfico de pie que muestra el 
    porcentaje de partidas terminadas por estado.
    """
    estados = ["abandonada","finalizada","timeout"]
    lista = [ len(df[df["Estado"] == i]) for i in estados]
    explode2 = ( 0, 0, 0)
    plt.pie(lista,explode=explode2,shadow=True,startangle=90,labeldistance=1.1,autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '')
    plt.axis('equal')
    plt.legend(estados)
    plt.title("Porcentaje de partidas por estado")

def porcentaje_palabras_timeout(df) :
    """Esta función recibe el data frame de registro de eventos
    por parámetro y genera un gráfico de barras que muestra
    el porcentaje de palabras encontradas en cada partida que terminó
    por límite de tiempo.
    """
    def calcular_porcentaje(fila) :
        encontradas = fila["Estado"]
        if fila["Estado2"] in ("ok","error") :
            encontradas += 1
        return (encontradas-2) / fila["Cantidad_palabras_a_adivinar"] * 100

    try :
        df_filtrado = df[(df["Estado"] != "error")]
        df_filtrado = df_filtrado.fillna("inicio")
        df_filtrado = df_filtrado.groupby("Partida").agg({"Estado" : "count" , "Cantidad_palabras_a_adivinar" : "first"})
        df_filtrado["Estado2"] = df.groupby("Partida").last()["Estado"]
        df_filtrado["Porcentaje_completado"] = df_filtrado.apply(calcular_porcentaje, axis=1)
        df_filtrado = df_filtrado[df_filtrado["Estado2"] == "timeout" ]
        df_filtrado = df_filtrado.drop(["Estado","Cantidad_palabras_a_adivinar","Estado2"],axis=1).sort_values("Porcentaje_completado",ascending=True).plot(kind="bar")
    except :
        #Si no hay partidas terminadas por timeout se rompe el programa
        pass

def draw_figure(canvas, figure):
        """Esta función recibe un gráfico y un canvas por parámetro
        y muestra el gráfico recibido en el canvas.
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

def generar_ventana_estadisticas(usuario) :
    """Recibe el diccionario usuario por parámetro
    y genera la ventana de estadísiticas.    
    """
    path_file = os.path.join(os.getcwd(),"src","files", "datos_jugadas.csv" )   

    # Se comprueba si el archivo existe, de ser así se define un conjunto de opciones
    # y se asigna un layout con un canvas en blanco, sino se muestra otro layout por default
    if os.path.exists (path_file) :
        df = pd.read_csv(path_file,encoding="utf-8")
        opciones = ["Porcentaje de partidas terminadas por género","Tiempo promedio de partidas por nivel (seg)","Porcentaje de partidas finalizadas por día",
                    "Top 10 de palabras encontradas primero","Porcentaje de partidas por estado","% de palabras encontradas en partidas timeout"] 
        fig = plt.gcf()        
        DPI = fig.get_dpi()
        fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
        ventana_estadisticas = layout_estadisticas.build(usuario["Configuracion"]["Color_fondo"],usuario["Configuracion"]["Color_botones"],opciones)
        figure_canvas_agg = draw_figure(ventana_estadisticas['-CANVAS-'].TKCanvas, fig)
    else :
        ventana_estadisticas = layout_no_hay_partidas_jugadas.build("Estadisticas",usuario["Configuracion"]["Color_fondo"])    

    # Bucle de la ventana
    while True :
        event, values = ventana_estadisticas.read()
        if event in (sg.WIN_CLOSED,"-SALIR-") :
            plt.clf()
            break
        if event == "-OP-" :
            figure_canvas_agg.get_tk_widget().forget()
            plt.clf()
            if values["-OP-"] == opciones[0] :
                porcentaje_generos(df.copy())                
            elif values["-OP-"] == opciones [1] :                
                tiempo_promedio_por_nivel(df.copy())                
            elif values["-OP-"] == opciones[2] :
                porcentaje_dias_semana(df.copy())
            elif values["-OP-"] == opciones[3] :
                top_diez_palabras(df.copy())
            elif values["-OP-"] == opciones[4] :
                porcentaje_por_estado(df.copy())
            elif values["-OP-"] == opciones[5] :
                porcentaje_palabras_timeout(df.copy())
            fig = plt.gcf()    
            DPI = fig.get_dpi()    
            fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            figure_canvas_agg = draw_figure(ventana_estadisticas['-CANVAS-'].TKCanvas, fig)
    ventana_estadisticas.close()