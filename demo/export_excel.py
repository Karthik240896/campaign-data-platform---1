import pandas as pd
from etl.normalize import normalize_row

fake_raw_rows = [
    {"date": "2026-07-01", "campaign_name": "Summer Sale", "spend": 120.50, "clicks": 45, "conversions": 3, "revenue": 400.0, "currency": "EUR"},
    {"date": "2026-07-02", "campaign_name": "Brand Awareness", "spend": 80.0, "clicks": 20, "conversions": 1, "revenue": 90.0, "currency": "EUR"},
]

clean_rows = [normalize_row(r) for r in fake_raw_rows]
df = pd.DataFrame(clean_rows)
df.to_excel("demo/sample_output.xlsx", index=False, sheet_name="Google Ads")
print("Written demo/sample_output.xlsx")
