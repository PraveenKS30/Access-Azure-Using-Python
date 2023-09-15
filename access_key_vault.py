from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
vault_url = os.environ["AZURE_VAULT_URL"]


secret_name = "ExampleKey"

# create a credential 
credentials = ClientSecretCredential(
    client_id = client_id, 
    client_secret= client_secret,
    tenant_id= tenant_id
)

# create a secret client object
secret_client = SecretClient(vault_url= vault_url, credential= credentials)


# retrieve the secret value from key vault
secret = secret_client.get_secret(secret_name)


print("The secret value is :" + secret.value)