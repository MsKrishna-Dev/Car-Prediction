from pathlib import Path
import pandas as pd
import joblib

CAR_PRICE_API_DIR = Path(__file__).resolve().parent
# BASE_DIR = Path(__file__).resolve().parent.parent  # goes to Car Price FastAPI/
MODEL_PATH = CAR_PRICE_API_DIR / "random_forest_model.pkl"
COLS_PATH = CAR_PRICE_API_DIR / "feature_columns.pkl"
# MODEL_PATH = BASE_DIR / "random_forest_model.pkl"
# COLS_PATH = BASE_DIR / "feature_columns.pkl"

print(COLS_PATH)
_model = None
_feature_columns = None

# print("Model path:", MODEL_PATH)
# print("Columns path:", COLS_PATH)

# _model = None
# _feature_columns = None


def load_artifacts():
    global _model, _feature_columns
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _feature_columns is None:
        _feature_columns = joblib.load(COLS_PATH)


def preprocess(payload: dict) -> pd.DataFrame:
    """
    Converts raw input into the SAME one-hot encoded column structure used in training.
    """
    df = pd.DataFrame([payload])

    categorical_cols = ["Fuel_Type", "Seller_Type", "Transmission", "Owner", "Car_Name"]
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Align columns to training columns
    for col in _feature_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    # Remove extra cols (if any) and order correctly
    df_encoded = df_encoded[_feature_columns]

    return df_encoded


def predict_price(payload: dict) -> float:
    load_artifacts()
    X = preprocess(payload)
    pred = _model.predict(X)[0]
    return float(pred)
