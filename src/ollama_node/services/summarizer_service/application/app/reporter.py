from __future__ import annotations

from temporalio import workflow
from .researcher import vuln_research
from .summarizer import summarize_scan_results
@workflow.defn(name="HostReporter")
class HostReporter:
    @workflow.run
    async def run(self) -> None:
        return await workflow.execute_activity(
            #vuln_research,
            summarize_scan_results,

        )


