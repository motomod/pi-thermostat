from flask import Flask
from flask import render_template

def run(config):
    if config["enabled"] != True:
	return

    print "web started"

    app = Flask(__name__)

    @app.route('/temp')
    def temp():
        return "26";

    @app.route('/dashboard')
    def dash():
        return render_template('index.html')

    app.run(host= 'localhost', port=9000, debug=True)
