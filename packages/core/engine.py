import logging
from typing import Any, Dict, List
from datetime import datetime
from .types import Agent, AgentState, ExecutionResult
from .exceptions import InvalidAgentStateError, ExecutionError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents = {}
        self.agent_states = {}
        self.executor = None

    def register_agent(self, agent: Agent):
        self.agents[agent.id] = agent
        self.agent_states[agent.id] = AgentState.PENDING

    def run_agent(self, agent_id: str, input_data: Any) -> ExecutionResult:
        if agent_id not in self.agents:
            raise InvalidAgentStateError('Agent not registered')

        agent = self.agents[agent_id]
        state = self.agent_states[agent_id]

        if state == AgentState.RUNNING:
            raise InvalidAgentStateError('Agent is already running')

        self.agent_states[agent_id] = AgentState.RUNNING

        try:
            result = agent.execute(input_data)
            self.agent_states[agent_id] = AgentState.COMPLETED
            return ExecutionResult(result, None)
        except Exception as e:
            self.agent_states[agent_id] = AgentState.FAILED
            return ExecutionResult(None, str(e))

    def get_agent_state(self, agent_id: str) -> AgentState:
        return self.agent_states.get(agent_id, AgentState.UNKNOWN)

    def shutdown(self):
        for agent_id in self.agents:
            self.agent_states[agent_id] = AgentState.TERMINATED

class ExecutionResult:
    def __init__(self, result: Any, error: str):
        self.result = result
        self.error = error

    def __str__(self):
        if self.error:
            return f'Error: {self.error}'
        else:
            return str(self.result)

