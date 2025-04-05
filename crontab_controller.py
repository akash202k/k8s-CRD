from kubernetes import client, config, watch

# Load kubeconfig (works inside cluster or from your local ~/.kube/config)
config.load_kube_config()

# Define the API for Custom Resources
crd_api = client.CustomObjectsApi()

group = "k8s.akashpawar.com"  # Correct group name here
version = "v1"  # Version of your custom resource
namespace = "default"  # The namespace where the resource is located
plural = "crontabs"  # Plural name of the custom resource

# Start watching for changes
w = watch.Watch()
print("🔍 Watching for CronTab resources...")

for event in w.stream(crd_api.list_namespaced_custom_object, group, version, namespace, plural):
    cr = event['object']
    event_type = event['type']
    name = cr['metadata']['name']
    spec = cr.get('spec', {})

    print(f"\n🌀 Event: {event_type} CronTab: {name}")
    print(f"   ➤ Cron Schedule: {spec.get('cronSpec')}")
    print(f"   ➤ Image: {spec.get('image')}")
    print(f"   ➤ Replicas: {spec.get('replicas')}")
