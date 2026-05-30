def run_procurement(requirement: str) -> dict:
    initial_state = ProcurementState(
        initial_requirement=requirement,  # Use new name
        vendors=[],
        rfq="",
        quotations=[],
        selected_vendor=None,
        po=""
    )
    # ... rest remains same
