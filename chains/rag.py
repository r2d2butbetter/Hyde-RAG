from langchain_chroma import Chroma
from config import Config
from .hyde import build_hyde_chain
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def create_rag_chain():
    embeddings = OllamaEmbeddings(model=Config.EMBEDDING_MODEL)
    vector_store = Chroma(collection_name='vector-db', embedding_function=embeddings, persist_directory='./chroma_db')


    retriever = vector_store.as_retriever()

    hyde_chain = build_hyde_chain()
    retrieval_chain = hyde_chain | retriever

    final_llm = ChatOllama(model=Config.LLM_MODEL, temperature=0)

    prompt_str = """
    Answer using the context below:
    {context}
    
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(prompt_str)

    final_chain = {"context": retrieval_chain, "question": RunnablePassthrough()} | prompt | final_llm | StrOutputParser()


    return final_chain



