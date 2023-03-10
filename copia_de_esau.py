# -*- coding: utf-8 -*-
"""Copia de ESAU.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16fnNznzyMgF1PY89V38LLWHauFSs9MZT
"""

# from google.colab import drive
# drive.mount('/content/drive/', force_remount=True)
# base = "/content/drive/MyDrive/ESAU/"

import pandas as pd
import numpy as np

nombre_archivo = "Escalas.xlsx"
sheets = None
df = pd.read_excel(nombre_archivo, sheet_name=sheets) #trying out first 3 pages

nombres_hojas = []
for key, _ in df.items():
  # print(key)
  nombres_hojas.append(key)

df_hoja = []

with pd.ExcelWriter(f'output_{nombre_archivo.split(".xlsx")[0]}.xlsx') as writer:
  for num_hoja in nombres_hojas:
# num_hoja = "12049-SAN LUIS POTOSI - NUEV(Y)"
    vigente_desde = df[num_hoja].columns[0]
    # print(f"{vigente_desde}")
    tipo_escala = df[num_hoja].iloc[2,0].split(" ")[-1]
    tipo_moneda = df[num_hoja].iloc[3,0].split(" ")[-1]
    tipo_viaje =  df[num_hoja].iloc[4,0].split(" ")[-1]
    tipo_tarifa =  df[num_hoja].iloc[5,0].split(" ")[-1]

    ruta =  df[num_hoja].iloc[7,0].split(" ")[2]
    tipo_servicio =  " ".join(df[num_hoja].iloc[8,0].split(" ")[3:])
    # print(tipo_escala, tipo_viaje, tipo_tarifa, ruta, tipo_servicio)
    ciudades = []
    # display(df[num_hoja])
    number_of_rows = df[num_hoja][df[num_hoja].iloc[:,0].isnull() ].index[-1]
    for column in range(len(df[num_hoja].columns)):
      # print(num_hoja)
      ciudad =  df[num_hoja].iloc[column+10,column]
      ciudades.append(ciudad)
      # print(ciudad)
      ### pone nombres de ciudades en NaNs
      df[num_hoja].iloc[column+10,column] = np.nan

    triang_izq = df[num_hoja].iloc[11:11+len(ciudades)-1]

    triang_izq = triang_izq.reset_index().drop(columns="index").rename(columns=dict(zip(triang_izq.columns,ciudades)))
    #
    triang_izq.loc[triang_izq.shape[0]] = [np.nan for col in triang_izq.columns]
    triang_izq = triang_izq.shift(1)
    triang_izq.index = ciudades
    # 
        
    triang_der = triang_izq.T
    triang_izq = triang_izq.fillna(0)
    triang_der = triang_der.fillna(0)

    triang_der.columns = [col.split("   ")[0] for col in triang_der.columns]

    df_sheet = pd.DataFrame(triang_izq.values + triang_der.values, columns=triang_der.columns)
    df_sheet.index = [col.split("   ")[0] for col in triang_der.columns]

    data = df_sheet[df_sheet >= 0].stack().index.tolist()
    df_form = pd.DataFrame(data, columns =['IDA', 'VUELTA'])
    df_form["PRECIO"] = df_sheet[df_sheet >= 0].stack().tolist() 
    # df_form
        # df_hoja.append(df_form)
        
    df_form.to_excel(writer, sheet_name=num_hoja)

  # for num, df_form in enumerate(df_hoja):
    # df_form.to_excel(writer, sheet_name=num_hoja)
  # num_hoja = '98760-ZARAGOZA, NL - MONTERR(S)'







"""#Paso a paso

"""

import pandas as pd
import numpy as np

df = pd.read_excel("Escalas.xlsx", sheet_name=None) #trying out first 3 pages
#

nombres_hojas = []
for key, _ in df.items():
  # print(key)
  nombres_hojas.append(key)

# num_hoja = '98760-ZARAGOZA, NL - MONTERR(S)'

vigente_desde = df[num_hoja].columns[0]
print(f"{vigente_desde}")
tipo_escala = df[num_hoja].iloc[2,0].split(" ")[-1]
tipo_moneda = df[num_hoja].iloc[3,0].split(" ")[-1]
tipo_viaje =  df[num_hoja].iloc[4,0].split(" ")[-1]
tipo_tarifa =  df[num_hoja].iloc[5,0].split(" ")[-1]

ruta =  df[num_hoja].iloc[7,0].split(" ")[2]
tipo_servicio =  " ".join(df[num_hoja].iloc[8,0].split(" ")[3:])
tipo_escala, tipo_viaje, tipo_tarifa, ruta, tipo_servicio

### get diagonal names
# num_hoja = 1
ciudades = []
for column in range(len(df[num_hoja].columns)):
  ciudad =  df[num_hoja].iloc[column+10,column+0]
  ciudades.append(ciudad)
  # print(ciudad)
  ### pone nombres de ciudades en NaNs
  df[num_hoja].iloc[column+10,column+0] = np.nan

len(ciudades)

ciudades

triang_izq = df[num_hoja].iloc[11:11+len(ciudades)-1]

triang_izq

triang_izq = triang_izq.reset_index().drop(columns="index").rename(columns=dict(zip(triang_izq.columns,ciudades)))
triang_izq

triang_izq.loc[triang_izq.shape[0]] = [np.nan for col in triang_izq.columns]
triang_izq = triang_izq.shift(1)
triang_izq.index = ciudades
triang_izq

triang_der = triang_izq.T#shift(-1)
# for column in range( len(triang_der.columns)):
#   triang_der.iloc[column+0,column+0] = np.nan

triang_izq.T.shape, triang_der.shape

triang_der = triang_izq.T
triang_izq = triang_izq.fillna(0)
triang_der = triang_der.fillna(0)

triang_izq.reset_index().drop(columns="index").rename(columns=dict(zip(triang_izq.columns,ciudades)))

triang_der = triang_izq.T
triang_izq = triang_izq.fillna(0)
triang_der = triang_der.fillna(0)

triang_der.columns = [col.split("   ")[0] for col in triang_der.columns]

df_sheet = pd.DataFrame(triang_izq.values + triang_der.values, columns=triang_der.columns)
df_sheet.index = [col.split("   ")[0] for col in triang_der.columns]
df_sheet

data = df_sheet[df_sheet >= 0].stack().index.tolist()

data = df_sheet[df_sheet >= 0].stack().index.tolist()
df_form = pd.DataFrame(data, columns =['IDA', 'VUELTA'])
df_form["PRECIO"] = df_sheet[df_sheet >= 0].stack().tolist()

df_form



# df_form["TRAMO"] =

# df_sheet[df_sheet >= 0].stack().index.tolist()
dict(zip(df_sheet[df_sheet >= 0].stack().index.tolist(),df_sheet[df_sheet >= 0].stack().tolist()))

import numpy as np

import pandas as pd
a = pd.Series([10, 20, 30])
print(a)
a = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(a)
a = pd.Series([10, 20,np.nan])
print(a)
type(a)





"""# Secci??n nueva

Importa Pandas.Numpy, Matplotlib.pyplot.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Define el Basepath a C:\Users\esvelazquez\Documents\6. Noviembre-2022\Federal\BOT"""

basepath = "/content/"

"""Define los nombre de los archivos en cuestion """

archivo1 = basepath + "/Todos (26-10 a 01-11).xlsx"
archivo2 = basepath + "/Monitoreo Competencia 19-Oct 25-Oct-2022 Historico.xlsx"

"""Cargar el archivo a 3 dataframes"""

dfbd = pd.read_excel (archivo1, sheet_name = "BD") 
dfcveorg = pd.read_excel (archivo2, sheet_name = "CVE Ciud")
dfserv = pd.read_excel (archivo2, sheet_name = "T.Serv")
dftarifa = pd.read_excel (archivo2, sheet_name = "Tarifas SENDA")

dfbd

"""Agregar tablas a mi df

% Desc 
Clave Origen
Clave Destino
Tipo de Servicio
Cantidad de Corridas
Concatenado Tarifas
Tarifa Base Senda
Horas Redondeadas
Empresa Hora
"""

dfbd ["%Desc"] =(( dfbd["preciofinal"]/ dfbd["precio"]) -1)*100

merged_inner = pd.merge(left=dfbd, right=dfcveorg, how="left", left_on = "origen", right_on="origen")

merged_inner.head()

"""Tabla Dinamica


"""

tdinamica = dfbd.groupby(["asientosOcupados"]).sum()

"""Tabla dinamica """

tdinamica = pd.pivot_table(dfbd, index= "competidor", columns= "fecha salida", values= "asientosOcupados")

print(tdinamica)

"""Grafica de Pivot """

Totalocupacion = tdinamica[("competidor","fechasalida")]

output.plot(kind = "bar")
plt.show()

