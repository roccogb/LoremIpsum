from flask import Flask
from backend import register_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tp-ids-2025'

register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=8100)
