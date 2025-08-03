import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Set MLflow tracking URI
mlflow.set_tracking_uri("file:///D:/Netflix Project/Python Scripts/mlruns")

# Start an MLflow run
with mlflow.start_run():
    # Load data from Parquet
    df = pd.read_parquet('D:\\Netflix Project\\Python Scripts\\data_lake\\subscriptions_batch.parquet')

    # Prepare features (X) and target (y)
    X = df[['Cost Per Month - Basic ($)', 'Cost Per Month - Standard ($)']]
    y = df['Cost Per Month - Premium ($)']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Log parameters and metrics
    mlflow.log_param("model", "LinearRegression")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_metric("test_r2_score", model.score(X_test, y_test))
    mlflow.log_metric("training_samples", len(X_train))

    # Save model
    joblib.dump(model, 'ml_models/fee_predictor_model.pkl')
    mlflow.sklearn.log_model(model, "subscription_model")

    print(f"Model trained with R² score: {model.score(X_test, y_test):.4f}")