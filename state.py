from typing import TypedDict, List, Optional

class ProcurementState(TypedDict):
    initial_requirement: str  # RENAMED from 'requirement'
    vendors: List[str]
    rfq: str
    quotations: List[dict]
    selected_vendor: Optional[str]
    po: str
