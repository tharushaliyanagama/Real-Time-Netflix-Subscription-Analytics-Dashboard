import csv
import apache_beam as beam
from dynamodb_store import DynamoDBStore

class WriteToSubscriptionsFn(beam.DoFn):
    def process(self, element):
        import boto3
        store = DynamoDBStore(endpoint='http://localhost:8000')  # Removed region_name
        table = store.get_table('Subscriptions')
        table.put_item(Item=element)
        return [element]

with beam.Pipeline() as pipeline:
    data = []
    with open('netflix price in different countries.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i < 5:  # Simulate stream with first 5 rows
                data.append({
                    'id': row['Country'].lower().replace(' ', '_'),
                    'country': row['Country'],
                    'basic_fee': row['Cost Per Month - Basic ($)'],
                    'standard_fee': row['Cost Per Month - Standard ($)'],
                    'premium_fee': row['Cost Per Month - Premium ($)']
                })
    (pipeline
     | beam.Create(data)
     | beam.ParDo(WriteToSubscriptionsFn())
     | beam.Map(print))