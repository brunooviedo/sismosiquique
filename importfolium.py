import folium
from folium import Map
from folium.map import Popup
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import pandas as pd


  # Creating a more organized map using clusters
mapa = folium.Map([-20.214066, -70.152465], zoom_start=6,  tiles='Stamen Terrain',)

# leer el archivo csv que contiene los datos de localización
data = pd.read_csv('data_iquique.csv')

df = data.head(300)

tooltip = "Iquique"



def generate_popup(Hora, magnitud, Profundidad, referencia):
    return f'''<strong>Hora Local:</strong><br> {Hora}<br><strong>magnitud:</strong> {magnitud}<br><strong>Profundidad:</strong> {Profundidad} <strong>Referencia:</strong>{referencia}'''

def generate_color(magnitud):
    if magnitud <= 3:
        c_outline, c_fill = '#008f39', '#008f39'
        m_opacity, f_opacity = 0.7, 0.6
    elif magnitud <= 5:
        c_outline, c_fill = '#ffda79', '#ffda79'
        m_opacity, f_opacity = 0.7, 0.6
    else:
        c_outline, c_fill = '#c0392b', '#e74c3c'
        m_opacity, f_opacity = 1, 1
    return c_outline, c_fill, m_opacity, f_opacity

mc = MarkerCluster()

for _, row in df.iterrows():
# for i in range(len(data)):
    # c_outline, c_fill, m_opacity, f_opacity = generate_color(row['Magnitud'])
    # folium.Circle(
    #     popup = generate_popup(row ['Fecha Local'],row ['Magnitud'], row['Profundidad [Km]'], row['Referencia Geográfica']),
    #     color=c_outline,  # this is the color of the border
    #     fill=True,
    #     fill_color=c_fill,  # fill is inside the circle
    #     opacity=m_opacity,  # this is the alpha for the border
    #     fill_opacity=f_opacity,  # we will make that less opaque so we can see layers
    #     radius=(row['Magnitud'] ** 6) / 3)
    
    mc.add_child(folium.Marker(
        location=[str(row['Latitud']),
        str(row['Longitud'])],
        popup = generate_popup(row ['Fecha Local'],row ['magnitud'], row['Profundidad [Km]'], row['Referencia Geográfica']),
        clustered_marker=True))
    
mapa.add_child(mc)


    
mapa1 = folium.Map([-20.214066, -70.152465], zoom_start=7,  tiles='Stamen Terrain',)

for _, row in df.iterrows():
# for i in range(len(data)):
        c_outline, c_fill, m_opacity, f_opacity = generate_color(row['magnitud'])
        folium.Circle(
            location=[row['Latitud'], row['Longitud']],
            popup = generate_popup(row ['Fecha Local'],row ['magnitud'], row['Profundidad [Km]'], row['Referencia Geográfica']),
            color=c_outline,  # this is the color of the border
            fill=True,
            fill_color=c_fill,  # fill is inside the circle
            opacity=m_opacity,
            weight= 15,# this is the alpha for the border
            fill_opacity=f_opacity,  # we will make that less opaque so we can see layers
            radius=(row['magnitud'] ** 5) 
        
    ).add_to(mapa1)
        

folium.Marker(
    [-24.397486, -69.161143], popup="<i>Coordenadas Tranque -24.397486, -72.161143</i>",
    icon=folium.Icon(color="red",icon="home", prefix='fa'),
    tooltip=tooltip
).add_to(mapa1)

mapa2 = folium.Map([-20.214066, -70.152465], zoom_start=7,  tiles='Stamen Terrain',)



# Your code here: Add a heatmap to the map
HeatMap(data=data[['Latitud', 'Longitud']], radius=15).add_to(mapa2)

folium.Circle(
    radius=200000,
    location=[-24.397486, -69.161143],
    popup="Radio de 200 Kilometros",
    color="red",
    #fill=True,
    opacity=0.5,
    #fill_opacity=0.1,
    #fill_color="red",
).add_to(mapa)

folium.Circle(
    radius=300000,
    location=[-24.397486, -69.161143],
    popup="Radio de 300 Kilometros",
    color="yellow",
    #fill=True,
    opacity=0.5,
    #fill_opacity=0.1,
    #fill_color="yellow",
).add_to(mapa)

folium.Marker(
    [-24.397486, -69.161143], popup="<i>Coordenadas Tranque -24.397486, -72.161143</i>",
    icon=folium.Icon(color="red",icon="home", prefix='fa'),
).add_to(mapa)

folium.Circle(
    radius=200000,
    location=[-24.397486, -69.161143],
    popup="Radio de 200 Kilometros",
    color="red",
    #fill=True,
    opacity=0.5,
    #fill_opacity=0.1,
    #fill_color="red",
).add_to(mapa1)
folium.Circle(
    radius=300000,
    location=[-24.397486, -69.161143],
    popup="Radio de 300 Kilometros",
    color="yellow",
    #fill=True,
    opacity=0.5,
    #fill_opacity=0.1,
    #fill_color="yellow",
).add_to(mapa1)

folium.Circle(
    radius=200000,
    location=[-24.397486, -69.161143],
    popup="Radio de 200 Kilometros",
    color="red",
    #fill=True,
    opacity=0.5,
    #fill_opacity=0.1,
    #fill_color="red",
).add_to(mapa2)
folium.Circle(
    radius=300000,
    location=[-24.397486, -69.161143],
    popup="Radio de 300 Kilometros",
    color="yellow",
    #fill=True,
    opacity=0.5,
    #fill_opacity=0.1,
    #fill_color="yellow",
).add_to(mapa2)
 
        
mapa1.save('templates/mapa.html')
mapa.save('templates/areas.html')
mapa2.save('templates/head.html')
