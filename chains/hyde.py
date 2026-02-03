from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from config import Config


def build_hyde_chain():
    llm = ChatOllama(model=Config.LLM_MODEL, temperature=0.7)

    template = """You are an expert lawyer who has read dozens of Legal documents
    Write a theoretical paragraph that answers the following question. 
    Do not be conversational, just output the answer passage.
    
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    
    chain = prompt | llm | StrOutputParser()

    return chain
