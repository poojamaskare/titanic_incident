from langchain.chains import Chain
from langchain.agents import AgentExecutor
from langchain.tools import Tool
from ..tools.data_tools import summarize_ticket_fares, calculate_percentage
from ..agents.titanic_agent import TitanicAgent

class AnalysisChain(Chain):
    def __init__(self, data):
        self.agent = TitanicAgent(data)
        self.tools = [
            Tool(name="Summarize Data", func=summarize_ticket_fares, description="Summarizes the Titanic dataset fare data."),
            Tool(name="Calculate Percentages", func=calculate_percentage, description="Calculates survival percentages based on criteria.")
        ]
        self.executor = AgentExecutor(agent=self.agent, tools=self.tools)

    def run(self, query):
        return self.executor.run(query)