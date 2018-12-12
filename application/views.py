from initialize import * 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World', 200

if __name__ == '__main__':
    app.run()
