from datetime import datetime
from uuid import UUID

from core.enums import PricingTierType
from core.models import CustomBaseModel


class JWTPayload(CustomBaseModel):
    sub: UUID
    em: str
    exp: datetime
    pricing_tier: PricingTierType
    authenticated: bool
