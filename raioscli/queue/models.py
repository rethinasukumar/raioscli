from dataclasses import dataclass
from datetime import datetime


@dataclass
class QueueMessage:
    id: str
    body: str
    created_at: datetime
    receive_count: int = 0
