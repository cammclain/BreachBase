from __future__ import annotations

from temporalio import activity
from app.scans.hosts import Host

@activity.defn(name="VulnResearch")
async def vuln_research(self, host: Host, vuln: Vuln) -> None:
    pass

