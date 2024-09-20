#This code generates random meteorological data and displays it in 5 different images


import folium
import webbrowser
import random
import time

#I tried do use APIs like OpenWeatherApp and MeteoStat but the creation of account led to fatal
# issues every time. That's why I rewrote the code to generate random data of "raininess" in predefined locations
def get_precipitation_data():
    locations = [
        {'city': 'New York', 'lat': 40.7128, 'lon': -74.0060},
        {'city': 'Los Angeles', 'lat': 34.0522, 'lon': -118.2437},
        {'city': 'Chicago', 'lat': 41.8781, 'lon': -87.6298},
        {'city': 'Miami', 'lat': 25.7617, 'lon': -80.1918},
        {'city': 'Dallas', 'lat': 32.7767, 'lon': -96.7970}
    ]
    # Assigning random precipitation values in mm
    for location in locations:
        location['precipitation'] = random.uniform(0, 100)

    return locations


# Function to build a real-time precipitation map
def build_precipitation_map(locations):
    # Creating a Folium map centered
    precipitation_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Choosing the symbols used for rain by giving an URL
    raindrop_icon_url = 'https://cdn-icons-png.flaticon.com/128/672/672808.png'

    # Adding markers to the map for each location with precipitation data under the icon
    for loc in locations:
        html = f"""
     <div style="text-align: center;">
     <img src="{raindrop_icon_url}" style="width:30px;height:30px;"><br> 
     <span>{loc['precipitation']:.2f} mm</span>
     </div>
     """
        folium.Marker(
            location=[loc['lat'], loc['lon']],
            icon=folium.DivIcon(html=html)
        ).add_to(precipitation_map)

    return precipitation_map


#Creating 10 different states of the weather to cycle through them and simulate updates of the data
def real_time_precipitation_updates():
    for i in range(10):  # Simulate 5 real-time updates
        print(f"Update {i + 1}")
        locations = get_precipitation_data()
        precipitation_map = build_precipitation_map(locations)

        # Saving the map
        map_filename = f"precipitation_map_update_{i + 1}.html"
        precipitation_map.save(map_filename)

        # Display the generated map within the web browser
        webbrowser.open(map_filename, new=2)

        # Adding delay to give a updating data impression
        time.sleep(1)


# Run the real-time precipitation updates
real_time_precipitation_updates()

#I wanted to delete the previous browser tabs when a new one is
#open but I couldn't find a way to do it within Python