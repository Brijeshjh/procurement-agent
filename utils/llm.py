def mock_llm(prompt: str) -> str:
    """Simulates LLM response without external API calls"""
    if "RFQ" in prompt:
        return f"""RFP #2024-001
Medical Grade Rubber Seals RFQ

Product: FDA-approved silicone rubber seals
Quantity: 1,000 units
Delivery: Within 2 weeks
Requirements: 
- Must meet ISO 13485 standards
- Batch traceability required
- Packaging: Sterile individual units"""
    
    elif "Purchase Order" in prompt:
        return f"""PO #78945
Vendor: MediSeal Inc.
Items: 1,000 medical grade rubber seals
Total: $2,500.00
Delivery: 14 days
Payment terms: Net 30"""
    
    return "Mock LLM response"
