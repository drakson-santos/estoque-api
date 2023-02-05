from wsgi import create_app
from flask_cors import CORS

app = create_app()
CORS(app)

@app.route('/')
def index():
    print("bbbbbbbbbbbb")
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(debug=True)