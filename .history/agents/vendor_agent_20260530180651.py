from tools.vendor_search_tool import search_vendors

def find_vendors(state: dict) -> dict:
    return {"vendors": search_vendors(state["requirement"])}
