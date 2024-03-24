from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os 

load_dotenv()

sas_token = os.environ["AZURE_SAS_TOKEN"]
account_url = os.environ["AZURE_STORAGE_URL"]
container_name = 'democontainer3006'
blob_name = 'sample3.txt'

# set client to access azure storage container
blob_service_client = BlobServiceClient(account_url= account_url, credential=sas_token)

# get the container client 
container_client = blob_service_client.get_container_client(container=container_name)

# download blob data 
blob_client = container_client.get_blob_client(blob= blob_name)

data = blob_client.download_blob().readall().decode("utf-8")

print(data)