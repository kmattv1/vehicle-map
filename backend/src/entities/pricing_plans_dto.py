from dataclasses import dataclass
from typing import List


@dataclass(order=True, frozen=True)
class PerMinPricing:
    start: int
    rate: float
    interval: int


@dataclass(order=True, frozen=True)
class Plan:
    plan_id: str
    name: str
    currency: str
    price: int
    is_taxable: bool
    description: str
    per_min_pricing: List[PerMinPricing]


@dataclass
class Plans:
    plans: List[Plan]


@dataclass
class PricingPlansResponse:
    data: Plans
