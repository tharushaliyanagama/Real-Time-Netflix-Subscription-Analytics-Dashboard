import csv
from dynamodb_store import DynamoDBStore

def ingest_csv():
    store = DynamoDBStore(endpoint='http://localhost:8000')
    table = store.get_table('Subscriptions')
    with open('D:\\Netflix Project\\Python Scripts\\Netflix subscription fee Dec-2021.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print("CSV Headers:", reader.fieldnames)
        for row in reader:
            table.put_item(Item={
                'id': row['Country_code'],
                'country': row['Country'],
                'basic_fee': row['Cost Per Month - Basic ($)'],
                'standard_fee': row['Cost Per Month - Standard ($)'],
                'premium_fee': row['Cost Per Month - Premium ($)']
            })

if __name__ == '__main__':
    ingest_csv()