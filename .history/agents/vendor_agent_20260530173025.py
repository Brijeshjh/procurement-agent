from tools.vendor_search_tool import search_vendors

def find_vendors(state: dict) -> dict:
    state["vendors"] = search_vendors(state["requirement"])
    return state
