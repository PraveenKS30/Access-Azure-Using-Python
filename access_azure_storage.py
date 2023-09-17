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

def get_blob_data():
    
    container_name = 'storagecommoncontainer'
    blob_name = 'sample3.txt'

    # set client to access azure storage container
    blob_service_client = BlobServiceClient(account_url= account_url, credential= credentials)

    # get the container client 
    container_client = blob_service_client.get_container_client(container=container_name)

    # download blob data 
    blob_client = container_client.get_blob_client(blob= blob_name)

    data = blob_client.download_blob().readall().decode("utf-8")

    print(data)

def list_blob():
    container_name = 'storagecommoncontainer'

    # set client to access azure storage container
    blob_service_client = BlobServiceClient(account_url= account_url, credential= credentials)

    # get the container client 
    container_client = blob_service_client.get_container_client(container=container_name)

    for blob in container_client.list_blobs():
        print(blob.name)


def get_multi_blob_data():
    container_name = 'storagecommoncontainer'

    # set client to access azure storage container
    blob_service_client = BlobServiceClient(account_url= account_url, credential= credentials)

    # get the container client 
    container_client = blob_service_client.get_container_client(container=container_name)

    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob= blob.name)
        data = blob_client.download_blob().readall()
        print(data.decode("utf-8"))

def upload_blob():
    local_dir = "input"
    container_name = 'storagecommoncontainer'

    # set client to access azure storage container
    blob_service_client = BlobServiceClient(account_url= account_url, credential= credentials)

    # get the container client 
    container_client = blob_service_client.get_container_client(container=container_name)

    # read all files from directory
    filenames = os.listdir(local_dir)
    
    for filename in filenames :
        # get full file path
        full_file_path = os.path.join(local_dir, filename) 

        # read files and upload data to blob storage container 
        with open(full_file_path, "r") as fl :
            data = fl.read()
            container_client.upload_blob(name= filename, data=data)


# main
if __name__ == "__main__":
    #get_blob_data()
    #list_blob()
    #get_multi_blob_data()
    upload_blob()
