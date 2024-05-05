from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#carga de archivos
 
endpoint1 = pd.read_csv('endpoint1.csv') 
endpoint2 = pd.read_csv('endpoint2.csv')
endpoint3 = pd.read_csv('endpoint3.csv')
endpoint5 = pd.read_csv('endpoint5.csv')
recomendados = pd.read_csv('recomendado.csv')

app = FastAPI()

@app.get('/end1/{genero}')                                # ENDPOINT1
def PlayTimeGenre( genero : str ):
    horas_por_año = {}
    for index, row in endpoint1.iterrows(): # endpoint1 es la variable que refiere al csv
        if genero in row['genres']:
            if row['release_date'] in horas_por_año:
                horas_por_año[row['release_date']] += row['horas']
            else:
                horas_por_año[row['release_date']] = row['horas']
    if horas_por_año:
        año_mas_jugado = max(horas_por_año, key=horas_por_año.get)
        horas_por_año = {}
        return f"año mas jugado para {genero} es: {año_mas_jugado}"
    else:
        return 'No se encontró dicho genero'
    
@app.get('/end2/{genero}')                                  # ENDPOINT2
def UserForGenre(genero: str):
    playtime_por_usuario = {}
    playtime_por_año = {}

    for index, registro in endpoint2.iterrows():
        if registro['genres'] == genero:
            user_id = registro['user_id']
            playtime = registro['playtime_forever']
            if user_id in playtime_por_usuario:
                playtime_por_usuario[user_id] += playtime
            else:
                playtime_por_usuario[user_id] = playtime

            año = registro['release_date'][:4]  # Obtenemos solo el año
            if user_id in playtime_por_año:
                playtime_por_año[user_id].setdefault(año, 0)
                playtime_por_año[user_id][año] += playtime
            else:
                playtime_por_año[user_id] = {año: playtime}
        else: return print("No se encuentra el genero")

    max_playtime = max(playtime_por_usuario.values())
    usuario_max_playtime = [user_id for user_id, playtime in playtime_por_usuario.items() if round(playtime, 2) == max_playtime]

    años_playtime_max = playtime_por_año.get(usuario_max_playtime[0], {})
    # Convertir el playtime de cada año a horas
    for año, playtime in años_playtime_max.items():
        años_playtime_max[año] = playtime / 60  # Suponiendo que las unidades de juego son horas

    return f"Usuario que mas jugó: {usuario_max_playtime[0] if usuario_max_playtime else None}. Los años {años_playtime_max} horas"


@app.get('/end3/{ano}')  # ENDPOINT 3
def UsersRecommend(ano: int):
    
    if ano in endpoint3['año_posted']:
        data_valor = endpoint3[endpoint3['año_posted'] == ano]
        data_valor = data_valor.sort_values(by='count', ascending=False)
        max_game = data_valor.iloc[0]['app_name']
        second_max_game = data_valor.iloc[1]['app_name']
        third_max_game = data_valor.iloc[2]['app_name']
        return {
            "Primero más recomendado": max_game,
            "Segundo más recomendado": second_max_game,
            "Tercer más recomendado": third_max_game
        }
    else: return print("No se encuentra el año")


@app.get('/end4/{ano}')                                   # ENDPOINT 4
def UsersNotRecommend (ano:int):
    if ano in endpoint3['año_posted']:
        data_valor = endpoint3[endpoint3['año_posted'] == ano] # Filtrar valor de la función
        data_valor = data_valor.sort_values(by='count', ascending=True) # Ordenar por columna count
        min_game = data_valor.iloc[0]['app_name'] # el 1°
        second_min_game = data_valor.iloc[1]['app_name'] # el 2°
        third_min_game = data_valor.iloc[2]['app_name'] # el 3°
        
        return "Primero más recomendado:", min_game, "Segundo más recomendado:", second_min_game, "Tercer más recomendado:", third_min_game
    else: return 'no se encuentra el año'

@app.get('/end5/{ano}')                                   # ENDPOINT 5
def sentiment_analysis(ano: int):
    list= endpoint5['año'].tolist()
    if ano in list:  # endpoint5 variable que refiere al csv
        return f"Negativos: {endpoint5.iloc[list.index(ano)]['sentiment_0']}, Neutros: {endpoint5.iloc[list.index(ano)]['sentiment_1']}, Positivos: {endpoint5.iloc[list.index(ano)]['sentiment_2']}"
    else:
        return 'No se encontró valor para:', ano

@app.get('/end6/{id}')
def recomendacion_juego( id : int):
    data = pd.read_csv('recomendado.csv')
    df = pd.DataFrame(data)

    if id not in df['id'].values:
        return print("No se encuentra ese ID")    

    id_consultado = df[df['id'] == id].iloc[:,2:26].values.reshape(1, -1)
    otros_id = df[df['id'] != 1].iloc[:,2:26].values

    similar = cosine_similarity(id_consultado, otros_id)

    mas_similares = similar.argsort()[0][-5:][::-1]
    ids_mas_similares = df.loc[df.index.isin(mas_similares), 'id'].tolist()
    return f"Los 5 IDs más similares: {ids_mas_similares}"
