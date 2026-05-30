from utils.llm import mock_llm
from prompts.rfq_prompt import RFQ_PROMPT
import json

def generate_rfq(state: dict) -> dict:
    rfq = mock_llm(RFQ_PROMPT.format(requirement=state["requirement"]))
    
    # Save to output file
    with open("output/generated_rfq.txt", "w") as f:
        f.write(rfq)
    
    state["rfq"] = rfq
    return state
