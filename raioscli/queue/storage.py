from pathlib import Path
import json

QUEUE_ROOT = Path(".raios/queue")


def ensure():
    QUEUE_ROOT.mkdir(
        parents=True,
        exist_ok=True
    )


def queue_file(name: str):
    ensure()
    return QUEUE_ROOT / f"{name}.json"


def load(name: str):
    file = queue_file(name)

    if not file.exists():
        return []

    return json.loads(
        file.read_text()
    )


def save(name: str, data):
    queue_file(name).write_text(
        json.dumps(data, indent=2)
    )
