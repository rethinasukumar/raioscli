from enum import Enum


class Event(str, Enum):
    NODE_UP = "NODE_UP"
    NODE_DOWN = "NODE_DOWN"
    REGION_DEPLOYED = "REGION_DEPLOYED"
