# app.py
from flask import Flask, render_template, request, jsonify
from weather_backend import get_weather_data, get_weather_description

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city', '').strip()
    
    if not city:
        return jsonify({'error': 'Please enter a city name'})
    
    weather_data = get_weather_data(city)
    
    if weather_data:
        # Add emoji and description
        weather_data['description'] = get_weather_description(weather_data['conditions'])
        weather_data['emoji'] = weather_data['description'].split(' ')[0]  # Get the emoji
        return jsonify(weather_data)
    else:
        return jsonify({'error': f'City "{city}" not found. Please try another name.'})

if __name__ == '__main__':
    app.run(debug=True)