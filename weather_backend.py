import requests

def get_weather_data(city_name):
    """Simple version to get it working"""
    try:
        # Just return test data for now
        return {
            'city': city_name,
            'country': 'Test',
            'temperature': 20,
            'conditions': 0,
            'wind_speed': 10,
            'wind_direction': 180
        }
    except:
        return None

def get_weather_description(code):
    return "☀️ Clear sky"
