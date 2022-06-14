from datetime import datetime
from typing import Any, List

from pydantic import BaseModel


class Description(BaseModel):
    key: str
    value: str


class Invoice(BaseModel):
    amount: int
    brcode: str
    created: datetime
    descriptions: List[Description]
    discountAmount: int
    discounts: List[Any]
    due: datetime
    expiration: int
    fee: int
    fine: float
    fineAmount: int
    id: str
    interest: float
    interestAmount: int
    link: str
    name: str
    nominalAmount: int
    pdf: str
    status: str
    tags: List[str]
    taxId: str
    transactionIds: List[Any]
    updated: datetime


class Log(BaseModel):
    created: datetime
    errors: List[Any]
    id: str
    invoice: Invoice
    type: str


class Event(BaseModel):
    created: datetime
    id: str
    log: Log
    subscription: str
    workspaceId: str


class WebhookCallback(BaseModel):
    event: Event


class WebhookResponse(BaseModel):
    transfer_created: bool
    invoice_type: str
