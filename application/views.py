from initialize import * 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World', 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run()
