# src/mail_agent/crew.py
from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from src.mail_agent.tools.mailer import SendMail
# from langchain_groq import ChatGroq
import os
# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MailAgent():
	"""MailAgent crew"""


	# def __init__(self):
	# 	self.llm = ChatGroq(temperature=0,model_name="mixtral-8x7b-32768")
	GROQ_API_KEY=os.getenv('GROQ_API_KEY')
	def __init__(self,GROQ_API_KEY=GROQ_API_KEY):
		self.llm=LLM(model="groq/llama-3.3-70b-versatile",temperature=0.7)
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def mail_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['mail_writer'],
			# verbose=True,
			llm=self.llm,
			allow_delegation=False,
			tools=[SendMail.send_mail],
			
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_mail'],
			verbose=True,
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
