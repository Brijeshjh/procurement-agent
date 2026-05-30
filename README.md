# AI Procurement Agent

A streamlined, AI-powered agent built with LangGraph to automate the procurement process. It takes a procurement requirement (e.g., "We need 1000 FDA-approved rubber seals") and automates the generation of key procurement documents like Requests for Quotation (RFQ) and Purchase Orders (PO). 

The project includes a sleek, user-friendly UI built with Streamlit.

## Features

- **Automated Workflow:** Uses an AI graph-based workflow (LangGraph) to process procurement requirements.
- **RFQ Generation:** Automatically drafts a Request for Quotation based on the given requirement.
- **PO Generation:** Creates a final Purchase Order document.
- **Interactive UI:** Provides a web-based dashboard (Streamlit) for users to input requirements and view/download the generated RFQ and PO documents.

## Project Structure

- `app.py`: Contains the core entry point for the backend procurement logic and workflow state initialization.
- `graph.py` & `state.py`: Defines the LangGraph workflow nodes and the state object that passes through the pipeline.
- `streamlit_app.py`: The frontend UI application.
- `agents/`: Contains logic for the individual agent nodes (e.g., RFQ generation, vendor selection).
- `data/` & `output/`: Directories for mock vendor data and the output files (generated RFQ/PO).
- `prompts/`: Contains the prompt templates used by the AI agents.
- `tools/` & `utils/`: Helper functions and tools for the agents.

## Installation

1. **Clone the repository and navigate into it.**
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Requires: `langgraph`, `pydantic`, `streamlit`)*
4. **Set up environment variables:**
   If you need specific API keys for the LLM being used, configure them in the `.env` file.

## Usage

### Using the Web UI
Run the Streamlit application to use the interactive dashboard:

```bash
streamlit run streamlit_app.py
```

This will open a web browser window where you can:
1. Enter your procurement requirement.
2. Click "Run Procurement".
3. Review and download the generated documents.

### Running Programmatically
You can also run the agent standalone for testing purposes using:

```bash
python app.py
```
This runs the predefined test requirement and outputs the documents to the `output/` directory.

## License

This project is open-source and available under the terms of the LICENSE file included in the repository.
