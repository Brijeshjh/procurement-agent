from langgraph.graph import StateGraph, END
from state import ProcurementState
from agents.requirement_agent import process_requirement
from agents.vendor_agent import find_vendors
from agents.rfq_agent import generate_rfq
from agents.quotation_agent import collect_quotations
from agents.comparison_agent import compare_quotations
from agents.po_agent import generate_po

def build_graph():
    workflow = StateGraph(ProcurementState)
    
    # Add nodes
    workflow.add_node("process_requirement", process_requirement)
    workflow.add_node("vendor", find_vendors)
    workflow.add_node("rfq_node", generate_rfq)
    workflow.add_node("quotation", collect_quotations)
    workflow.add_node("comparison", compare_quotations)
    workflow.add_node("po_node", generate_po)
    
    # Define edges
    workflow.set_entry_point("process_requirement")
    workflow.add_edge("process_requirement", "vendor")
    workflow.add_edge("vendor", "rfq_node")
    workflow.add_edge("rfq_node", "quotation")
    workflow.add_edge("quotation", "comparison")
    workflow.add_edge("comparison", "po_node")
    workflow.add_edge("po_node", END)
    
    return workflow.compile()
