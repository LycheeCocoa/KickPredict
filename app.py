from flask import Flask, render_template, request
from predict import predict_kickstart


def create_app():
    app = Flask(__name__)

    # setup for usage w/nginx
    @app.route('/')
    def root():
        return render_template('index.html', title="Home")

    @app.route('/predict/', methods=['GET', 'POST'])
    def predict():
        # 0 Goal
        # 1 Duration
        # 2 - 15 Cats
        # 16 - 19 Countries
        goal = request.form.get('goal')
        duration = request.form.get('duration')
        cat = request.form.get('category')
        country = request.form.get('country')

        prediction = predict_kickstart(goal, duration, cat, country)
        message = 'Your Kickstarter is {}% likely to succeed!'.format(
            (prediction[0][1] * 100).round(2))

        return render_template('prediction.html', message=message)

    return app
