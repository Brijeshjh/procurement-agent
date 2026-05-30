# procurement-agent/agents/rfq_agent.py
from utils.llm import mock_llm
from prompts.rfq_prompt import RFQ_PROMPT
import json

def generate_rfq(state: dict) -> dict:
    # Use the original requirement without modifying it
    requirement = state["initial_requirement"]  # CORRECT reference
    rfq = mock_llm(RFQ_PROMPT.format(requirement=requirement))
    # ... rest remains same

    with open("output/generated_rfq.txt", "w") as f:
        f.write(rfq)
    
    return {"rfq": rfq}
