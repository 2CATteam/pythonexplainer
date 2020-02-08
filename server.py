from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
    return app.send_static_file('home.html')
app.run()
print('Running website')
