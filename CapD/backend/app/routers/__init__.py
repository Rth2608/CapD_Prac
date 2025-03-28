import importlib
import pkgutil

all_routers = []

for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name == "__init__":
        continue
    module = importlib.import_module(f"{__name__}.{module_name}")
    if hasattr(module, "router"):
        router = getattr(module, "router")
        prefix = getattr(module, "prefix", "")
        tags = getattr(module, "tags", [])
        all_routers.append((router, prefix, tags))
