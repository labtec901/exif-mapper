import folium
from GPSPhoto import gpsphoto
import os
import pandas as pd
import pathlib
import logging
import time

# Set logging
logging.basicConfig(handlers=[logging.FileHandler("exif_mapping.log"), logging.StreamHandler()],
                    format='%(asctime)s | %(levelname)s: %(message)s', level=logging.INFO)

#path = r"""C:\Users\Labtec\Camera Uploads"""
path = input("Enter the path to the folder of images you wish to extract GPS data from: ")

# Create a list of all the images in the folder, and extract the GPS data from each
df = pd.DataFrame(columns=['Image', 'Image_Path', 'latitude', 'longitude', 'altitude_meters', 'altitude_feet'])
for imageName in os.listdir(path):
    inputPath = os.path.join(path, imageName)
    try:
        data = gpsphoto.getGPSData(inputPath)
        # print(data)
        if data:
            #Blanks for the altitude in meters and feet.  This works for some images, but not all.
            df.loc[len(df.index)] = [imageName, inputPath, data['Latitude'], data['Longitude'], 0, 0 / 0.3048]
            logging.debug('Got GPS Data For: ' + imageName)
    except:
        logging.warning('Failed to Get GPS Data For: ' + imageName)
        pass

USA_center = [39.8283, -98.5795] #lat and long of center of USA

# Create the map

my_map = folium.Map(location=USA_center, zoom_start=5)

folium.TileLayer('openstreetmap', attr=".").add_to(my_map)
folium.TileLayer('stamentonerbackground', attr=".").add_to(my_map)
folium.LayerControl().add_to(my_map)


markers_added = 0
for _, r in df.iterrows():
    lat = r['latitude']
    lon = r['longitude']
    path = r["Image_Path"]
    image = r["Image"]


    folium.CircleMarker(fill=True, location=[lat, lon],
                        popup=folium.Popup(
                            f'<a href="https://www.google.com/maps/search/?api=1&query={lat},{lon}" target="_blank">{image}</a> <a href="file:///{pathlib.PureWindowsPath(path).as_posix()}" target="_blank"><img src="file:///{pathlib.PureWindowsPath(path).as_posix()}" width=450px>',
                            lazy=True),
                        ).add_to(my_map)
    markers_added += 1
    if markers_added % 500 == 0:
        logging.info(str(markers_added) + ' Markers Added')

logging.info(str(markers_added) + ' Markers Added')
# Display the map
my_map.save("exifmap.html")
logging.info('Map Created')
time.sleep(5)
