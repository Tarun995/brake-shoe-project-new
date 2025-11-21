import joblib
import pandas as pd

model = joblib.load(r"D:\New volume 1\sem 3\projects\Brake Shoes\models\defect_model.joblib")

def predict_defect(temp, pressure, cycle_time, vibration, humidity):
    X = pd.DataFrame([[temp, pressure, cycle_time, vibration, humidity]],
                     columns=['temp','pressure','cycle_time','vibration','humidity'])
    
    prob = model.predict_proba(X)[0][1]
    return prob
