from flask import Flask, request
from flask_cors import CORS #cross_origin

import oriongw

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello from CityIoT Oulu!'

@app.route('/optimasolutions_get1')
def optimasolutions_get1():
    return oriongw.get_optimasolutions_test1()

@app.route('/optimasolutions_get2')
def optimasolutions_get2():
    return oriongw.get_optimasolutions_test2()

@app.route('/optimasolutions_set1', methods=['POST'])
def optimasolutions_set1():
	idasdata = request.get_data(as_text=True, parse_form_data=False)
	return oriongw.set_optimasolutions_test1(idasdata)

@app.route('/optimasolutions_set2', methods=['POST'])
def optimasolutions_set2():
	idasdata = request.get_data(as_text=True, parse_form_data=False)
	return oriongw.set_optimasolutions_test2(idasdata)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
