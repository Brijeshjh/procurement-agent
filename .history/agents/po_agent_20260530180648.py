from utils.llm import mock_llm
from prompts.po_prompt import PO_PROMPT
import json

def generate_po(state: dict) -> dict:
    quote = state["quotations"][0]
    po = mock_llm(PO_PROMPT.format(
        vendor=quote["vendor"],
        requirement=state["requirement"],
        quantity=1000,
        total=quote["total"],
        delivery_time=quote["delivery_time"]
    ))
    
    # Save to output file
    with open("output/generated_po.txt", "w") as f:
        f.write(po)
    
    return {"po": po}
