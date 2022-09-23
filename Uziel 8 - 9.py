import pandas as pd
import hypothesis

path = "./data/Casos_Diarios_Estado_Nacional_Confirmados.csv"

def read_data(path):
    data = pd.read_csv(path)
    return data
print("\nLa lectura de los datos es:\n",read_data(path))

def drop_data(data):
    covid_data = data.drop(columns=['cve_ent','poblacion'])
    return covid_data
print("\nInformacion con drop:\n",drop_data(read_data(path)))

def media_estado(covid_data):
    media_estado = covid_data.mean(axis = 0)
    return media_estado
print("\nMedia por cada estado:\n",media_estado(drop_data(read_data(path))))