from config.azure_openai import client, deployment

def call_llm(system_prompt, user_prompt, temperature=0.3):
    """Reusable function to call Azure OpenAI chat API"""

    # TODO: Call the Azure OpenAI API using the client object.
    # Set the model, messages and temperature parameters.
    # The messages should include a system and a user message with their respective prompts.
    response = ___

    return response.choices[0].message.content
