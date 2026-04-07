from config.azure_openai import client, deployment

def call_llm(system_prompt, user_prompt, temperature=0.3):
    """Reusable function to call Azure OpenAI chat API"""

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature
    )

    return response.choices[0].message.content
