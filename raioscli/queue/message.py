from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class Message:
    id: str
    body: str
    created_at: str

    @classmethod
    def create(cls, body: str):
        return cls(
            id=str(uuid.uuid4()),
            body=body,
            created_at=datetime.utcnow().isoformat()
        )
