PO_PROMPT = """
Generate Purchase Order for:
Vendor: {vendor}
Item: {requirement}
Quantity: {quantity}
Total: ${total:.2f}
Delivery: {delivery_time}

Format as formal business document.
"""
