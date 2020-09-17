from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/renan/<name>')
def renan(name):
    return "<h1>Olá, {}!</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)