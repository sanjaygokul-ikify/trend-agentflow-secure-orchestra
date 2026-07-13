import unittest
from packages.core import Engine, Agent, AgentState, ExecutionResult

class TestRuntime(unittest.TestCase):
    def test_shutdown(self):
        engine = Engine()
        agent = Agent('test', lambda x: x)
        engine.register_agent(agent)
        engine.shutdown()
        self.assertEqual(engine.get_agent_state('test'), AgentState.TERMINATED)

if __name__ == '__main__':
    unittest.main()