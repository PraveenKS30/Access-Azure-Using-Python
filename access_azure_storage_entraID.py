from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
account_url = os.environ["AZURE_STORAGE_URL"]

# create a credential 
credentials = ClientSecretCredential(
    client_id = client_id, 
    client_secret= client_secret,
    tenant_id= tenant_id
)

container_name = 'democontainer3006'
blob_name = 'sample3.txt'

# set client to access azure storage container
blob_service_client = BlobServiceClient(account_url= account_url, credential=credentials)

# get the container client 
container_client = blob_service_client.get_container_client(container=container_name)

# download blob data 
blob_client = container_client.get_blob_client(blob= blob_name)

data = blob_client.download_blob().readall().decode("utf-8")

print(data)