# import Libraries
import folium
import pandas

# import data/ load data
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# Color of Icon 
def color_producer(elevation):
    if elevation <= 1000:
        return 'green'
    elif elevation <= 3000:
        return 'orange'
    else:
        return 'red'

# Html 
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location= [38.50, -99.09], zoom_start= 5, tiles="Stamen Terrain")

# Creating layer 1
# fg = feature group
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color=color_producer(el))))

# Add layer to map
map.add_child(fg)

# save map
map.save("Map.html")