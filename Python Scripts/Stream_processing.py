import apache_beam as beam
import csv
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import WriteToParquet
import pyarrow as pa

# Define pyarrow schema for Parquet
schema = pa.schema([
    ('id', pa.string()),
    ('country', pa.string()),
    ('basic_fee', pa.float64()),
    ('standard_fee', pa.float64()),
    ('premium_fee', pa.float64()),
    ('timestamp', pa.string())
])

# Beam pipeline
with beam.Pipeline(options=PipelineOptions()) as pipeline:
    data = []
    with open('D:\\Netflix Project\\Python Scripts\\netflix price in different countries.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i < 5:
                data.append({
                    'id': row['Country'].lower().replace(' ', '_'),
                    'country': row['Country'],
                    'basic_fee': float(row['Cost Per Month - Basic ($)']),
                    'standard_fee': float(row['Cost Per Month - Standard ($)']),
                    'premium_fee': float(row['Cost Per Month - Premium ($)']),
                })

    (
        pipeline
        | "Create Data" >> beam.Create(data)
        | "Add Timestamp" >> beam.Map(lambda x: {
            'id': x['id'],
            'country': x['country'],
            'basic_fee': x['basic_fee'],
            'standard_fee': x['standard_fee'],
            'premium_fee': x['premium_fee'],
            'timestamp': '2025-08-03T19:00:00Z'
        })
        | "Write to Parquet" >> WriteToParquet(
            file_path_prefix='D:\\Netflix Project\\Python Scripts\\data_lake\\subscriptions_stream',
            schema=schema,
            file_name_suffix=".parquet"
        )
    )
