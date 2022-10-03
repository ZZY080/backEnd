from dataclasses import dataclass


@dataclass
class ServerStatus:
    python_version: str
    system_description: str

    system_cpu_present: float
    system_memory_usage: float
    app_memory_usage: float

    system_uptime: str
    app_uptime: str

    app_name: str
