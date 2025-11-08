from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import csv
from typing import Dict, IO
from ..utils.validators import validate_row
from ..utils.metrics import ProcessMetrics, Stopwatch

def aggregate_sales_from_csv(
    input_path: Path,
    output_path: Path,
) -> ProcessMetrics:
    """
    Stream-read input_path, aggregate per department, write output_path.
    Memory usage is O(d) where d = #unique departments.
    """
    metrics = ProcessMetrics()
    totals: Dict[str, int] = defaultdict(int)
    sw = Stopwatch()

    with input_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        # Skip header if present by peeking first row
        first = next(reader, None)
        if first is not None:
            if _looks_like_header(first):
                pass  # already consumed header
            else:
                _process_row(first, totals, metrics)
        for row in reader:
            _process_row(row, totals, metrics)

    metrics.departments = len(totals)

    with output_path.open("w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["Department Name", "Total Number of Sales"])
        for dept, total in sorted(totals.items()):
            writer.writerow([dept, total])

    metrics.elapsed_sec = sw.stop()
    return metrics

def _looks_like_header(row: list[str]) -> bool:
    joined = ",".join([c.strip().lower() for c in row])
    return joined.startswith("department") and "number of sales" in joined

def _process_row(row: list[str], totals, metrics: ProcessMetrics) -> None:
    metrics.rows += 1
    ok, err = validate_row(row)
    if not ok:
        metrics.bad_rows += 1
        return
    dept = row[0].strip()
    sales = int(row[2].strip())
    totals[dept] += sales
