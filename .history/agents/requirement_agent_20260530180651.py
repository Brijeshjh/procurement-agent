# procurement-agent/agents/requirement_agent.py
from utils.llm import mock_llm
from prompts.requirement_prompt import REQUIREMENT_PROMPT
import json

def process_requirement(state: dict) -> dict:
    """EXTRACT requirements without modifying the original requirement"""
    # Mock LLM response
    mock_response = """
    {
      "requirement": "1000 units of medical grade rubber seals",
      "quantity": 1000,
      "specifications": [
        "FDA approved", 
        "Temperature range: -20°C to 120°C",
        "Material: Silicone"
      ]
    }
    """
    # In real implementation, you'd parse this
    # For now, we'll just add NEW state keys
    parsed = json.loads(mock_response)
    return {"parsed_requirement": parsed}
