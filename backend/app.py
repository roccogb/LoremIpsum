from flask import Flask
from routes_backend import register_routes

app = Flask(__name__,
    static_folder="../frontend/static",
    template_folder="../frontend/templates")

app.config['SECRET_KEY'] = 'tp-ids-2025'

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=8100)
