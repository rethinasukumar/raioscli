# raioscli/agents/events.py

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


class EventType(str, Enum):
    NODE_UP = "NODE_UP"
    NODE_DOWN = "NODE_DOWN"
    REGION_DEPLOYED = "REGION_DEPLOYED"
    REGION_DESTROYED = "REGION_DESTROYED"
    TASK_STARTED = "TASK_STARTED"
    TASK_COMPLETED = "TASK_COMPLETED"
    TASK_FAILED = "TASK_FAILED"


@dataclass
class Event:
    event_type: EventType
    source: str
    payload: Dict[str, Any] | None = None
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": self.event_type.value,
            "source": self.source,
            "payload": self.payload or {},
            "timestamp": self.timestamp,
        }
