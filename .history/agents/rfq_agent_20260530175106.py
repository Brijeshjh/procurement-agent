# procurement-agent/agents/rfq_agent.py
from utils.llm import mock_llm
from prompts.rfq_prompt import RFQ_PROMPT
import json

def generate_rfq(state: dict) -> dict:
    # Use parsed requirement
    requirement = state["parsed_requirement"]["requirement"]
    
    rfq = mock_llm(RFQ_PROMPT.format(requirement=requirement))
    
    with open("output/generated_rfq.txt", "w") as f:
        f.write(rfq)
    
    state["rfq"] = rfq
    return state
