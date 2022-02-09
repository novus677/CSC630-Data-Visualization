import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
import json

df = pd.read_csv('traffic_data_2020.csv')
this_map = folium.Map(location=[42.1282, -71.3824], zoom_start=8)

records = df[['latitude', 'longitude']].to_records()

this_map = this_map = folium.Map(location=[42.1282, -71.3824], zoom_start=8)

for record in records:
    folium.CircleMarker(location=[record[1], record[2]], radius=1, weight=3).add_to(this_map)

with open('traffic_data_2020_animation.geojson') as j:
    data = json.load(j)
    
for i in range(len(data['features'])):
    data['features'][i]['properties']['times'] = [data['features'][i]['properties']['date']]

this_map = folium.Map(location=[42.1282, -71.3824], zoom_start=8)
TimestampedGeoJson(data, transition_time=20).add_to(this_map)

this_map.save('traffic_data_2020_animation.html')