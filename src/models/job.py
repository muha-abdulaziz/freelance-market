from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Job:
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    def to_dict(self) -> dict[str, Any]:
        return {
            "id":self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
