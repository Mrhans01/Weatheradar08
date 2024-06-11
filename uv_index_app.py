import requests

API_KEY = 'c62ce4cc8162aedbe2780c0527631ce5'

def get_uv_index(latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/uvi?lat={latitude}&lon={longitude}&appid={API_KEY}"
    response = requests.get(url)

    try:
        uv_data = response.json()
        uv_index = uv_data['value']
    except (ValueError, KeyError):
        uv_index = 'N/A'  # Fallback value if UV index is not available

    return uv_index

def main():
    latitude = 3.8667 # Replace with the latitude of the location
    longitude = 11.5167  # Replace with the longitude of the location

    uv_index = get_uv_index(latitude, longitude)
    print(f"UV Index: {uv_index}")

if __name__ == '__main__':
    main()