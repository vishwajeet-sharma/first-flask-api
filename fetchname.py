from flask import Flask,jsonify
import requests
app = Flask(__name__)

@app.route('/users', methods=["GET"])
def log():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    data =  r.json()
    print(data[0][1])
    return ""

if __name__ == '__main__':
    app.run()
