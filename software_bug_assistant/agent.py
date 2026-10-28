from google.adk.agents import Agent

from .tools import get_current_date, search_tool

# --- Agent Definition (model, instructions, tools) ---
root_agent = Agent(
    model="gemini-1.5-flash",
    name="software_assistant",
    instruction="""
    You are a skilled expert in triaging and debugging software issues for a
    robotics company.
    """,
    tools=[get_current_date, search_tool],
)
