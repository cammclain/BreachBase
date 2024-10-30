from __future__ import annotations

from temporalio import activity

@activity.defn(name="SummarizeScanResults")
async def summarize_scan_results(self, data: str) -> None:

    # 1. Fetch the scan results from SurrealDB
    # 2. Send the scan results to Ollama for summarization
    # 3. Save the summarized results back to SurrealDB
    # return the summarized results
    pass

