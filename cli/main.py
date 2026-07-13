import argparse
from packages.utils.logging import Logger
from services.orchestrator import Orchestrator
from packages.core import Engine, Agent

def main():
    parser = argparse.ArgumentParser(description='Distributed Multi-Agent Orchestration Framework')
    parser.add_argument('--agent_id', type=str, help='Agent ID')
    parser.add_argument('--input_data', type=str, help='Input Data')
    args = parser.parse_args()

    engine = Engine()
    agent = Agent('test', lambda x: x)
    engine.register_agent(agent)

    orchestrator = Orchestrator(engine)
    result = orchestrator.run(args.agent_id, args.input_data)
    logger = Logger('cli')
    logger.info(f'Result: {result}')

if __name__ == '__main__':
    main()