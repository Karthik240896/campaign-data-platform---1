from etl.normalize import normalize_row

def test_normalize_maps_fields():
    raw = {"date": "2026-07-01", "campaign_name": "Test", "spend": 10.5, "clicks": 3}
    clean = normalize_row(raw)
    assert clean["campaign"] == "Test"
    assert clean["clicks"] == 3
