# simple flask app
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask API Home Page'

@app.route('/api')
def test():
    return jsonify({'message':'Flask Api is running'})


@app.route('/api/test')
def checks():
    return jsonify({'message':'Flask Api is tested'})

@app.route('/flask')
def checks():
    return jsonify({'Project Author':'Nelson Nwajie'})

@app.route('/api/flask')
def checks():
    return jsonify({'Project Author':'Nelson Nwajie'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

# flask app that needs configmap
# export SECRET_KEY=password
#export MY_VARIABLE=nelson

# import os
# from flask import Flask

# app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY')

# @app.route('/')
# def hello():
#     my_variable = os.environ.get('MY_VARIABLE')
#     if my_variable:
#         return f'The value of MY_VARIABLE is: {my_variable}<br>Secret Key: {app.secret_key}'
#     else:
#         return 'MY_VARIABLE is not set.'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True, port=5000)