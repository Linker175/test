from flask import Flask 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_request():
    # Gérer la requête GET ici
    return 'Hello ESP32!'

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
        

