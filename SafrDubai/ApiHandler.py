from SafrDubai import HERE_API_KEY, GEOAPIFY_API_KEY
import requests

def transit(origin_lat, origin_lng, dest_lat, dest_lng):
    response = requests.get(f"https://transit.router.hereapi.com/v8/routes?apiKey={HERE_API_KEY}&origin={origin_lat},{origin_lng}&destination={dest_lat},{dest_lng}")
    jsonify = response.json()
    return jsonify

def geocode(query):
    response = requests.get(f"https://geocode.search.hereapi.com/v1/geocode?apiKey={HERE_API_KEY}&q={query}")
    jsonify = response.json()
    if response.status_code == 200:
        latitude = jsonify["items"][0]["position"]["lat"]
        longitude = jsonify["items"][0]["position"]["lng"]
        location = [latitude, longitude]
        return location
    else:
        return "An Error Occurred"a
