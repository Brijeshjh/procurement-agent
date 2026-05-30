def get_quotation(vendor: str, rfq: str) -> dict:
    """Mock quotation generator"""
    return {
        "vendor": vendor,
        "price_per_unit": 2.50,
        "total": 2500.00,
        "delivery_time": "14 days",
        "comments": "FDA certified - meets all specs"
    }
