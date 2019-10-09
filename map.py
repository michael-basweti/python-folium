import folium
import os
import json

# create map object
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Global tooltip
tooltip='Click for more'

# vis data
vis = os.path.join('data', 'vis.json')

# overlay
overlay = os.path.join('data', 'overlay.json')
# logIcon
logoIcon=folium.features.CustomIcon('habiba.jpg',icon_size=[50,50])
# add markers
folium.Marker([42.363600, -71.099500],
                popup='<strong>Location One</strong>',
                tooltip=tooltip).add_to(m),
folium.Marker([42.333600, -71.109500],
                popup='<strong>Location One</strong>',
                tooltip=tooltip,
                icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([42.323600, -71.199500],
                popup='<strong>Location One</strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m),

folium.Marker([42.343600, -71.189500],
                popup='<strong>Location One</strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m),

folium.Marker([42.360000, -71.188500],
                popup='<strong>Location One</strong>',
                tooltip=tooltip,
                icon=logoIcon).add_to(m),

folium.Marker([42.350000, -71.188500],
                popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),width=450, height=250))).add_to(m),

folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup="Brad's birth place",
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m),

folium.GeoJson(overlay, name='Cambridge').add_to(m)

# generate map
m.save('map.html')