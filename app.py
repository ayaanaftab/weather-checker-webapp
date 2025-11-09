import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 SUCCESS! Flask is running on Railway!"

@app.route('/health')
def health():
    return "✅ Health check passed!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
