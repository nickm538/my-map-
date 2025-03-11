import folium
import pandas as pd
import os

# Sample data for Long Island townships (replace with actual data)
townships = [
    'Hempstead', 'North Hempstead', 'Oyster Bay', 'Glen Cove', 'Long Beach',
    'Brookhaven', 'Islip', 'Babylon', 'Huntington', 'Smithtown',
    'Southampton', 'Riverhead', 'East Hampton', 'Shelter Island', 'Southold'
]
levels = [0.8, 0.4, 0.3, 0.5, 0.2, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.6, 0.3, 0.1, 0.2]
df = pd.DataFrame({'Township': townships, 'Level': levels})

# Create a map centered on Long Island
m = folium.Map(location=[40.7, -73.6], zoom_start=10)

# Add the choropleth layer for the heatmap
folium.Choropleth(
    geo_data='tl_rd22_36_cousub.geojson',  # Path to your GeoJSON file
    name='choropleth',
    data=df,
    columns=['Township', 'Level'],
    key_on='feature.properties.NAME',  # Adjust based on your GeoJSON's property name
    fill_color='YlOrRd',  # Yellow to Red: light (low) to dark (high)
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Homelessness/Poverty Level (Percentage of Population)'
).add_to(m)

# Save the map as an interactive HTML file
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
m.save(os.path.join(output_dir, 'heatmap.html'))