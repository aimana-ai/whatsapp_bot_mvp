from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool
# Define the agent to summarize messages
# Create an agent that reads the content of a file and summarizes it


file_read_tool = FileReadTool(file_path='Data/filtered_data.json')

summarizer_agent = Agent(
  role='Senior Assistant',
  goal='Assist the recipient by summarizing the last 24 hours of conversations',
  backstory="""You're an assistant for the person receiving these messages.
    Your job is to help them by summarizing the conversations from the last 24 hours
    and providing any necessary insights.""",
  tools=[file_read_tool],  # Optional, defaults to an empty list
  verbose=True,  # Optional
  
)

summary_task = Task(
    description='Read the content of the JSON file with the conversations from the past 24 hours and create a one-paragraph summary pointing out the most important messages',
    agent=summarizer_agent,
    expected_output='A one-paragraph in Portuguese with a summary of the most important conversations from the past 24 hours',
)

crew = Crew(
    agents=[summarizer_agent],
    tasks=[summary_task],
    verbose=True
)

