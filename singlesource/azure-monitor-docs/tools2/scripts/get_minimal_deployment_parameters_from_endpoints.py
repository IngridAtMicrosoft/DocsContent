import requests
import json
from azure_utils import get_bearer_token
from typing import Optional

def get_resource_schema_url(resource_type: str, api_version: Optional[str] = None):
    base_url = "https://schema.management.azure.com/schemas/"
    # Common path format
    if not api_version:
        # Default fallback for demo purposes (you can make this dynamic)
        api_version = "2023-04-01"

    namespace, type_name = resource_type.split("/", 1)
    schema_file = f"{namespace}/{type_name}/{api_version}.json"
    return f"{base_url}{schema_file}"

def fetch_schema(url: str):
    if "management.azure.com/schemas/" in url:
        # Public schema endpoint, no auth header
        response = requests.get(url)
    else:
        token = get_bearer_token()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Schema not found (404) for {url}. Skipping.")
        return None
    else:
        print(f"Failed to fetch schema from {url} (Status: {response.status_code})")
        return None

def extract_required_properties(schema):
    # This function assumes standard ARM template structure
    try:
        # Dive into the resource definition
        resource_def = schema["resourceDefinitions"]
        first_resource = next(iter(resource_def.values()))
        required_props = first_resource.get("required", [])
        print("*************REQUIRED*************")
        print(required_props)
        return required_props
    except Exception as e:
        print("Error extracting properties:", e)
        return []


if __name__ == "__main__":
    ENDPOINTS_JSON = "tools2/data/resource_endpoints.json"
    OUT_JSON = "tools2/data/minimal_required_properties.json"
    with open(ENDPOINTS_JSON, "r", encoding="utf-8") as f:
        endpoints = json.load(f)
    results = []
    for entry in endpoints:
        resource_type = f"{entry['namespace']}/{entry['resourceType']}"
        api_version = entry.get("apiVersion")
        schema_url = get_resource_schema_url(resource_type, api_version)
        print(f"Fetching schema from: {schema_url}")
        schema_json = fetch_schema(schema_url)
        if schema_json:
            required_fields = extract_required_properties(schema_json)
        else:
            required_fields = []
        results.append({
            "resourceType": resource_type,
            "apiVersion": api_version,
            "requiredProperties": required_fields
        })
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Saved minimal required properties for all resources to {OUT_JSON}")
