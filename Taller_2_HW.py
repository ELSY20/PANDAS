# -*- coding: utf-8 -*-
"""


@author: Elsy

Elsy Yuliana Silgado Rivera
ID: 502194
elsy.silgado@upb.edu.co

"""
#Importamos las librerias
import pandas as pd
from datetime import datetime
import numpy as np

#Implemetamos los datos con su variable
data = pd.DataFrame({'NOMBRE': ['ELSY SILGADO','DEIMER MORELO','JESUS PORTILLO',
                                 'JONNIER TERAN','JONATHAN BRITO','GUSTAVO BLANCO',
                                 'DAYAN HERNANDEZ','WENDY MENDOZA','ALVARO ZAMORA',
                                 'GABRIELA RAMOS','MIGUEL FABRIS','JHONY MELENDEZ',
                                 'ADRIANA SUAREZ','JAIDER ECHEVERRI','NOIVER DARIO RAMOS',
                                 'MIRIAM LOPEZ','IVAN PALENCIA','ANGELA POSSO'],
                     'EDAD': [23,25,21,26,22,26,28,29,21,22,27,26,27,22,26,23,22,27],
                     'SEXO': ['F','M','M','M','M','M','F','F','M','F','M','M',
                              'F','M','M','F','M','F'],
                     'PESO': [64,72,71,75,77,71,63,60,70,62,73,79,60,73,71,67,72,67],
                     'ALTURA': [160,172,171,175,172,160,165,171,178,158,190,150,
                                165,172,176,177,171,174],
                     'DINERO_INVERTIR': [30000000,2000000,4000000,2000000,6000000,30000000,
                                         6000000,3000000,6000000,9000000,14000000,20000000,
                                         42875000,10000000,30000000,3000000,10000000,20000000],
                     'INTERES_ANUAL': [0.04,0.04,0.06,0.06,0.04,0.05,0.06,0.07,0.07,
                                       0.06,0.05,0.05,0.06,0.05,0.06,0.06,0.06,0.07],
                     'ANOS_INVERSION': [1,2,3,3,2,1,1,2,3,3,2,1,1,2,3,3,2,1],
                     'TELEFONO': ['3122569447','3116364059','3123063546','3236665257',
                                  '3027482936','3176765047','3155691850','3001461692',
                                  '3001838809','3232792344','3038615222','3001688142',
                                  '3017510586','3108741997','3343112735','3005459861',
                                  '3008737611','3006792711'],
                     'HORA_COMPRA_PAN':['5:00:00','6:00:00','8:10:00','12:00:00','18:30:00',
                                        '18:00:00','9:00:00','7:15:00','12:20:00','16:30:00',
                                        '20:30:00','8:30:00','15:00:00','8:10:00','14:30:00',
                                        '9:00:00','10:00:00','8:00:00']})

#ejercicio_1
for i in data.index:
    z = round(((data["PESO"][i])/((data["ALTURA"][i])/100)),2)
    print("""Hola {} su masa corporal es: {}""".format(str(data["NOMBRE"][i]),str(z)))
    print("---------------------------------------------------")
    
#ejercicio_2
for i in data.index:
    dinero = round(data["DINERO_INVERTIR"][i]*(((data["INTERES_ANUAL"][i])
                                                 /(100+1))**data["ANOS_INVERSION"][i]),2)
    print("""hola {} su capital a invertir es: {}""".format(str(data["NOMBRE"][i])
                                                                      ,str(dinero)))
    print("---------------------------------------------------")

#ejercicio_3
data["HORAS_HORN"] = ((pd.to_timedelta(data["HORA_COMPRA_PAN"])-pd.to_timedelta("4:00:00")).dt.total_seconds())//3600

c = [
    (data["HORAS_HORN"] >= 4) & (data["HORAS_HORN"]<4),
    (data["HORAS_HORN"] >= 5) & (data["HORAS_HORN"]<6),
    (data["HORAS_HORN"] <= 7) & (data["HORAS_HORN"]<12),
    (data["HORAS_HORN"] <= 10) & (data["HORAS_HORN"]<10)]
s = [0.3, 0.2, 0.1, 0.5]

data["PORC_DESC"] =  np.select(c, s, default='Not Specified')
data["PRECIO"] = 7000-(pd.to_numeric(data["PORC_DESC"], errors='coerce') *7000)
print(data["PRECIO"])

#ejercicio_4
c_ext = [
    (data["SEXO"] == "F"),
    (data["SEXO"] == "M")]
s_ext = [6, 8]


data["EXTENSION_CEL"] = np.select(c_ext, s_ext, default='Not Specified')
print(data["EXTENSION_CEL"])
