from decimal import Decimal

def normalize_row(raw: dict) -> dict:
    return {
        "date": raw["date"],
        "campaign": raw["campaign_name"],
        "spend": Decimal(str(raw.get("spend") or 0)),
        "clicks": raw.get("clicks"),
        "conversions": raw.get("conversions"),
        "revenue": Decimal(str(raw.get("revenue") or 0)),
        "currency": raw.get("currency", "EUR"),
    }
