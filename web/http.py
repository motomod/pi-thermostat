from flask import Flask
from flask import render_template
import yaml
from subprocess import call

class sdasdas:

    def test():
        print("adsdas")

    def webrun(config):
        app = Flask(__name__)

        @app.route('/temp')
        def temp():
            return "26";

        @app.route('/dashboard')
        def dash():
            return render_template('index.html')

        if __name__ == '__main__':
            app.run(host= '192.168.1.210', port=9000, debug=True)
