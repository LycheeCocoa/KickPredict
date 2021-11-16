from flask import Flask, render_template, request
from .predict import predict_kickstart


def create_app():
    app = Flask(__name__)

    # setup for usage w/nginx
    @app.route('/')
    def root():
        return render_template('index.html', title="Home")

    @app.route('/predict/')
    def predict():
        return predict_kickstart()

    return app
