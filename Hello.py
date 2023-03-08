from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hellomyfriend"

@app.route('/code', methods=['GET'])
def get_code():
    # récupérer le code ici et le stocker dans une variable 'code'
    code = "33"
    return code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

        

