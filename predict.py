from xgboost import XGBClassifier
from joblib import load
import numpy as np
model = XGBClassifier()
model.load_model('test_model')

def predict_kickstart():
    return '1'