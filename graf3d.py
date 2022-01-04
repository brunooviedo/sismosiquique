import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import pandas as pd

# leer archivo csv
df = pd.read_csv("data_iquique.csv")


# crear figura extrallendo los datos de csv, latitud, longitud y profundidad [km], agregar color de acuerdo a la columna magnitud, y crear escala de color
fig = px.scatter_3d(df, x = 'Latitud', y = 'Longitud', z='Profundidad [Km]', color='magnitud',
                    color_continuous_scale=["blue", "green", "red"], title="Grafica de Profundidad")
# se da estilo al grafico
fig.update_traces(marker=dict(size=5,
                         line=dict(width=5,
                         color='Black')),
              selector=dict(mode='markers'))

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=6),
                     zaxis = dict(nticks=4, range=[300,0],),),) #se agrega rango al eje z
    # margin=dict(r=20, l=10, b=10, t=10)) #margen interno del grafico 3D
    
    # grafica de magnitud
    
#se vcrea la figura 2
fig2 = px.scatter(df, x='Fecha Local', y="magnitud", color='magnitud',
                  color_continuous_scale=["blue", "green", "red"], title="Grafica de Magnitud")
#estilo de la figura 2
fig2.update_traces(marker=dict(size=8,
                         line=dict(width=1,
                         color='Black')),
              selector=dict(mode='markers'))

#se imprime los graficos
# fig.show()
# fig2.show()
#se guardan en hml los graficos
fig.write_html("templates/graf3d.html")
fig2.write_html("templates/magnitud.html")

#