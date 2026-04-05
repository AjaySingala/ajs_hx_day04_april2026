from services.llm_service import call_llm
from utils.prompts import KNOWLEDGE_PROMPT

def knowledge_node(state):
    """Answers using internal knowledge"""

    query = state["requirement"]

    response = call_llm(
        KNOWLEDGE_PROMPT,
        f"Answer this IT query:\n{query}"
    )

    return {"knowledge_answer": response}
