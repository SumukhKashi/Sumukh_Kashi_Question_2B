from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Sumukh Kashi 1BM20IS163!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)