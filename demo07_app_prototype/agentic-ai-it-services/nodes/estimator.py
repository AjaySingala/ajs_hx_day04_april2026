from services.llm_service import call_llm
from tools.estimator_tool import estimation_tool

def estimator_node(state):
    """Estimator that can call external API via tool"""

    # TODO: Extract the requirement from the state.
    requirement = ___

    # Step 1: Ask LLM if tool should be used
    # TODO: Call the llm with the requirement and ask it to decide whether to use estimation tool.
    # If the estimation is required, it should respond "USE_TOOL", otherwise "NO_TOOL".
    decision = call_llm(
        ___
    )


    # Step 2: Tool execution path
    # TODO: If LLM returns "USE_TOOL" call the estimation tool with the requirement.
    # Return the tool result as the estimate.
    ___


    # Step 3: Fallback to LLM estimation
    # TODO: If LLM returns "NO_TOOL", call the LLM to get an estimate directly.
    # Define the role as "software estimator".
    # Provide the requirement in the prompt and ask for an effort estimation.
    response = call_llm(
        ___
    )

    return {"estimate": response}
