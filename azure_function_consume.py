import requests 
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
vault_url = os.environ["AZURE_VAULT_URL"]
function_url= os.environ["AZURE_FUNCTION_URL"]


secret_name = "FUNCTION-KEY"

# create a credential 
credentials = ClientSecretCredential(
    client_id = client_id, 
    client_secret= client_secret,
    tenant_id= tenant_id
)

# create a secret client object
secret_client = SecretClient(vault_url= vault_url, credential= credentials)


# retrieve the secret value from key vault
secret_key = secret_client.get_secret(secret_name)

# define parameters
headers = {'Content-type' : 'application/json', 
           'x-functions-key': secret_key.value}

data = {'name':''}

# make the HTTP connection to a function 
response = requests.post(function_url, headers= headers, json=data)

# check the response code and status
if response.status_code == 200 :
    print("Function call is successful")
    print(response.text)

else :
    print("Function call is failed :", response.status_code)
    print(response.text)