#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:12:01 2017

@author: yorranshellwattson
"""
import folium
import pandas as pd

#Pretty Map 
#CHANGE THE ICONS to mta icons
#ADD geojson
libs = pd.read_csv('AnnualRidership.csv')

coords = []
popups = []
icons = []
mapVor = folium.Map(location=[40.75, -73.9],tiles="Cartodb Positron",zoom_start=13)

for index, row in libs.iterrows():
    if (row['Line'] == "G" or row['Line'] == "L" or row['Line'] == "M"):    
        lat = row['Latitude']
        lon = row['Longitude']
        name = row['Line'] + ' train at ' + row['Station']
        coords.append([lat,lon])
        
        if(row['Line'] == "G"):
             folium.Marker([lat,lon],popup = name, icon = folium.Icon(color='green')).add_to(mapVor)
        elif(row['Line'] == "M"):
             folium.Marker([lat,lon],popup = name, icon = folium.Icon(color='orange')).add_to(mapVor)
        elif(row['Line'] == "L"):
             folium.Marker([lat,lon],popup = name, icon = folium.Icon(color='gray')).add_to(mapVor)
        
mapVor.save(outfile='beforeTrain.html')
