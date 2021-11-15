from flask import Flask, render_template, request
import random
import string


def create_app():
    app = Flask(__name__, static_url_path='/static')

    # setup for usage w/nginx
    @app.route('/')
    def root():
        return render_template('landing.html', title="Home")

    return app
