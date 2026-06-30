from google.adk.agents.llm_agent import Agent
import data_tool

# Changed back to root_agent so the framework is happy!
root_agent = Agent(
    model='gemini-2.5-flash',
    name='Data_Pipeline_Analyst_Agent',
    description='An autonomous agent designed to clean local data layouts and generate executive business intelligence reports.',
    instruction=(
        "You are an expert Data Analyst Agent. When a user asks you to analyze or clean a data file, "
        "you MUST call the 'clean_and_analyze_dataset' tool first. Do not guess or hallucinate data metrics. "
        "Once the tool returns the data pipeline success metrics, read those numbers and output a polished, "
        "professional business intelligence summary with clear key takeaways for a manager."
    ),
    tools=[data_tool.clean_and_analyze_dataset]
)