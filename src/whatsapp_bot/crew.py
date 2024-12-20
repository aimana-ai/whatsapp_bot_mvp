from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from whatsapp_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class WhatsappCrewCrew():
	"""WhatsappCrew crew"""

	@agent
	def assistant(self) -> Agent:
		return Agent(
			config=self.agents_config['assistant'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)


	@task
	def assistant_task(self) -> Task:
		return Task(
			config=self.tasks_config['assistant_task'],
		)



	@crew
	def crew(self) -> Crew:
		"""Creates the WhatsappCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
