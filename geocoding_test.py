import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='YOUR_API_KEY')

# גיאוקודינג ישיר
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

if geocode_result:
    location = geocode_result[0]['geometry']['location']
    print(f"קואורדינטות: {location['lat']}, {location['lng']}")

    # גיאוקודינג הפוך
    reverse_geocode_result = gmaps.reverse_geocode((location['lat'], location['lng']))

    if reverse_geocode_result:
        address = reverse_geocode_result[0]['formatted_address']
        print(f"כתובת: {address}")
else:
    print("לא נמצאו תוצאות")

# חיפוש מקומות בקרבת מקום
places_result = gmaps.places_nearby(location=location, radius=1000, type='restaurant')

if places_result['results']:
    print("\nמסעדות בקרבת מקום:")
    for place in places_result['results'][:5]:  # הצגת 5 התוצאות הראשונות
        print(f"- {place['name']}")
