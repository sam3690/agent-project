from dotenv import load_dotenv
import os
from pydantic import BaseModel
# from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor


load_dotenv()

OPENROUTE_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTE_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set.")

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

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
            Wrap the output in this format and provide no other text.\n{{format_instruction}}""",
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

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[],    
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_response = agent_executor.invoke({"input": "What is the capital of France?"})
print(raw_response)
# completion = llm.chat.completions.create(
#     model="deepseek/deepseek-chat",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the meaing of life?"
#         },
#     ],
# )
# print(completion.choices[0].message.content)
