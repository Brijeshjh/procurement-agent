# procurement-agent/agents/requirement_agent.py
from utils.llm import mock_llm
from prompts.requirement_prompt import REQUIREMENT_PROMPT
import json

def process_requirement(state: dict) -> dict:
    # ONLY update parsed data, DON'T modify initial_requirement
    mock_response = """{"parsed": "1000 units of medical grade rubber seals"}"""
    state["parsed_requirement"] = mock_response  # NEW key
    return state
