import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('data/iris.csv')  # change to your dataset path

X = df.drop('target', axis=1)
y = df['target']

# Split & train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")