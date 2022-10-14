import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


def extract(source):
    df = pd.read_csv(source, index_col=2, squeeze=True)
    df_sin_ultimos_15_dias = df.iloc[:, :-15]  # Para no tomar en cuenta ultimos 15 dias
    return df_sin_ultimos_15_dias


df = extract("data/Casos_Diarios_Estado_Nacional_Confirmados.csv")


def transform(dataframe):
    print('PRIMERO-----------------------')
    pico_maximo_nacional = {
        'Nivel': ['Nacional'],
        'Fecha': [dataframe.iloc[-1, 2:].idxmax()],
        'Casos': [dataframe.iloc[-1, 2:].max()]
    }
    primero = pd.DataFrame(pico_maximo_nacional)

    # print('SEGUNDO-----------------------')
    casos_acumulados = dataframe.iloc[-1:, 2:].sum(axis=1)
    # print('casos acumulados\n', casos_acumulados)
    # print('poblacion', dataframe.iloc[-1:, 1])
    porcentaje = (casos_acumulados * 100) / dataframe.iloc[-1:, 1]
    segundo = porcentaje

    # 3ero.
    # print('TERCERO-----------------------')
    tercero = dataframe.iloc[:-1, 2:].idxmax(axis=1)

    # 4to.
    # print('CUARTO-----------------------')
    total_casos = dataframe.iloc[:-1, 2:].sum(axis=1)

    estado_mas_casos = {
        'Estado': [total_casos.idxmax()],
        'Casos': [total_casos.max()]
    }

    cuarto = pd.DataFrame(estado_mas_casos)

    # 5to.
    # print('QUINTO-----------------------')
    casos_por_estado = dataframe.iloc[:-1, 2:].sum(axis=1)
    poblacion = dataframe.iloc[:-1, 1]
    porcentaje = (casos_por_estado * 100) / poblacion

    mayor_porcentaje = {
        'Estado': [porcentaje.idxmax()],
        '%': [porcentaje.max()]
    }

    quinto = pd.DataFrame(mayor_porcentaje)

    # 6to.
    # print('SEXTO-----------------------')

    estado_menos_casos = {
        'Estado': [total_casos.idxmin()],
        'Casos': [total_casos.min()]
    }

    sexto = pd.DataFrame(estado_menos_casos)

    # 7mo.
    # print('SEPTIMO-----------------------')
    casos_por_estado = df.iloc[:-1, 2:].sum(axis=1)
    poblacion = df.iloc[:-1, 1]
    porcentaje = (casos_por_estado * 100) / poblacion

    menor_porcentaje = {
        'Estado': [porcentaje.idxmin()],
        '%': [porcentaje.min()]
    }

    septimo = pd.DataFrame(menor_porcentaje)

    # print('OCTAVO-----------------------')
    media = dataframe.iloc[:-1, 2:].mean(axis=1)
    octavo = media

    return primero, segundo, tercero, cuarto, quinto, sexto, septimo, octavo


def grafica_ejercicio10(dataframe):
    # print('DECIMO-----------------------')
    dataframe.iloc[-1, 2:].plot()
    plt.show()


def load(primero, segundo, tercero, cuarto, quinto, sexto, septimo, octavo):
    writer = pd.ExcelWriter('Historico_contagios_nacional.xlsx')
    primero.to_excel(writer, sheet_name='Pico maximo nivel nacional', index=True)
    segundo.to_excel(writer, sheet_name='Porcentaje de casos nivel nacional', index=True)
    tercero.to_excel(writer, sheet_name='Fecha pico max por estado', index=True)
    cuarto.to_excel(writer, sheet_name='Estado con mas casos', index=True)
    quinto.to_excel(writer, sheet_name='Mayor porcentaje de casos', index=True)
    sexto.to_excel(writer, sheet_name='Estado con menos casos', index=True)
    septimo.to_excel(writer, sheet_name='Menor porcentaje de casos', index=True)
    octavo.to_excel(writer, sheet_name='Media de casos por estado', index=True)
    writer.save()


load(transform(df)[0],
     transform(df)[1],
     transform(df)[2],
     transform(df)[3],
     transform(df)[4],
     transform(df)[5],
     transform(df)[6],
     transform(df)[7])

grafica_ejercicio10(df)
