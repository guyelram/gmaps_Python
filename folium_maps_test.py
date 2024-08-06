
import folium

# create map
map = folium.Map(location=[31.7767, 35.2345], zoom_start=7)

# save map as html file
map.save(r"D:\my_map.html")

folium.Marker (
    location=[32.0853, 34.7818],
    popup="תל אביב",
    tooltip="לחץ כאן").add_to(map)

map.save(r"d:\tel_aviv_map.html")
