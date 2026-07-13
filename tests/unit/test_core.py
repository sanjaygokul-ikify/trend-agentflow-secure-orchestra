import unittest
from packages.core import Engine, Agent, AgentState, ExecutionResult

class TestCore(unittest.TestCase):
    def test_agent_state(self):
        engine = Engine()
        agent = Agent('test', lambda x: x)
        engine.register_agent(agent)
        self.assertEqual(engine.get_agent_state('test'), AgentState.PENDING)

    def test_run_agent(self):
        engine = Engine()
        agent = Agent('test', lambda x: x)
        engine.register_agent(agent)
        result = engine.run_agent('test', 'Hello World')
        self.assertIsInstance(result, ExecutionResult)

if __name__ == '__main__':
    unittest.main()