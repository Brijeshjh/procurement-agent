def compare_quotations(state: dict) -> dict:
    # In real project: Compare multiple quotes
    # Simplified: Select first vendor
    state["selected_vendor"] = state["quotations"][0]["vendor"]
    return state
