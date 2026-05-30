from tools.quotation_tool import get_quotation
import json

def collect_quotations(state: dict) -> dict:
    quotations = []
    for vendor in state["vendors"][:1]:  # Only first vendor for simplicity
        quote = get_quotation(vendor, state["rfq"])
        quotations.append(quote)
    
    # Save to data file
    with open("data/quotations.json", "w") as f:
        json.dump(quotations, f, indent=2)
    
    state["quotations"] = quotations
    return state
