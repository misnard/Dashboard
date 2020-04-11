import enum


class InvoiceStatus(enum.Enum):
    pending = 0
    paid = 1
    closed = 2
