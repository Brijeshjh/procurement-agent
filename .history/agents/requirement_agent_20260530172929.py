from utils.llm import mock_llm
from prompts.requirement_prompt import REQUIREMENT_PROMPT

def process_requirement(state: dict) -> dict:
    # Mock LLM response - in reality would call real LLM
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
    result = mock_llm(REQUIREMENT_PROMPT.format(input=state["requirement"]))
    
    # In real project: Parse LLM response with parser.py
    state["requirement"] = "1000 units of medical grade rubber seals"
    return state
