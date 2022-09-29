import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def load(source):
    df = pd.read_csv(source, index_col=2, squeeze=True)
    df_sin_ultimos_15_dias = df.iloc[:, :-15] #Para no tomar en cuenta ultimos 15 dias
    return df_sin_ultimos_15_dias


df = load("data/Casos_Diarios_Estado_Nacional_Confirmados.csv")



def transform(dataframe):

    print("-" * 25, "Pico maximo a nivel nacional", "-" * 25)

    # 1ero.
    casos_nacionales = dataframe.iloc[-1:, 2:]
    casos_nacionales_t = casos_nacionales.transpose()
    print(casos_nacionales_t.loc[casos_nacionales_t.idxmax()])


    #Segundo
    # 2 Determianr el % de casos acumulados a nivel nacional


    print("-" * 25, "% de casos acumulados a nivel nacional", "-" * 25)

    # 2do.
    casos_acumulados = dataframe.iloc[-1:, 2:].sum(axis=1)
    print('casos acumulados', casos_acumulados)
    print('poblacion', dataframe.iloc[-1:, 1])
    porcentaje = (casos_acumulados * 100) / df.iloc[-1:, 1]
    print('porcentaje', porcentaje)

    plt.show()


    print("-" * 25, "Pico Maximo de Estados", "-" * 25)

    # 3ero.
    grouped_data = dataframe.groupby('nombre')
    print(grouped_data.mean().iloc[:-1, 2:].idxmax(axis=1))

    # 4to.
    casos_e_acumulados = df.iloc[:-1, 2:].sum(axis=1)
    print(df.iloc[:-1, 2:].sum(axis=1))
    print('casos', casos_e_acumulados[casos_e_acumulados == casos_e_acumulados.max()])

    # 5to.
    print("-" * 25, "Estado con mas % de casos acomulados", "*" * 25)
    porcentajaCasosAcom = (casos_e_acumulados * 100) / df.iloc[:, 0]
    print(porcentajaCasosAcom[porcentajaCasosAcom == porcentajaCasosAcom.max()])




transform(df)