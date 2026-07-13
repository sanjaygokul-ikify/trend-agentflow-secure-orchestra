from enum import Enum
from typing import Any

class AgentState(Enum):
    UNKNOWN = 0
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3
    FAILED = 4
    TERMINATED = 5

class Agent:
    def __init__(self, id: str, execute: callable):
        self.id = id
        self.execute = execute

class ExecutionResult:
    def __init__(self, result: Any, error: str):
        self.result = result
        self.error = error