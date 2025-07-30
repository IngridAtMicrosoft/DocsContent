# azure_utils.py
import json
import subprocess
from azure.identity import AzureCliCredential

def get_credential():
    return AzureCliCredential()

def get_credentials():
    """Alias for get_credential() for compatibility"""
    return get_credential()

def get_subscription_id():
    """Get subscription ID using Azure CLI"""
    try:
        # Try with shell=True for Windows compatibility
        result = subprocess.run(
            "az account show --output json",
            capture_output=True,
            text=True,
            shell=True,
            check=True
        )
        return json.loads(result.stdout)["id"]
    except FileNotFoundError:
        print("❌ Azure CLI 'az' command not found. Make sure Azure CLI is installed and in PATH.")
        raise
    except subprocess.CalledProcessError as e:
        print(f"❌ Azure CLI command failed: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        raise
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse Azure CLI output: {e}")
        raise

def get_bearer_token():
    credential = get_credential()
    token = credential.get_token("https://management.azure.com/.default")
    return token.token

def find_log_analytics_workspace(client, resource_group, name_filter="log", use_sdk=True):
    """Find a Log Analytics workspace in the specified resource group"""
    if use_sdk and client:
        # Using SDK-based lookup
        workspaces = client.workspaces.list_by_resource_group(resource_group)
        for workspace in workspaces:
            if name_filter.lower() in workspace.name.lower():
                return workspace
    else:
        # REST API based lookup for compatibility with list-tables.py
        credential = get_credential()
        subscription_id = get_subscription_id()
        token = credential.get_token("https://management.azure.com/.default").token
        
        import requests
        headers = {"Authorization": f"Bearer {token}"}
        url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.OperationalInsights/workspaces?api-version=2021-06-01"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            workspaces = response.json().get("value", [])
            for workspace in workspaces:
                if name_filter.lower() in workspace["name"].lower():
                    return workspace
    
    return None
