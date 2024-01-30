import os
import json
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv

load_dotenv()

# define database and container
db_name = 'testdb'
container_name = 'personinfo'

# credential
cosmos_url = os.environ["AZURE_EMULATOR_COSMOS_ENDPOINT"]
cosmos_key = os.environ["AZURE_EMULATOR_COSMOS_KEY"]

# create cosmos client
client = CosmosClient(url= cosmos_url, credential= cosmos_key)

# define partition key 
key_path = PartitionKey(path="/id")

# create a database if not exists
database = client.create_database_if_not_exists(id= db_name)
print("database", database.id)

# create a container if not exists
container = database.create_container_if_not_exists(
    id= container_name, 
    partition_key = key_path,
    offer_throughput = 400
)
print("container", container.id)
'''
# insert an item 
new_item = {
        "id": "1",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "price": 7.99,
        "published_year": 1960
}

container.create_item(new_item)


# bulk insert
# load data file
with open('data.json') as f:
    items = json.load(f)

# read item one by one and insert it into cosmosdb
for item in items:
    container.create_item(item)


# query an item 
QUERY = "SELECT * FROM personinfo p WHERE p.id = @Id"
ID = "3"
params = [dict(name="@Id", value=ID)]

results = container.query_items(
    query=QUERY, parameters=params, enable_cross_partition_query=True
)

# loop over the results 
items = [item for item in results]
output = json.dumps(items, indent=True)
print("Result list\t", output)


# query an item 
QUERY = "SELECT * FROM personinfo p WHERE p.id IN (@Id1, @Id2)"
ID1 = "3"
ID2 = "4"
params = [dict(name="@Id1", value=ID1), dict(name="@Id2", value=ID2)]

results = container.query_items(
    query=QUERY, parameters=params, enable_cross_partition_query=True
)

# loop over the results 
items = [item for item in results]
output = json.dumps(items, indent=True)
print("Result list\t", output)
'''

# upsert an item 
new_item1 = {
        "id": "4",
        "title": "Moby Dick",
        "author": "Herman Melville",
        "genre": "Adventure",
        "price": 19.99,
        "published_year": 1851
    }

container.upsert_item(new_item1)