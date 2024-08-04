from typing import List, Dict, Optional
from pydantic import BaseModel
from uuid import UUID, uuid4


class Job(BaseModel):
    id: Optional[int] = None
    title: str
    statistics: dict