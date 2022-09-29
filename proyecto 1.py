import pandas as pd
import matplotlib.pyplot as plt

# Se lee el archivo csv
df = pd.read_csv("Nacional1.csv", index_col=2, squeeze=True)

# 1 Determinar el pico maximo a nivel nacional
print("-" * 25, "Pico maximo a nivel nacional", "-" * 25)
casosNacional = df.iloc[-1:, 1:]
casosNacionalT = casosNacional.transpose()
print(casosNacionalT.loc[casosNacionalT.idxmax()])

# 2 Determianr el % de casos acumulados a nivel nacional
print("-"*25, "% de casos acumulados a nivel nacional", "-"*25)
casosAcom = df.iloc[-1:, 1:].sum(axis=1)
porcentajeCasosAcom = (casosAcom * 100) / df.iloc[-1:, 1]
print(porcentajeCasosAcom)
plt.show()

# 3 Determinar la fecha en donde ocurrio el pico maximo de cada uno de los estados
print("-" * 25, "Pico Maximo de Estados", "-" * 25)
grouped_data = df.groupby('nombre')
print(grouped_data.mean().iloc[:-1, 2:].idxmax(axis=1))

# 4 Determinar el estado con mas casos acomulados
print("-" * 25, "Estado con mas casos acomulados", "-" * 25)
casosAcom = df.iloc[:-1, 2:].sum(axis=1)
print(casosAcom[casosAcom == casosAcom.max()])

# 5 Determinar el estado con el porcentaje mas alto de casos
# acomulados en funcion de la poblacion
print("-" * 25, "Estado con mas % de casos acomulados", "*" * 25)
porcentajaCasosAcom = (casosAcom * 100) / df.iloc[:, 0]
print(porcentajaCasosAcom[porcentajaCasosAcom == porcentajaCasosAcom.max()])

# 6 Determinar el estado con menos casos acomulados
print("-" * 25, "Estado con mas menos acomulados", "-" * 25)
print(casosAcom[casosAcom == casosAcom.min()])

# 7 Determinar el estado con el porcentaje mas bajo de casos
# acomulados en funcion de la poblacion
print("-" * 25, "Estado con menos % de casos acomulados", "-" * 25)
print(porcentajaCasosAcom[porcentajaCasosAcom == porcentajaCasosAcom.min()])
casosAcomNacional = df.iloc[-1:, 1:].cumsum(axis=1)
casosAcomNacionalT = casosAcomNacional.transpose()

# Determinar los estados que comparten una mediana similar
print("-" * 25, "Estados con mediana Similar", "-" * 25)
medianDF = df.iloc[:-1, 2:].median(axis=1)
duplicar = medianDF[medianDF.duplicated(keep=False)]
print(duplicar)

# Determinar los estados que comparten una desviacion estandar similar
print("-" * 25, "Estados con desviacion estandar Similar", "-" * 25)
stdDF = (df.iloc[:-1, 2:].std(axis=1))
duplicar2 = stdDF[stdDF.duplicated(keep=False)]
print(duplicar2)












