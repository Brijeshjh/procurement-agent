REQUIREMENT_PROMPT = """
Extract procurement requirements from user input. Return JSON with:
{{
  "requirement": "Clear description of what's needed",
  "quantity": "Number of units",
  "specifications": ["List of technical specs"]
}}

User input: {input}
"""
