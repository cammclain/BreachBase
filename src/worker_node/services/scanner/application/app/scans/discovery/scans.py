from __future__ import annotations

from temporalio import activity
from bbot.scanner import Scanner
from app.scans.hosts import Host

@activity.defn(name="PortScan")
async def port_scan(self, host: Host) -> None:
    scanner: Scanner = Scanner()
    scanner.scan(host.ip)

    return scanner.results


@activity.defn(name="ServiceScan")
async def service_scan(self, host: Host) -> None:
    pass



@activity.defn(name="VulnScan")
async def vuln_scan(self, host: Host) -> None:
    pass

