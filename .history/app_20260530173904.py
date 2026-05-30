# procurement-agent/app.py (modified version)

from graph import build_graph
from state import ProcurementState

def run_procurement(requirement: str) -> dict:
    """Run the procurement workflow with a given requirement"""
    # Initialize state with user input
    initial_state = ProcurementState(
        requirement=requirement,
        vendors=[],
        rfq="",
        quotations=[],
        selected_vendor=None,
        po=""
    )
    
    # Build and run the graph
    graph = build_graph()
    final_state = graph.invoke(initial_state)
    
    return final_state

if __name__ == "__main__":
    # Example usage (for standalone testing)
    test_requirement = "We need 1000 FDA-approved rubber seals for medical devices"
    state = run_procurement(test_requirement)
    print("✅ Procurement process completed!")
    print(f"PO generated at: output/generated_po.txt")
    print(f"RFQ generated at: output/generated_rfq.txt")
