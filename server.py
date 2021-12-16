from jinja2 import environment
from UI import app

if __name__ == "__main__":
    app.env = "development"
    app.run(port=8080, debug=True)