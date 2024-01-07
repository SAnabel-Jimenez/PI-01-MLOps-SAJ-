# Ya está listo para poder codear las APIs con Fastapi. Se usará el framework FastAPI 

#===================================== Librerías ===================================================
# Importar librerias
from fastapi import FastAPI # Importa la clase FastAPI del modulo fastapi
import pandas as pd 
from functions import PlayTimeGenre,UserForGenre,UsersRecommend,UsersWorstDeveloper,sentiment_analysis,recomendacion_juego

# Se crea una instancia llamada app
app = FastAPI() # Se crea la aplicacion


# http://127.0.0.1:8000   #borrar esta linea
# http://127.0.0.1:8000 #de ahora

# Se crea las definiciones de los métodos
# Define un decorador de operaciones de ruta
@app.get("/") 
async def portada():
    """
    Root de la aplicación

    Returns:
        str: Mensaje inicial que describe las funcionalidades de la aplicación.
    """
    PlayTimeGenre = '/PlayTimeGenre/'
    UserForGenre = '/UserForGenre/'
    UsersRecommend = '/UsersRecommend/'
    UsersWorstDeveloper = '/UsersWorstDeveloper/'
    sentiment_analysis = '/sentiment_analysis/'
    recomendacion_juego = '/recomendacion_juego/'

    return {"Proyecto": "PI - Machine Learning Operations (MLOps). " + "Las funciones disponibles en esta API son: "+PlayTimeGenre + ","+UserForGenre + ","+UsersRecommend +","+UsersWorstDeveloper+","+sentiment_analysis+ ","+recomendacion_juego + "."+"Ingrese una de ellas en la barra de navegación"}

#===================================== ENDPOINTS ===================================================
# ENDPOINT 1
@app.get("/PlayTimeGenre/{genero}") # Parametro:genero
def Endpoint1_PlayTimeGenre(genero: str):
    """
    Ruta para obtener el año con más horas jugadas para dicho género.

    Parametros: 
        genero (str): Género del cual se quiere conocer el año con más horas jugadas.
    
    Return: 
        Diccionario con el año que registra más horas jugadas para el género indicado.
    """
    result = PlayTimeGenre(genero)

    return result


# ENDPOINT 2
@app.get("/UserForGenre/{genero}") # Parametro:genero
def Endpoint2_UserForGenre(genero: str):
    """
    Ruta para obtener el usuario con más horas jugadas para el género dado y una lista de sus horas jugadas por año.

    Parametros: 
        genero (str): Género del cual se quiere conocer el usuario y su lista de horas por año.
    
    Return: 
        Diccionario con el usuario con más horas jugadas para el género dado y lista de sus horas jugadas por año.
    """
    result = UserForGenre(genero)

    return result



# ENDPOINT 3
@app.get("/UsersRecommend/{year}") # Parametro:genero
def Endpoint3_UsersRecommend(year: int):
    """
    Ruta para obtener el TOP 3 de juegos más recomendados para el año dado.

    Parametros: 
        year (int): Año 
    
    Return: 
        Diccionario con los 3 primeros puestos de los juegos más recomendados para el año indicado
    """
    result = UsersRecommend(year)

    return result


# ENDPOINT 4
@app.get("/UsersWorstDeveloper/{year}") # Parametro:genero
def Endpoint4_UsersWorstDeveloper(year: int):
    """
    Ruta para obtener el TOP 3 de las desarrolladoras menos recomendadas por los usuarios para el año dado.

    Parametros: 
        year (int): Año
    
    Return: 
        Diccionario con el año el TOP 3 de las desarrollaas menos recomendadas para ese año.
    """
    result = UsersWorstDeveloper(year)

    return result


# ENDPOINT 5
@app.get("/sentiment_analysis/{empresa_desarrolladora}") # Parametro:genero
def Endpoint5_sentiment_analysis(empresa_desarrolladora: str):
    """
    Ruta para obtener las desarrolladoras y la cantidad total de reseñas categorizadas con un análisis de sentimientos.

    Parametros: 
        empresa_desarrolladora (str): Empresa desarrolladora.
    
    Return: 
        Diccionario con el nombre de la empresa desarrolladora y la cantidad de reseñas por categoría.
    """
    result = sentiment_analysis(empresa_desarrolladora)

    return result

# ENDPOINT 6
@app.get("/recomendacion_juego/{item_id}") # Parametro:genero
def Endpoint6_recomendacion_juego(item_id: int):
    """
    Ruta para obtener los juegos recomendados similares al ingresado.

    Parametros: 
        item_id (int): id del producto.
    
    Return: 
        Listado del nombre de los juegos similares para el item_id indicado.
    """
    result = recomendacion_juego(item_id)

    return result