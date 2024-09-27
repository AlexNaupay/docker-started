import json
from flask import Flask
app = Flask(__name__)

@app.route('/me')
def getMyInfo():
    value = {
        "name": "Alex",
        "lastname": "N",
        "socialMedia":
        [
            {"facebookUser": "nlexhen"},
            {"instagramUser": "alexnaupay"},
            {"xUser": "alexnaupay"},
            {"githubUser": "alexnaupay"}
        ],
        "blog": "https://alexnaupay.com",
        "author": "Alex Naupay"
    }
    return json.dumps(value)