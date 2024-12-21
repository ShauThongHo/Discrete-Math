import streamlit as st
from streamlit_folium import st_static
import requests
import folium

    # List of tourist attractions in Malaysia with their coordinates and types
tourist_attractions_malaysia = [
        {"name": "Petronas Twin Towers", "latitude": 3.1578, "longitude": 101.7123, "type": "natural wonder"},
        {"name": "Batu Caves", "latitude": 3.2379, "longitude": 101.6831, "type": "historical site"},
        {"name": "Mount Kinabalu", "latitude": 6.0750, "longitude": 116.5580, "type": "natural wonder"},
        {"name": "George Town", "latitude": 5.4141, "longitude": 100.3288, "type": "historical site"},
        {"name": "Langkawi Sky Bridge", "latitude": 6.3810, "longitude": 99.6653, "type": "natural wonder"}
    ]

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
for attraction in tourist_attractions_malaysia:
        marker_color = marker_colors.get(attraction["type"], "gray")  # Default to gray if type is not found
        popup_text = f"<b>{attraction['name']}</b><br>Type: {attraction['type']}"  # Include type information in the popup instead
        marker = folium.Marker(
            location=[attraction["latitude"], attraction["longitude"]],
            popup=popup_text,
            tooltip=attraction["name"],
            icon=folium.Icon(color=marker_color)
        )
        
        # Add marker to the appropriate feature group
        if attraction["type"] == "historical site":
            historical_sites.add_child(marker)
        elif attraction["type"] == "natural wonder":
            natural_wonders.add_child(marker)
        elif attraction["type"] == "amusement park":
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
map_html = "tourist_attractions_malaysia_map_with_customizations.html"
map_malaysia.save(map_html)

    # Display the map in Streamlit
st.title("Tourist Attractions in Malaysia")
st.write(f"Total number of attractions: {len(tourist_attractions_malaysia)}")
st.write("Map with customizations:")
st.write("")
st.components.v1.html(open(map_html).read(), height=600, width=800)