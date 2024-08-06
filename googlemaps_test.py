import gmplot

# Create a map object centered around a specific location
gmap = gmplot.GoogleMapPlotter(37.7749, -122.4194, 13)

# Draw the map
gmap.draw(r"d:\my_gmap.html")

gmap.marker(37.7749, -122.4194, title="San Francisco")

# Draw the map
gmap.draw(r"d:\my_gmap_with_markers.html")

