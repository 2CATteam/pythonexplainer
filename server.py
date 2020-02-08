from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
    return app.send_static_file('home.html')

@app.route('/explain/', methods=['POST'])
def explain():
    code = request.args.get("code")
    if (code):
        toReturn = {}
        #Do the thing
        return json.dumps(toReturn)
    else:
        return None

@app.route('/trace/', methods=['POST'])
def trace():
    code = request.args.get("code")
    variable = request.args.get("variable")
    if (code):
        toReturn = {}
        #Do the thing
        return json.dumps(toReturn)

@app.route('/run/', methods=['POST'])
def run():
    code = request.args.get("code")
    if (code):
        toReturn = {}
        #Do the thing
        return json.dumps(toReturn)

@app.route('/debug/', methods=['POST'])
def trace():
    code = request.args.get("code")
    if (code):
        toReturn = {}
        #Do the thing
        return json.dumps(toReturn)

app.run()
print('Running website')
