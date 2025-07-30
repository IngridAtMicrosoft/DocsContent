import json
import os

def get_resource_endpoints(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    endpoints = []
    for entry in data.get("value", []):
        namespace = entry.get("namespace")
        resource_types = entry.get("resourceTypes", [])
        for resource in resource_types:
            resource_type = resource.get("resourceType")
            api_versions = resource.get("apiVersions", [])
            api_version = resource.get("defaultApiVersion") if "defaultApiVersion" in resource else (api_versions[0] if api_versions else None)
            if not namespace or not resource_type or not api_version:
                continue
            # Construct endpoint pattern
            endpoint = f"https://management.azure.com/providers/{namespace}/{resource_type}?api-version={api_version}"
            endpoints.append({
                "namespace": namespace,
                "resourceType": resource_type,
                "apiVersion": api_version,
                "endpoint": endpoint
            })
    return endpoints

def save_endpoints(endpoints, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(endpoints, f, indent=2)
    print(f"Saved endpoints to {out_path}")

if __name__ == "__main__":
    JSON_PATH = "tools2/data/all-azure-resource-types.json"
    OUT_PATH = "tools2/data/resource_endpoints.json"
    endpoints = get_resource_endpoints(JSON_PATH)
    save_endpoints(endpoints, OUT_PATH)
    print(f"Found {len(endpoints)} endpoints.")
