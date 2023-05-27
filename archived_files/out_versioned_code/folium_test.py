# !pip install folium

# +
import folium
import pandas as pd

# Create a map centered around London
map_london = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Iterate over the data and add markers to the map
for index, row in df_selected.iterrows():
    # Extract the latitude and longitude
    lat = row['latitude']
    lon = row['longitude']
    
    # Create a marker with a popup
    marker = folium.Marker(location=[lat, lon])
    
    # Add the marker to the map
    marker.add_to(map_london)
    
# Display the map inline in Jupyter Notebook
map_london
