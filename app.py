from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() :
	return "Hello! What's up?<h1> Hi, there</h1>"

if __name__ == "__main__" :
	app.debug = True
	app.run(port=5000)
