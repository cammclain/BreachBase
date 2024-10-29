from __future__ import annotations

from temporalio import workflow

from dataclasses import dataclass


@dataclass
class Service:
    port: int
    protocol: str

@dataclass
class Host:
    ip: str
    port: int
    protocol: str
    services: list[Service]


@workflow.defn(name="ScanHosts")
class ScanHosts:
    @workflow.run
    async def run(self) -> None:
        pass





