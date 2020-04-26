from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/hey', methods=['GET','POST'])
def hello():
	return render_template("hey.html")

if __name__ == "__main__":
	app.run(debug = True)
