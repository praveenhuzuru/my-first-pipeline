import sys

def check_service(service_name, status):
    if status == "up":
        print(f"✅ {service_name} is UP")
        return True
    else:
        print(f"❌ {service_name} is DOWN")
        return False

services = [
    ("Database", "up"),
    ("API Server", "up"),
    ("Cache", "up"),
]

all_healthy = all(check_service(name, status) for name, status in services)

if all_healthy:
    print("\n✅ All systems healthy!")
    sys.exit(0)
else:
    print("\n❌ Some systems are DOWN!")
    sys.exit(1)
