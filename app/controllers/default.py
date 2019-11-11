from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Hello World"


@app.route("/hey/<name>")
def hello(name):
    return "Hey, %s!" % name