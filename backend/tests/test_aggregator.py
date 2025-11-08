from pathlib import Path
from backend.app.core.aggregator import aggregate_sales_from_csv

def test_aggregate_basic(tmp_path: Path):
    input_csv = tmp_path / "in.csv"
    output_csv = tmp_path / "out.csv"
    input_csv.write_text(
        "Department Name,Date,Number of Sales\n"
        "Electronics,2023-08-01,100\n"
        "Clothing,2023-08-01,200\n"
        "Electronics,2023-08-02,150\n",
        encoding="utf-8"
    )
    metrics = aggregate_sales_from_csv(input_csv, output_csv)
    assert metrics.rows == 3
    out = output_csv.read_text(encoding="utf-8").strip().splitlines()
    assert out[0] == "Department Name,Total Number of Sales"
    assert "Electronics,250" in out[1:] and "Clothing,200" in out[1:]
