from dataclasses import dataclass


@dataclass
class Config:
    EMBEDDING_MODEL: str = "nomic-embed-text"
    LLM_MODEL: str = "llama3.2"
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200