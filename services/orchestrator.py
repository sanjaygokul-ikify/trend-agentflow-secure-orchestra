from .types import Engine

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def run(self, agent_id: str, input_data: any):
        result = self.engine.run_agent(agent_id, input_data)
        return result