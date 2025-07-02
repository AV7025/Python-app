from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

app = Flask(__name__)

# Fetch Key Vault URL from environment
KEY_VAULT_URL = os.getenv("KEY_VAULT_URL")

# Use DefaultAzureCredential (works locally via az login)
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

@app.route("/")
def get_secret():
    secret = client.get_secret("DatabaseConnectionString")
    return f"✅ Secret Retrieved: {secret.value}"

if __name__ == "__main__":
    app.run(debug=True)
