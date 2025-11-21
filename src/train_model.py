import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv(r"D:\New volume 1\sem 3\projects\Brake Shoes\raw_data.csv")

X = df[['temp','pressure','cycle_time','vibration','humidity']]
y = df['defect']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy =", accuracy_score(y_test, pred))

# Save model
joblib.dump(model, "./models/defect_model.joblib")

print("Model saved!")
