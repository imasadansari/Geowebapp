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
fg_volcano = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg_volcano.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color=color_producer(el))))

# crating next layer of population
fg_population = folium.FeatureGroup(name="Population")

fg_population.add_child(folium.GeoJson(data= open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 3500000 
else 'orange' if 3500000 <= x['properties']['POP2005'] <= 10000000  else 'red'}))

# Add layer to map
map.add_child(fg_volcano)
map.add_child(fg_population)

# Add Layer Controler
# keep in mind to add it after adding layers else it wont work
map.add_child(folium.LayerControl())

# save map
map.save("Map.html")