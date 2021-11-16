from xgboost import XGBClassifier
model = XGBClassifier()
model.load_model('test_model')

def predict_kickstart():
    return '1'