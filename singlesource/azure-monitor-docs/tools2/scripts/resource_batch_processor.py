import subprocess
import json
from azure_utils import get_credential, get_bearer_token, get_subscription_id

# FUNCTIONS
"""
Get all Azure Resources data and put it in a JSON file.
"""
def get_azure_resources():
    print("Getting list of all Azure Resources using REST API")
    token = get_bearer_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = "https://management.azure.com/providers?api-version=2021-04-01"
    import requests
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching providers: {response.status_code} {response.text}")
        return
    data = response.json()
    # Only include providers that start with 'Microsoft.'
    filtered = {
        "value": [prov for prov in data.get("value", []) if prov.get("namespace", "").startswith("Microsoft.")]
    }
    output = json.dumps(filtered, indent=2)
    print("Writing filtered list to a JSON file.")
    folder = "tools2\\data\\"
    filename = "all-azure-resource-types.json"
    filepath = folder + filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output)

def main():
    get_azure_resources()


if __name__ == "__main__":
    main()
