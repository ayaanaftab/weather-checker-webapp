import requests
import json

def get_weather_for_city(city_name):
    """
    Get weather for ANY city by:
    1. Converting city name to coordinates
    2. Getting weather for those coordinates
    """
    
    # STEP 1: Convert city name to coordinates (geocoding)
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        'name': city_name,
        'count': 1,  # Just get the first result
        'format': 'json'
    }
    
    print(f"🔍 Searching for coordinates of '{city_name}'...")
    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()
    
    # Check if city was found
    if not geo_data.get('results'):
        print(f"❌ City '{city_name}' not found!")
        return None
    
    # Extract coordinates from the geocoding result
    city_info = geo_data['results'][0]
    lat = city_info['latitude']
    lon = city_info['longitude']
    actual_city_name = city_info['name']
    country = city_info.get('country', 'Unknown')
    
    print(f"📍 Found: {actual_city_name}, {country} (Lat: {lat}, Lon: {lon})")
    
    # STEP 2: Get weather data for these coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': 'true',
        'temperature_unit': 'celsius'
    }
    
    print("🌤️ Fetching weather data...")
    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()
    
    # Add city information to the weather data
    weather_data['city_name'] = actual_city_name
    weather_data['country'] = country
    
    return weather_data

def display_weather(data):
    """Display the weather in a nice format"""
    if not data:
        return
    
    city = data['city_name']
    country = data['country']
    current = data['current_weather']
    
    # Weather code descriptions
    weather_codes = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Fog", 51: "Light drizzle", 53: "Moderate drizzle",
        61: "Light rain", 63: "Moderate rain", 65: "Heavy rain",
        80: "Light showers", 81: "Moderate showers", 82: "Violent showers",
        95: "Thunderstorm"
    }
    
    weather_desc = weather_codes.get(current['weathercode'], "Unknown conditions")
    
    print("\n" + "="*50)
    print(f"🌤️  WEATHER IN {city.upper()}, {country.upper()}")
    print("="*50)
    print(f"🌡️  Temperature: {current['temperature']}°C")
    print(f"📝 Conditions: {weather_desc}")
    print(f"💨 Wind Speed: {current['windspeed']} km/h")
    print(f"🧭 Wind Direction: {current['winddirection']}°")
    print("="*50)

# Main program
def main():
    print("🌍 UNIVERSAL WEATHER APP")
    print("Get weather for any city worldwide!")
    print("Type 'quit' to exit\n")
    
    while True:
        city = input("Enter city name: ").strip()
        
        if city.lower() in ['quit', 'exit', 'q']:
            print("Thanks for using the weather app! 👋")
            break
        
        if not city:
            print("Please enter a city name.")
            continue
        
        # Get and display weather
        weather_data = get_weather_for_city(city)
        
        if weather_data:
            display_weather(weather_data)
        else:
            print("Please try another city name.\n")

if __name__ == "__main__":
    main()