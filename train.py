import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

DATA_PATH = "car-price-api/cardekho_data (1).csv"  # put the csv in project root (same as train.py)
MODEL_PATH = "car-price-api/random_forest_model.pkl"
COLS_PATH = "car-price-api/feature_columns.pkl"


def main():
    df = pd.read_csv(DATA_PATH)

    # Target / Features
    X = df.drop("Selling_Price", axis=1)
    y = df["Selling_Price"]

    # One-hot encode categorical columns (same idea as your notebook)
    categorical_cols = ["Fuel_Type", "Seller_Type", "Transmission", "Owner", "Car_Name"]
    X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42
    )

    # Train model (you can replace params with your best_params_ from RandomizedSearchCV)
    model = RandomForestRegressor(n_estimators=500, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    # Save model + training columns (VERY IMPORTANT for inference alignment)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(list(X_train.columns), COLS_PATH)

    print("✅ Model saved to:", MODEL_PATH)
    print("✅ Feature columns saved to:", COLS_PATH)
    print("Train columns count:", len(X_train.columns))


if __name__ == "__main__":
    main()
