"""Week 4 predictive modeling workflow."""
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("data/processed/logistics_shipments.csv")
target = "Delivery_Time_hr"
X = df.drop(columns=target)
y = df[target]

categorical = ["Zone", "Transport_Mode", "Traffic_Level"]
numeric = ["Shipment_Volume_kg", "Distance_km"]

preprocessor = ColumnTransformer([
    ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical),
    ("numeric", "passthrough", numeric),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=8, min_samples_leaf=5, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=200, max_depth=12, min_samples_leaf=3, random_state=42)
}

for name, estimator in models.items():
    pipe = Pipeline([("preprocessor", preprocessor), ("model", estimator)])
    pipe.fit(X_train, y_train)
    prediction = pipe.predict(X_test)
    print(name)
    print("MAE:", mean_absolute_error(y_test, prediction))
    print("RMSE:", mean_squared_error(y_test, prediction) ** 0.5)
    print("R2:", r2_score(y_test, prediction))

rf = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(random_state=42, n_jobs=-1)),
])

parameters = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [8, 12, None],
    "model__min_samples_leaf": [2, 4],
}

search = GridSearchCV(
    rf, parameters, cv=3,
    scoring="neg_root_mean_squared_error", n_jobs=-1
)
search.fit(X_train, y_train)
best_prediction = search.predict(X_test)

print("Best parameters:", search.best_params_)
print("Tuned MAE:", mean_absolute_error(y_test, best_prediction))
print("Tuned RMSE:", mean_squared_error(y_test, best_prediction) ** 0.5)
print("Tuned R2:", r2_score(y_test, best_prediction))
