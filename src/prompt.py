from typing import List


def aggregate_responses(responses: List[str]):
    return "\n---\n".join(f"{r}" for r in responses)
