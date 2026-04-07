from services.api_service import call_estimation_api

def estimation_tool(requirement: str) -> str:
    """Tool that wraps external API call"""

    result = call_estimation_api(requirement)

    return f"""
Estimation Result:
Modules: {result['modules']}
Effort: {result['effort_days']} days
Complexity: {result['complexity']}
"""
