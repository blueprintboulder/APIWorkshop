import requests
from flask import Flask
import importlib
util = importlib.import_module('util')

app = Flask(__name__)

@app.route("/")
def home():

    return 'DELETEME -- as you can see, your webpage displays what this function returns!'

    LOCATION = ''   # TODO: enter your desired location
    url = ''        # TODO: figure out the endpoint to use!
    response = ''   # TODO: make a get request!
    json_resp = ''  # TODO: access the returned data in json format

    # Construct HTML code to return
    return util.generate_html(LOCATION, json_resp)
    
if __name__ == "__main__":
    app.run(debug=True)
