from __future__ import annotations

from temporalio import worker
from app.summarizer import SummarizeScanResults

def main() -> None:
    worker.run(SummarizeScanResults)
