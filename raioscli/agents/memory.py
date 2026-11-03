MEMORY = {
    "region": "ap-sg-1",
    "nodes": [
        "cp-1",
        "dp-1"
    ]
}


def get_region():
    return MEMORY["region"]


def get_nodes():
    return MEMORY["nodes"]
