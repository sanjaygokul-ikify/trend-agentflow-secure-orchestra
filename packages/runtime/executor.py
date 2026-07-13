import logging
from typing import Any, Dict, List
from . import Executor

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, core_engine):
        self.core_engine = core_engine

    def execute_agent(self, agent_id: str, input_data: Any) -> Any:
        result = self.core_engine.run_agent(agent_id, input_data)
        return result.result

    def get_agent_state(self, agent_id: str) -> str:
        state = self.core_engine.get_agent_state(agent_id)
        return state.name
