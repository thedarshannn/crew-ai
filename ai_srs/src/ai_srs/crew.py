from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from tools import RequirementsGathererTool, SRSFormatterTool

load_dotenv()

@CrewBase
class AiSrs():
	"""AI SRS Generator Crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def requirements_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['requirements_analyst'],
			tools=[RequirementsGathererTool()],
			verbose=True
		)

	@agent
	def technical_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_writer'],
			tools=[SRSFormatterTool()],
			verbose=True
		)

	@agent
	def reviewer(self) -> Agent:
		return Agent(
			config=self.agents_config['reviewer'],
			verbose=True
		)

	@task
	def gather_requirements_task(self) -> Task:
		return Task(
			config=self.tasks_config['gather_requirements_task'],
		)

	@task
	def draft_srs_task(self) -> Task:
		return Task(
			config=self.tasks_config['draft_srs_task'],
		)

	@task
	def review_srs_task(self) -> Task:
		return Task(
			config=self.tasks_config['review_srs_task'],
			output_file='srs_document.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AI SRS Generator crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
