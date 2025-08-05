# Real-Time Netflix Subscription Analytics Dashboard

## Overview
This project is a Real-Time Netflix Subscription Analytics Dashboard designed to process, store, and visualize Netflix subscription cost data across different countries. It leverages modern data engineering tools (Apache Beam, PySpark), real-time storage (DynamoDB), interactive visualization (Streamlit), and machine learning (MLflow, scikit-learn) to provide actionable insights and predictive analytics. Developed as part of an internship project, this repository demonstrates skills in data pipeline development, cloud integration, and ML model deployment.

## Features
- Real-Time Data Processing: Uses Apache Beam for streaming CSV data into Parquet files.
- Scalable Storage: Integrates with a local DynamoDB instance for real-time data persistence.
- Interactive Dashboard: Built with Streamlit to visualize subscription costs and trends.
- Predictive Analytics: Implements a linear regression model (tracked with MLflow) to predict premium subscription fees based on basic and standard fees.
- Experiment Tracking: Utilizes MLflow for managing model parameters, metrics, and versioning.

## Tech Stack
- **Languages**: Python 3.x
- **Libraries/Frameworks**:
  - Apache Beam (v2.58.0) for data processing
  - PySpark for batch processing
  - Streamlit for dashboarding
  - MLflow for ML experiment tracking
  - scikit-learn for predictive modeling
  - boto3 for DynamoDB interaction
  - pandas and pyarrow for data handling
- **Infrastructure**: Docker with DynamoDB-local
- **Version Control**: Git

## Installation & Setup
### Prerequisites
- **Docker**: For running the local DynamoDB instance.
- **Python 3.x**: With pip and virtualenv or Conda.
- **Git**: For cloning the repository.

### Steps
#### Clone the Repository
```
git clone https://github.com/TharushaLiyanagama/Netflix-Analytics-Dashboard.git
cd Netflix-Analytics-Dashboard
```

#### Set Up Virtual Environment
- Using Conda (recommended):
  ```
  conda create -n netflix_env python=3.9
  conda activate netflix_env
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```

#### Start DynamoDB
- Ensure Docker is running, then:
  ```
  docker-compose up -d
  ```

#### Run the Dashboard
- Navigate to the Python Scripts directory:
  ```
  cd Python Scripts
  streamlit run app.py
  ```

## Project Structure
```
Netflix-Analytics-Dashboard/
├── .gitignore              # Excludes environment and large files
├── README.md               # This file
├── requirements.txt        # Dependency list
├── docker-compose.yml      # DynamoDB configuration
├── Python Scripts/
│   ├── batch_ingestion.py  # Batch data ingestion
│   ├── stream_ingestion.py # Streaming data processing
│   ├── batch_processing.py # PySpark batch processing
│   ├── Stream_processing.py # Beam streaming to Parquet
│   ├── app.py             # Streamlit dashboard
│   ├── netflix_pipeline.py # Pipeline orchestration
│   ├── dynamodb_store.py  # Data loading to DynamoDB
│   ├── Create_table.py    # DynamoDB table creation
│   ├── ml_model.py        # Initial ML model
│   ├── subscription_predictor.py # MLflow-tracked model
│   ├── netflix price in different countries.csv # Sample data
│   ├── Netflix subscription fee Dec-2021.csv # Additional data
│   ├── data_lake/         # Parquet outputs 
│   ├── ml_models/         # Model files (ignored)
│   └── mlruns/            # MLflow experiment data 
```

## Usage
- **Data Ingestion**: Run `Stream_processing.py` or `batch_processing.py` to generate Parquet files in `data_lake/`.
- **Dashboard**: View real-time data and predictions at http://localhost:8501.
- **ML Experiments**: Modify `subscription_predictor.py` to experiment with different models, then track results in the MLflow UI.

## Future Improvements
- Integrate real-time ML predictions using MLflow model serving.
- Add more sophisticated models (e.g., random forest, neural networks).
- Enhance dashboard with interactive filters and multi-country comparisons.

## Last Updated
August 04, 2025
