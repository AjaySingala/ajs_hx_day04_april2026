from services.llm_service import call_llm
from utils.prompts import ARCHITECT_PROMPT

def architect_node(state):
    """Designs solution architecture"""

    # TODO: Extract the requirement from the state.
    requirement = ___

    # TODO: Call the llm with the architect prompt and the requirement to get the solution design.
    # Set the temperature to 0.5.
    response = call_llm(
        ___
    )

    return {"solution": response}
