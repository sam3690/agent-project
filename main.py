from dotenv import load_dotenv
import os
from pydantic import BaseModel
# from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool


load_dotenv()

OPENROUTE_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTE_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set.")

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

    def __str__(self):
        sources_str = '\n'. join(f'- {src}' for src in self.sources)
        tools_str = ', '.join(self.tools_used)
        return f"Topic: {self.topic}\nSummary: {self.summary}\nSources:\n{sources_str}\nTools Used: {tools_str}"

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTE_API_KEY,
    model="deepseek/deepseek-chat",  # Specify the model you want to use
    temperature=0.1,
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful research assistantthat will help generate a research paper.
            Answer the user query and use neccessary tools.
            Wrap the output in this format and provide no other text.\n{format_instructions}""",
        ),
        (
            "placeholder",
            "{chat_history}"
        ),
        (
            "human",
            "{input}"
        ),
        (
            "placeholder",
            "{agent_scratchpad}",
        )
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,    
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can I help you research? ")
raw_response = agent_executor.invoke({"input": query})
# print(raw_response)

try:
    structures_response = parser.parse(raw_response["output"])
    print(structures_response)
    save_tool.func(str(structures_response))
except Exception as e:
    print("Error parsin response", e, "Raw Response - ", raw_response)

