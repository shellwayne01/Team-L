#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:56:05 2017

@author: yorranshellwattson
"""
import json
import folium
import pandas as pd

coords = []
popups = []
icons = []

mapSub = folium.Map(location=[	40.7302, -73.9541],tiles="Cartodb Positron",zoom_start=13)
Subway = pd.read_csv('train.csv')

mapSub.choropleth(geo_path='M train.geojson',
                    line_color='#FF6319', fill_opacity=0.9, line_opacity= 1,line_weight=4
                    )
mapSub.choropleth(geo_path='G train.geojson',
                    line_color='#6CBE45', fill_opacity=0.9, line_opacity= 1,line_weight=4
                    )
mapSub.choropleth(geo_path='L train.geojson',
                    line_color='#A7A9AC', fill_opacity=0.9, line_opacity= 1,line_weight=4
                    )
with open('NormalSubway.geojson') as f:
    stations = json.load(f)


for feature in stations['features']:
    lon, lat = feature['geometry']['coordinates']
    icon_url = feature['properties']['Icon Url']
    stationName = feature['properties']['Station']
    line = feature['properties']['Line'] 
    popup =  line + " train at " + stationName   #Adds popup
    icon = folium.features.CustomIcon(icon_url,
                                      icon_size=(30, 30)) 

    marker = folium.map.Marker([lat, lon], popup=popup, icon=icon)
    mapSub.add_children(marker)
        
mapSub.save(outfile='trainIcons.html')

'''
#This method wasn't working for multiple data points so I used the geojson method instead
logoG_url = 'http://images.huffingtonpost.com/2015-11-05-1446691135-8331886-G_Train_logo.png'
logoM_url = 'https://2.bp.blogspot.com/-h8OPSVh1JvY/Vu914_VbilI/AAAAAAAA-qQ/gZCTNi7c_HQCCN8ln1Rjr9-1soj3pPY6Q/s1600/M%2Btrain.png'
logoL_url = 'http://wheresthel.com/images/ltrain.png'

iconG = folium.features.CustomIcon(logoG_url, icon_size=(50, 50))
iconM = folium.features.CustomIcon(logoM_url, icon_size=(50, 50))
iconL = folium.features.CustomIcon(logoL_url, icon_size=(50, 50))


for index, row in Subway.iterrows():
    if (row['Line'] == "G" or row['Line'] == "L" or row['Line'] == "M"):    
        lat = row['Latitude']
        lon = row['Longitude']
        name = row['Line'] + ' train at ' + row['Station']
        coords.append([lat,lon])
        
        if(row['Line'] == "G"):
             folium.Marker([lat,lon],popup = name, icon = iconG).add_to(mapSub) 
        elif(row['Line'] == "M"):
             folium.Marker([lat,lon],popup = name, icon = iconM).add_to(mapSub)
        elif(row['Line'] == "L"):
             folium.Marker([lat,lon],popup = name, icon = iconL).add_to(mapSub)

mapSub.save(outfile='failedIcons.html')
''' 
