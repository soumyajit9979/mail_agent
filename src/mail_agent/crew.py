# src/mail_agent/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.mail_agent.tools.mailer import SendMail

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MailAgent():
	"""MailAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def mail_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['mail_writer'],
			verbose=True,
			tools=[SendMail.send_mail]
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_mail'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MailAgent crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
