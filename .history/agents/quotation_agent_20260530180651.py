# procurement-agent/agents/quotation_agent.py
from tools.quotation_tool import get_quotation
import json

def collect_quotations(state: dict) -> dict:
    # Use the PARSED requirement instead of original
    requirement = state["parsed_requirement"]["requirement"]
    
    quotations = []
    for vendor in state["vendors"][:1]:
        quote = get_quotation(vendor, requirement)
        quotations.append(quote)
    
    with open("data/quotations.json", "w") as f:
        json.dump(quotations, f, indent=2)
    
    return {"quotations": quotations}
