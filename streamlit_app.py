import streamlit as st
import os
import time
from app import run_procurement  # Import the core function from your agent

# --- Configure Page ---
st.set_page_config(
    page_title="Procurement Agent",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Professional Look ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        height: 3.5rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1a5f8f;
    }
    .output-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #1f77b4;
    }
    .header {
        color: #1f77b4;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- Main App Logic ---
st.title("🤖 AI Procurement Agent")
st.subheader("Streamline your procurement process with AI automation")

# Initialize session state
if 'procurement_done' not in st.session_state:
    st.session_state.procurement_done = False

# Requirement Input Section
with st.container(border=True):
    st.markdown("<h3 class='header'>1. Enter Procurement Requirement</h3>", unsafe_allow_html=True)
    requirement = st.text_area(
        "Describe what you need to purchase:",
        height=150,
        placeholder="e.g., 1000 FDA-approved rubber seals for medical devices, 12V DC motors for robotics, etc.",
        key="requirement_input"
    )

# Action Buttons
col1, col2 = st.columns([1, 4])
with col1:
    run_button = st.button("🚀 Run Procurement", use_container_width=True, disabled=not requirement)

# Process when button is clicked
if run_button:
    with st.spinner("Processing your request... This may take 15-30 seconds"):
        # Clear previous outputs
        st.session_state.procurement_done = False
        st.session_state.rfq_content = None
        st.session_state.po_content = None
        
        # Run the procurement workflow
        try:
            # Call your agent's main function
            result = run_procurement(requirement)
            
            # Check if outputs were generated
            rfq_path = "output/generated_rfq.txt"
            po_path = "output/generated_po.txt"
            
            if os.path.exists(rfq_path) and os.path.exists(po_path):
                with open(rfq_path, 'r') as f:
                    st.session_state.rfq_content = f.read()
                with open(po_path, 'r') as f:
                    st.session_state.po_content = f.read()
                
                st.session_state.procurement_done = True
                st.success("✅ Procurement workflow completed successfully!")
            else:
                st.error("Output files not generated. Check agent execution.")
        except Exception as e:
            st.error(f"Error running procurement: {str(e)}")
            st.code(str(e), language="python")

# Show results when procurement is done
if st.session_state.procurement_done:
    # RFQ Section
    st.markdown("<h3 class='header'>2. Generated Request for Quotation (RFQ)</h3>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<div class='output-container'>", unsafe_allow_html=True)
        st.text_area("RFQ Document", st.session_state.rfq_content, height=300, disabled=True)
        st.download_button(
            "Download RFQ",
            st.session_state.rfq_content,
            file_name="generated_rfq.txt",
            mime="text/plain",
            use_container_width=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    # PO Section
    st.markdown("<h3 class='header'>3. Generated Purchase Order (PO)</h3>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<div class='output-container'>", unsafe_allow_html=True)
        st.text_area("Purchase Order", st.session_state.po_content, height=300, disabled=True)
        st.download_button(
            "Download PO",
            st.session_state.po_content,
            file_name="generated_po.txt",
            mime="text/plain",
            use_container_width=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

# --- Sidebar Instructions ---
with st.sidebar:
    st.title("ℹ️ How to Use")
    st.markdown("""
    1. **Enter Requirement**  
       Describe your procurement need in detail
   
    2. **Run Procurement**  
       Click the button to start the AI workflow
   
    3. **Review Outputs**  
       Check the generated RFQ and PO documents
   
    4. **Download Documents**  
       Save files for official use
    
    **Note**: This demo uses mock data. In production, it would connect to:
    - Vendor databases
    - CRM systems
    - Document management APIs
    """)

    st.divider()
    st.info("For demonstration purposes only. Actual implementation would include API integrations and security measures.")

# --- Footer ---
st.divider()
st.caption("Procurement Agent | Powered by LangGraph | © 2024")
