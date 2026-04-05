from typing import TypedDict, Optional

# Shared state passed between nodes
class AgentState(TypedDict):
    requirement: str
    knowledge_answer: Optional[str]
    estimate: Optional[str]
    solution: Optional[str]
    refined_solution: Optional[str]
    feedback: Optional[str]
