from xgboost import XGBClassifier
import numpy as np

model = XGBClassifier()
model.load_model('test_model')


def predict_kickstart(goal, duration, cat, country):
    data = np.zeros(20)
    data[0] = goal
    data[1] = duration
    data[int(cat)] = 1
    data[int(country)] = 1
    return model.predict_proba([data])
