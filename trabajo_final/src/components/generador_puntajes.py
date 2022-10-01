import PySimpleGUI as sg
from src.windows import layout_puntajes
import os
import pandas as pd
from src.windows import layout_no_hay_partidas_jugadas 

def generar_layout(existe,data_set,config,criterios) : 
    """Recibe un booleano, un dataframe y un diccionario con la configuracion del usuario
    y dependiendo del valor del parámetro booldeano (que indica si el dataframe recibido 
    es o no None) genera un layout u otro haciendo uso de los otros dos parámetros recibidos.     
    """          
    lista_tablas = list()
    if existe :
        header_list = list(data_set)   
        lista_tablas = [ 
            data_set[data_set["Nivel"] == i ].sort_values('Puntaje',ascending=False).to_numpy().tolist() for i in range(1,4)
        ]       
        lista_tablas.append(data_set.sort_values('Puntaje',ascending=False).to_numpy().tolist())
        layout = layout_puntajes.build(config["Color_fondo"],config["Color_botones"],lista_tablas,header_list,criterios)
    else: 
        layout = layout_no_hay_partidas_jugadas.build("Puntajes",config["Color_fondo"])
    
    return (layout,lista_tablas)

def actualizar_puntajes(ventana_puntajes,values,data_set,criterio) :
    """ Esta función genera las listas que se van a mostrar en las tablas de puntajes
    ordenadas por el criterio recibido en el parámetro 'criterio'.
    En caso de recibir el nombre de un jugador solo mostrará las partidas de ese jugador,
    de lo contrario mostrará todas las partidas.
    """
    tablas = list()
    if values["-INPUT-"] != "" :
        for i in range(3) :
            aux = data_set[(data_set["Jugador"] == values["-INPUT-"]) & (data_set["Nivel"]== i+1)].sort_values(criterio,ascending=False).to_numpy().tolist()
            ventana_puntajes[str(i)].update(values=aux)
            tablas.append(aux)
        aux = data_set[(data_set["Jugador"] == values["-INPUT-"])].sort_values(criterio,ascending=False).to_numpy().tolist()
        ventana_puntajes["3"].update(values=aux)  
        tablas.append(aux)
    else :
        for i in range(1,4) :
            tabla_temporal = data_set[data_set["Nivel"] == i ].sort_values(criterio,ascending=False).to_numpy().tolist()
            ventana_puntajes[str(i-1)].update(values=tabla_temporal)
            tablas.append(tabla_temporal)
            tabla_temporal = data_set.sort_values(criterio,ascending=False).to_numpy().tolist()
        ventana_puntajes["3"].update(tabla_temporal)   
        tablas.append(tabla_temporal)
    return tablas

def ordenar_listas(lista,ventana_puntajes,criterio) :
    """ Esta funcion reordena las tablas mostradas en patanlla
    segun el criterio recibido por parámetro, y actualiza las tablas
    en pantalla.
    """
    dic = {"Puntaje" : 1,"Fecha" : 8,"Ayudas" : 7, "Duración" : 3} 
    lista_nueva = list()
    for i in lista :             
        lista_nueva.append(list(sorted(i,reverse=True,key= lambda x : x[dic[criterio]])))
    indice = 0
    for b in lista_nueva :
        ventana_puntajes[str(indice)].update(values=b)
        indice += 1
    return lista_nueva       

def generar_ventana_puntajes(usuario):
    """Genera la ventana donde se muestran los puntajes 
    """ 
    config = usuario["Configuracion"]
    path_csv = os.path.join(os.getcwd(), "src", "files", "puntajes.csv" ) 
    data_set = None
    existe = False
    criterios = ["Puntaje","Fecha","Ayudas","Duración"]
    criterio = criterios[0]
    if os.path.exists(path_csv) :   
        data_set = pd.read_csv(path_csv,encoding="utf-8") 
        existe = True         

    # Se guardan en la variable tablas las listas que se setean en la tablas para no tener 
    # que volver a calcularlas en caso de querer mostrarlas con otro orden
    ventana_puntajes, tablas = generar_layout(existe,data_set,config,criterios)

    while True :
        event,values = ventana_puntajes.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-") :
            break
        if event in ("\r","-BUSCAR-") :
            tablas = actualizar_puntajes(ventana_puntajes,values,data_set,criterio)   
        if event == "-CRITERIO-" :
            criterio = values["-CRITERIO-"]            
            tablas = ordenar_listas(tablas.copy(),ventana_puntajes,criterio)
    ventana_puntajes.close()