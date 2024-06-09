from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, CredentialUnavailableError
import os
import logging

load_dotenv()

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Example 1: Using DefaultAzureCredential with Azure Key Vault to retrieve a secret
try :

    credentials = DefaultAzureCredential()
    vault_url = os.environ["AZURE_VAULT_URL"]

    secret_name = "ExampleKey"


    # create a secret client object
    secret_client = SecretClient(vault_url= vault_url, credential= credentials)


    # retrieve the secret value from key vault
    secret = secret_client.get_secret(secret_name)


    print("The secret value is :" + secret.value)

except CredentialUnavailableError:
    print("Failed to authenticate with DefaultAzureCredential. Please check your environment setup.")
