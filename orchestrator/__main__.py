import argparse
import asyncio
import json
from orchestrator.engine import Orchestrator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", choices=["run"])
    parser.add_argument("--goal", required=True)
    args = parser.parse_args()

    if args.cmd == "run":
        orch = Orchestrator()
        results = asyncio.run(orch.run(args.goal))
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
