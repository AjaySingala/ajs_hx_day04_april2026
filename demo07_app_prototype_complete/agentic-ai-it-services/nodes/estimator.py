from services.llm_service import call_llm
from tools.estimator_tool import estimation_tool

def estimator_node(state):
    """Estimator that can call external API via tool"""

    requirement = state["requirement"]

    # Step 1: Ask LLM if tool should be used
    decision = call_llm(
        "You decide whether to use estimation tool.",
        f"""
Requirement:
{requirement}

If estimation is needed, respond ONLY with:
USE_TOOL

Otherwise respond:
NO_TOOL
"""
    )

    # Step 2: Tool execution path
    if "USE_TOOL" in decision:
        tool_result = estimation_tool(requirement)

        return {"estimate": tool_result}

    # Step 3: Fallback to LLM estimation
    response = call_llm(
        "You are a software estimator.",
        f"Estimate effort:\n{requirement}"
    )

    return {"estimate": response}
