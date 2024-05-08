Índice:
    Introducción
    Desarrollo
	ETL
	Machine learning
	EDA
    API local (FastAPI)
    API remoto (RENDER.COM)
    Tecnologías usadas
    Base de datos de STEAM
    Dirección de la API    

**Introducción
El proyecto simula que la plataforma Steam nos contrata para realizar un producto mínimo viable sobre un sistema remoto de recomendaciones de sus videos juegos.
El desarrollo del proyecto consiste en tomar las bases de datos brindadas. Estas serán tratadas para poder disponibilizar la información. A partir de ella se tomará la información necesaria para ejecutar consultas específicas vía web.

**Desarrollo

*  ETL 
Para desarrollar este producto, Steam nos brinda 79,3mb de información comprimida. Cuando accedemos a ella, nos encontramos que se encuentra de forma anidada (significa que la información está dentro de la información). Esto demanda que debemos dar un tratamiento con el fin de presentarla de forma legible.
Superada la etapa anterior. Obtenemos los siguientes dataframes:
Games2:	Refiere a la información por juego
Reviews2:	Opinión de los jugadores
Items2 		Información adicional de jugadores sobre los juegos.
Finalmente, los exploramos para determinar la relación entre ellos.

*  Machine learning para análisis de sentimientos.
En el dataframe reviews se encuentra la columna reviews. La misma es una recopilación de opiniones de los jugadores acerca de los juegos. A través de la librería textblob procedemos a analizar dichas opiniones. Como resultado tendremos dos aspectos. El primero es una estandarización sobre si el juego gusta o no gusta en una escala del -1 al 1 en el parámetro polarrity. El segundo es que tan subjetiva es la opinión. Tomamos la polaridad y la discretizamos en tres segmentos: 
0 para valores inferior a -0.33
1 para valores entre -0.33 y 0.33
2 para valores superiores de 0.33

*  EDA
El proceso de EDA en este proyecto se orienta a lo siguiente. Poder tomar la información necesaria de los dataframe logrados para poder ejecutar las seis funciones de consulta. Para ello se diseña un dataframe específico y se diseña la función pedida por cada una de las seis consignas.
Las definiciones pedidas son:
1)  def PlayTimeGenre( genero : str ): Debe devolver año con más horas jugadas para dicho género.
2)  def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
3)  def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. 
4)  def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. 
5)  def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
6)  def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

**API local (FastAPI)
Desarrollados los códigos para las distintas funciones, armados los distintos dataframes y materializados en archivos csv. Se armó un archivo main.py para probar de forma local con el framework de FastAPI siguiendo las instrucciones del siguiente enlace: https://www.youtube.com/watch?v=J0y2tjBz2Ao

**API remoto (RENDER.COM)
Probado el proyecto de forma local. Se apaga el servidor de FastAPI. Se crea una carpeta nueva vacía en la cual desde git bash se crea un entorno virtual, se activa. Se crea un nuevo repositorio (git init) y se incluyen todos los archivos necesarios. Se los conecta de forma remota a un repositorio remoto a la cuenta de Git-Hub y se clona el repositorio.
Con toda esta información se crea un “web server” en render.com y se realiza un deploy.
Se consiguió esta dirección: https://proyecto-individual1-zfim.onrender.com/docs
Al entrar a esa dirección tenemos los 6 endpoint que corresponden a las 6 funciones probadas. Para usarlas solo hay que hacer click  en la función que se desea. Se desplegarán los parámetros. Hacer click en Try it Out. En descripción ingresar el parámetro a consultar y hacer click en Execute y en “Response body” tendremos la respuesta de la función

**Tecnologías usadas:
  Python
  Pandas
  Scikit-learn
  Uvicorn
  FastAPI
  Render
  Git
  Git-Hub

**Base de datos de Stem:
  https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj

**Dirección de la API
https://proyecto-individual1-zfim.onrender.com