import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name='us-east-1')

table_name = 'Subscriptions'

# Check if table exists
existing_tables = [table.name for table in dynamodb.tables.all()]
if table_name not in existing_tables:
      table = dynamodb.create_table(
          TableName=table_name,
          KeySchema=[
              {'AttributeName': 'country', 'KeyType': 'HASH'},  # Partition key
          ],
          AttributeDefinitions=[
              {'AttributeName': 'country', 'AttributeType': 'S'},
          ],
          ProvisionedThroughput={
              'ReadCapacityUnits': 5,
              'WriteCapacityUnits': 5
          }
      )

      table.wait_until_exists()
      print(f"Table '{table_name}' created successfully!")
else:
      print(f"Table '{table_name}' already exists. No action taken.")