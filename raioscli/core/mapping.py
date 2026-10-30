import yaml
from pathlib import Path

_mapping_cache = None

def load_mapping():
    global _mapping_cache
    if _mapping_cache is None:
        path = Path(__file__).parent / "mapping.yaml"
        _mapping_cache = yaml.safe_load(path.read_text())
    return _mapping_cache

def resolve_service(canonical: str, provider: str) -> str:
    mapping = load_mapping()
    return mapping["services"][canonical][provider]

