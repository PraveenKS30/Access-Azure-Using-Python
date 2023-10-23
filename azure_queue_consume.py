from azure.identity import ClientSecretCredential
from azure.storage.queue import QueueClient, BinaryBase64DecodePolicy
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
account_url = os.environ["AZURE_QUEUE_URL"]

queue_name = "queue360"
poison_queue = "queue360-poison"

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
                        message_decode_policy=BinaryBase64DecodePolicy())

poison_queue_client = QueueClient(account_url=account_url, 
                        queue_name=poison_queue, 
                        credential=credentials
                    )


# read messages from the queue
messages = queue_client.receive_messages()
    
# print messages
# print messages
for message in messages:
    try:
        # Process the message here
        # Raise an exception if the message contains 'error'
        message_content = message.content.decode('utf-8')
        if 'error' in message_content:
            raise Exception("Error keyword found in message.")
        else:
            print(message_content)
    except Exception as e:
        poison_queue_client.send_message(message_content)
        print(f"Moved message to poison queue due to error: {str(e)}")
        queue_client.delete_message(message)
