#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:12:01 2017

@author: yorranshellwattson
"""
import folium
import pandas as pd

Ridership = pd.read_csv('AnnualRidership.csv')
mapRidership = folium.Map(location=[40.723565, -73.965325],tiles="Cartodb Positron",zoom_start=13)

#Retrieves data from csv
for index, row in Ridership.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    line = row["Line"]
    station = row["Station"]
    #info = station + line  #/n maybe? GET THIS TO WORK
  
    #Add markers to the map:
    if line == "L":
        folium.CircleMarker([lat,lon], popup = line, radius = 150, fill_color="gray").add_to(mapRidership)
    if line == "G":
        folium.CircleMarker([lat,lon], popup = line, radius = 150, fill_color="green").add_to(mapRidership)
    if line == "M":
        folium.CircleMarker([lat,lon], popup = line, radius = 150, fill_color="orange").add_to(mapRidership)
        
mapRidership.save(outfile='AnnualRidership.html')
