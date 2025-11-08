from __future__ import annotations
import time
from dataclasses import dataclass

@dataclass
class ProcessMetrics:
    rows: int = 0
    bad_rows: int = 0
    departments: int = 0
    elapsed_sec: float = 0.0

class Stopwatch:
    def __init__(self) -> None:
        self._start = time.perf_counter()

    def stop(self) -> float:
        return time.perf_counter() - self._start
