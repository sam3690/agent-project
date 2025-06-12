from dotenv import load_dotenv
import os
from pydantic import BaseModel
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

OPENROUTE_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTE_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set.")

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTE_API_KEY,
)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful research assistantthat will help generate a research paper.
            Answer the user query and use neccessary tools.""",
        ),
        (
            "placeholder",
            "{chat_history}"
        ),
        (
            "human",
            "{query}"
        ),
        (
            "placeholder",
            "{topic}",
        )
    ]
).partial(format_instructions=parser.get_format_instructions())
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
