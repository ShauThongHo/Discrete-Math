import folium
import pandas as pd
import requests

# Load the CSV file
csv_file = 'tourist_attractions_malaysia.csv'
tourist_attractions_malaysia = pd.read_csv(csv_file)

# Create a map centered around Malaysia
map_malaysia = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Define marker colors based on the type of attraction
marker_colors = {
    "historical site": "blue",
    "natural wonder": "green",
    "amusement park": "red"
}

# Create feature groups for each type of attraction
historical_sites = folium.FeatureGroup(name="Historical Sites")
natural_wonders = folium.FeatureGroup(name="Natural Wonders")
amusement_parks = folium.FeatureGroup(name="Amusement Parks")

# Add markers for each tourist attraction
for index, row in tourist_attractions_malaysia.iterrows():
    marker_color = marker_colors.get(row["type"], "gray")  # Default to gray if type is not found
    popup_text = f"<b>{row['name']}</b><br>Type: {row['type']}"  # Include type information in the popup instead
    marker = folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup_text,
        tooltip=row["name"],
        icon=folium.Icon(color=marker_color)
    )

    # Add marker to the appropriate feature group
    if row["type"] == "historical site":
        historical_sites.add_child(marker)
    elif row["type"] == "natural wonder":
        natural_wonders.add_child(marker)
    elif row["type"] == "amusement park":
        amusement_parks.add_child(marker)

# Add feature groups to the map
map_malaysia.add_child(historical_sites)
map_malaysia.add_child(natural_wonders)
map_malaysia.add_child(amusement_parks)

# Add layer control to toggle different types of attractions on and off
folium.LayerControl().add_to(map_malaysia)

# URL to the GeoJSON file on GitHub
geojson_url = 'https://raw.githubusercontent.com/ShauThongHo/Discrete-Math/6234a8233c3070c2a067fe5cb04fadc0ae284363/malaysia.geojson'

# Fetch the GeoJSON data
response = requests.get(geojson_url)
geojson_data = response.json()

# Add the GeoJSON layer to the map and highlight Malaysia
folium.GeoJson(
    geojson_data,
    name="Malaysia",
    style_function=lambda feature: {
        'fillColor': 'yellow',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.5
    }
).add_to(map_malaysia)

# Save the map to an HTML file
map_malaysia.save("tourist_attractions_malaysia_map_with_customizations.html")

print("Customized interactive map with GeoJSON has been created and saved to 'tourist_attractions_malaysia_map_with_customizations.html'.")