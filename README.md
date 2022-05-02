# exif-mapper

Surprisingly, there doesn't seem to be any effective free way of plotting folders of geotagged images on a map.  Adobe Lightroom can sort of do it, and some random payware apps can do it poorly, but I wasn't able to find anything I wanted, so I made this.

This short script takes a folder or folder tree which contains geotagged images, and extracts the latitude and longitude GPS coordinates, and then plots these points on a leaflet map, including on-click popups to preview the image, see the image's name, and open the image location in Google Maps as well.

### Popup functionality
![2022-05-02_14-12-43_chrome](https://user-images.githubusercontent.com/11169730/166328499-469c79bc-44b6-430f-9f22-19cf54d64c40.png)
### Plotting lots of points
![2022-05-02_14-20-23_chrome](https://user-images.githubusercontent.com/11169730/166329500-60236f20-cce9-490e-9287-c65fe9317bde.png)


## Important!

* This script requires the folium, GPSPhoto, and pandas python packages.
* This script uses an *in development* function of folium, which as of this writing is still part of an open pull request which you can see [here](https://github.com/python-visualization/folium/pull/1511).  **You must replace the default folium/map.py file from your pip-installed folium instance with the one given in this pull request**.  This additional function prevents your browser from crashing when it tries to load every pop-up image at once when the page loads.  Using this tweak I can generate maps of more than 11,000 photos, which will instantly crash your browser without this change.
