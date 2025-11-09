import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Weather App is WORKING! If you see this, deployment is successful!"

@app.route('/test')
def test():
    return "✅ Test route is also working!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
