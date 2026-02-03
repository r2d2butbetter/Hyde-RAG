from chains.rag import create_rag_chain


if __name__ == "__main__":
    rag_chain = create_rag_chain()

    question = input("Enter your query: ")

    response = rag_chain.invoke(question)

    print(f"Answer\n\n{response}")