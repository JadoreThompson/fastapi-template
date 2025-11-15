from typing import Any
from uuid import UUID, uuid4

from pydantic import Field

from core.enums import CoreEventType
from core.models import CustomBaseModel
from utils.db import get_datetime


class CoreEvent(CustomBaseModel):
    type: CoreEventType
    data: Any
    id: UUID = Field(default_factory=uuid4)
    timestamp: int = Field(default_factory=lambda: int(get_datetime().timestamp()))
