import os
from flask import Flask, render_template, request, jsonify
from weather_backend import get_weather_data, get_weather_description

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Template error: {str(e)}"

@app.route('/weather', methods=['POST'])
def get_weather():
    try:
        city = request.form.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'Please enter a city name'})
        
        weather_data = get_weather_data(city)
        
        if weather_data:
            weather_data['description'] = get_weather_description(weather_data['conditions'])
            weather_data['emoji'] = weather_data['description'].split(' ')[0]
            return jsonify(weather_data)
        else:
            return jsonify({'error': f'City "{city}" not found'})
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
