import streamlit as st
import boto3
import pandas as pd
import mlflow.pyfunc

st.title("Real-Time Netflix Subscription Analytics Dashboard")

# DynamoDB setup with error handling
try:
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name='us-east-1')
    subs_table = dynamodb.Table('Subscriptions')
    subs = subs_table.scan()['Items']
except Exception as e:
    subs = []
    st.error(f"Failed to connect to DynamoDB or table 'Subscriptions' not found: {e}")

st.header("Subscriptions from DynamoDB")
if subs:
    for sub in subs:
        st.write(f"Country: {sub.get('country', 'N/A')}, Basic: ${sub.get('basic_fee', 0)}, "
                 f"Standard: ${sub.get('standard_fee', 0)}, Premium: ${sub.get('premium_fee', 0)}")
else:
    st.write("No data available in DynamoDB or table not found.")

st.header("Batch Analytics")
try:
    df = pd.read_parquet('D:\\Netflix Project\\Python Scripts\\data_lake\\subscriptions_batch.parquet')
    if not df.empty:
        st.bar_chart(df.groupby('Country')['Cost Per Month - Basic ($)'].mean())

        # Load the latest MLflow model 
        run_id = "230d19d2543f4d7a9e2f668342734d38"  
        model_uri = f"runs:/{run_id}/subscription_model"
        model = mlflow.pyfunc.load_model(model_uri)

        # Example prediction
        sample = df[['Cost Per Month - Basic ($)', 'Cost Per Month - Standard ($)']].iloc[0].values.reshape(1, -1)
        predicted_premium = model.predict(sample)[0]
        st.write(f"Predicted Premium Fee for Sample: ${predicted_premium:.2f}")
    else:
        st.write("No data available in the Parquet file.")
except FileNotFoundError:
    st.error("Parquet file not found. Please ensure 'subscriptions_batch.parquet' exists.")
except KeyError as e:
    st.error(f"Column error: {e}. Available columns are: {df.columns.tolist() if 'df' in locals() else 'N/A'}")
except Exception as e:
    st.error(f"An error occurred: {e}")