from typing import TypedDict, List, Optional

class ProcurementState(TypedDict, total=False):
    requirement: str          # Original user input (UNTOUCHED)
    parsed_requirement: dict  # NEW - from agent processing
    vendors: List[str]
    rfq: str
    quotations: List[dict]
    selected_vendor: Optional[str]
    po: str
