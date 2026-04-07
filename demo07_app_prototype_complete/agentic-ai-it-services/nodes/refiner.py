from services.llm_service import call_llm
from utils.prompts import REFINER_PROMPT

def refiner_node(state):
    """Refines solution using human feedback"""

    response = call_llm(
        REFINER_PROMPT,
        f"""
Solution:
{state['solution']}

Feedback:
{state['feedback']}

Refine it.
"""
    )

    return {"refined_solution": response}
