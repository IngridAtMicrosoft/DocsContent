import json
import os

def get_minimal_deployment_template(namespace, resource_type):
    # This function returns a generic minimal deployment template for a resource type
    # For most Azure resources, the minimal template includes: name, type, apiVersion, location, and an empty properties object
    # Some resources may require additional parameters, but this is the most common minimal set
    template = {
        "type": f"{namespace}/{resource_type}",
        "apiVersion": "latest",
        "name": "<resourceName>",
        "location": "<location>",
        "properties": {}
    }
    return template


def process_resource_endpoints(endpoints_json, out_json):
    with open(endpoints_json, "r", encoding="utf-8") as f:
        endpoints = json.load(f)
    results = []
    for entry in endpoints:
        namespace = entry.get("namespace")
        resource_type = entry.get("resourceType")
        api_version = entry.get("apiVersion") or "latest"
        template = get_minimal_deployment_template(namespace, resource_type)
        template["apiVersion"] = api_version
        results.append({
            "namespace": namespace,
            "resourceType": resource_type,
            "apiVersion": api_version,
            "minimalDeploymentTemplate": template
        })
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Saved minimal deployment templates to {out_json}")

if __name__ == "__main__":
    ENDPOINTS_JSON = "tools2/data/resource_endpoints.json"
    OUT_JSON = "tools2/data/minimal_deployment_templates.json"
    process_resource_endpoints(ENDPOINTS_JSON, OUT_JSON)
