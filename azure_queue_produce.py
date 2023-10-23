from azure.identity import ClientSecretCredential
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
account_url = os.environ["AZURE_QUEUE_URL"]

queue_name = "queue360"

# create a credential 
credentials = ClientSecretCredential(
    client_id = client_id, 
    client_secret= client_secret,
    tenant_id= tenant_id
)

# Create the QueueClient object
queue_client = QueueClient(account_url=account_url, 
                        queue_name=queue_name, 
                        credential=credentials,
                        message_encode_policy=BinaryBase64EncodePolicy()
                        )


# read from file and push it to queue
with open("queue_input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    queue_client.send_message(line.encode())
    