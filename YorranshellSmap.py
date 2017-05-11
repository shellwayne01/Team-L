#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:41:13 2017

@author: yorranshellwattson
"""
import folium
import pandas as pd

#Yorranshell's Subway Map
Ridership = pd.read_csv('AnnualRidership.csv')
mapRidership = folium.Map(location=[40.723565, -73.965325],tiles="Cartodb Positron",zoom_start=13)

#Retrieves data from csv
for index, row in Ridership.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    line = row["Line"]
    station = row["Station"]
    name = line + ' train at ' + station
  
    #Add markers to the map:
    if line == "L":
        folium.CircleMarker([lat,lon], popup = name, color= 'gray', fill_color='gray', radius=50).add_to(mapRidership)
    if line == "G":
        folium.CircleMarker([lat,lon], popup = name, color= 'green', fill_color='green', radius=50).add_to(mapRidership)
    if line == "M":
        folium.CircleMarker([lat,lon], popup = name, color= 'brown', fill_color='brown', radius=50).add_to(mapRidership)
        
mapRidership.save(outfile='YorranshellSmap.html')