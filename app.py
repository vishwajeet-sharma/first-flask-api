from flask import Flask,jsonify,make_response
import requests
import sys
from loguru import logger

app = Flask(__name__)

@app.route('/users', methods=["GET","POST"])

def fetchname():
    try:
        logger.info("My first API")
        r = requests.get('https://jsonplaceholder.typicode.com/users')
        if 200 <= r.status_code <= 299:
            #logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
            logger.info("response successfully recieved")
        elif 400 <= r.status_code <= 499:
            logger.exception("Client error:Webpage not found")
        else:
            logger.exception("Internal Server error")
        data =  r.json()
        namerev = []
        for entry in data:
            namerev.append(entry['name'][::-1])
        #print(namerev)
    
        return make_response(jsonify(namerev), 200)
    except:
        logger.exception("No response submitted")
    
if __name__ == '__main__':
    app.run(debug=True)
