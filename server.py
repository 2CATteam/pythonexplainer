from flask import Flask, request
import json, explainer, Lowes, library, run
app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
    return app.send_static_file('home.html')

@app.route('/explain/', methods=['POST'])
def explain():
    code = request.form.get("code")
    if (code):
        toReturn = explainer.readCode(code)
        return json.dumps(toReturn)
    else:
        print("No code")
        return None

@app.route('/trace/', methods=['POST'])
def trace():
    code = request.form.get("code")
    variable = request.form.get("variable")
    if (code):
        toReturn = {}
        #Do the thing
        return json.dumps(toReturn)

@app.route('/run/', methods=['POST'])
def runServer():
    code = request.form.get("code")
    input = request.form.get("input")
    if (code):
        toReturn = run.testRun(code, input)
        return json.dumps(toReturn)

@app.route('/debug/', methods=['POST'])
def debug():
    code = request.form.get("code")
    if (code):
        toReturn = Lowes.Lowes(code)
        #Do the thing
        return json.dumps(toReturn)

if (__name__ == "__main__"):
    app.run()
print('Running website')
