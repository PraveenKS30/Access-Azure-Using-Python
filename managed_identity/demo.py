from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import time

# 1. Configuration
VAULT_URL = "https://kv-demo-3009.vault.azure.net/"
SECRET_NAME = "MySecret"

def get_secret():
    try:
        # 2. This is the heart of the video!
        # It looks for AZ CLI locally or Managed Identity in Azure.
        credential = DefaultAzureCredential()

        # 3. Initialize the client
        client = SecretClient(vault_url=VAULT_URL, credential=credential)

        # 4. Fetch the secret
        print(f"Attempting to fetch '{SECRET_NAME}'...")
        retrieved_secret = client.get_secret(SECRET_NAME)
        
        return f"The secret value is: {retrieved_secret.value}"

    except Exception as e:
        return f"Failed to get secret. Error: {e}"

if __name__ == "__main__":
    print(get_secret())

    # Keep the container alive for 10 minutes so you can see the logs
    print("Container will stay alive for 10 minutes for demo purposes...")
    time.sleep(600)