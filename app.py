from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/rsvp")
def rsvp():
	return render_template("rsvp.html")


@app.route("/rsvp/<code>")
def rsvp_code(code):
	return render_template("rsvp_code.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
