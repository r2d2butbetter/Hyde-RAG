from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import Config

class Ingestion:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vector_db = Chroma(collection_name='vector-db', embedding_function=self.embeddings, persist_directory='./chroma_db')

        self.splitter = RecursiveCharacterTextSplitter(chunk_size=Config.CHUNK_SIZE, chunk_overlap=Config.CHUNK_OVERLAP)

    def ingest_docs(self, filepath: str):
        doc_loader = PyPDFLoader(filepath)

        document = doc_loader.load()
        split_docs = self.splitter.split_documents(document)
        print(f"{len(split_docs)} chunks created")

        self.vector_db.add_documents(split_docs)
        


if __name__ == "__main__":
    ingestor = Ingestion()
    filepath = "./nikedocs.pdf"
    ingestor.ingest_docs(filepath=filepath)
