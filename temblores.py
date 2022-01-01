#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame


e = urllib.request.urlopen("http://www.sismologia.cl/ultimos_sismos.html").read()

soup = BeautifulSoup(e, 'html.parser')

# Obtenemos la tabla

tabla_sismos = soup.find_all('table')[0]

# Obtenemos todas las filas
rows = tabla_sismos.find_all("tr")

output_rows = []
for row in rows:
    # obtenemos todas las column
    cells = row.find_all("td")
    output_row = []
    if len(cells) > 0:
        for cell in cells:
            output_row.append(cell.text)
        output_rows.append(output_row)

dataset = pd.DataFrame(output_rows)

dataset.columns = [
    "Fecha Local",
    "Fecha UTC",
    "Latitud",
    "Longitud",
    "Profundidad [Km]",
    "Magnitud",
    "Referencia Geográfica",
]
dataset[["Latitud", "Longitud"]] = dataset[["Latitud", "Longitud"]].apply(pd.to_numeric)

dataset_filter = dataset[
    (-21.655 <= dataset["Latitud"])
    & (dataset["Latitud"] <= -19.370)
    & (-72.316 <= dataset["Longitud"])
    & (dataset["Longitud"] <= -68.426)
]



df = pd.read_csv("data_iqq.csv") #leer archivo data.csv


con = pd.concat([dataset_filter,df]).astype({"Profundidad [Km]":float, "Latitud":float}) # concatenar dataset_filter y df, ademas cambia string a float las columnas Profundidad [Km] y Latitud

con = con.drop_duplicates()

con.to_csv("data_iqq.csv",  index=None) # crear csv con archivos concatenados

df1 = pd.read_csv("data_iqq.csv") #leer archivo data.csv

df1["Magnitud"].str.split('').astype(str) #separar magnitud en 2 columnas

split_datos = df1["Magnitud"].str.split(' ', expand=True) #separar magnitud en 2
split_datos.columns = ['magnitud', 'letras'] #crear 2 columnas valores y letras
con2 = pd.concat([df1, split_datos], axis=1) #concatenar datos del csv con las 2 columnas nuevas.


con2.to_csv("data_iquique.csv",  index=None) # crear nuevo csv con archivos concatenados
