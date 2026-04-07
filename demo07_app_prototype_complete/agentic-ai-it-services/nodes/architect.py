from services.llm_service import call_llm
from utils.prompts import ARCHITECT_PROMPT

def architect_node(state):
    """Designs solution architecture"""

    requirement = state["requirement"]

    response = call_llm(
        ARCHITECT_PROMPT,
        f"Design solution:\n{requirement}",
        temperature=0.5
    )

    return {"solution": response}
