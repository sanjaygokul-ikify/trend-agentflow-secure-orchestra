import unittest
from packages.core import Engine, Agent, AgentState, ExecutionResult
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine()
        agent = Agent('test', lambda x: x)
        engine.register_agent(agent)
        orchestrator = Orchestrator(engine)
        result = orchestrator.run('test', 'Hello World')
        self.assertIsInstance(result, ExecutionResult)

if __name__ == '__main__':
    unittest.main()