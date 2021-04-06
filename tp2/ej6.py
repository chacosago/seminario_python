# Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y
# minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula.

import procesar_palabras  

frase = """
        Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
        automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
        reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
        un montón de archivos con fotos de una manera compleja. Tal vez quieras
        escribir alguna pequeña base de datos personalizada, o una aplicación
        especializada con interfaz gráfica, o UN juego simple.
        """

palabras = procesar_palabras.texto_en_palabras(frase.lower())
print(f"len() de la frase: {len(frase)}\n")
print(f"len de palabras {len(palabras)}, y palabras:\n {palabras}\n")
palabras_unicas = list(set(palabras))
print(f"len de palabras_unicas {len(palabras_unicas)}, y sus palabras:\n {palabras_unicas}")
