import time

def call_estimation_api(requirement: str) -> dict:
    """Simulates calling an external enterprise estimation API"""

    # Simulate API latency
    time.sleep(1)

    # Mock response (replace with real API later)
    return {
        "modules": ["Frontend", "Backend", "Database"],
        "effort_days": 25,
        "complexity": "Medium"
    }
