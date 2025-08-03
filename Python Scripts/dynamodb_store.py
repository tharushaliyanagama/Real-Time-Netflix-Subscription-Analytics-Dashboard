import boto3
from botocore.exceptions import ClientError

class DynamoDBStore:
    def __init__(self, endpoint='http://localhost:8000', region_name='us-east-1'):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint, region_name=region_name)

    def get_table(self, table_name):
        return self.dynamodb.Table(table_name)

    def create_table(self, table_name, key_schema, attribute_definitions):
        table = self.dynamodb.Table(table_name)
        try:
            # Check if table already exists
            table.load()
            print(f"Table {table_name} already exists.")
            return
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                # Table does not exist, proceed to create
                self.dynamodb.create_table(
                    TableName=table_name,
                    KeySchema=key_schema,
                    AttributeDefinitions=attribute_definitions,
                    BillingMode='PAY_PER_REQUEST'
                )
                print(f"Creating table {table_name}...")
                table.wait_until_exists()
                print(f"Table {table_name} created successfully.")
            else:
                # Other error occurred
                print(f"Error checking table: {e}")
                raise

    def describe_table(self, table_name):
        """Optional: Describe table details for debugging."""
        table = self.dynamodb.Table(table_name)
        try:
            return table.table_status
        except ClientError as e:
            print(f"Error describing table: {e}")
            raise

