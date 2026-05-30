from typing import TypedDict, List, Optional

class ProcurementState(TypedDict):
    requirement: str
    vendors: List[str]
    rfq: str
    quotations: List[dict]
    selected_vendor: Optional[str]
    po: str
