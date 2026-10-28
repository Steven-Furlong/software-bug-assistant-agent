from google.adk.agents import Agent

# --- Agent Definition (model, instructions, tools) ---
root_agent = Agent(
    model="gemini-2.5-flash",
    name="software_assistant",
    instruction="""
    You are a skilled expert in triaging and debugging software issues for a
    coffee machine company, QuantumRoast.
    """,
    tools=[],
)
