from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_txt (data:str, filename:str = "research_output.txt"):
    timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timeStamp}\n\n{data}\n\n"

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(formatted_text)
    
    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name='save_text_to_file',
    func=save_to_txt,
    description='Save the research output to a text file.'
)

search = DuckDuckGoSearchRun()

search_tool = Tool(
    name ='search',
    func=search.run,
    description='Search the web for information.'
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_mas=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)