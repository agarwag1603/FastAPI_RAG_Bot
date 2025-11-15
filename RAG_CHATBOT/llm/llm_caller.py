from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from embedding.embedding_pdf import chroma_retriever 

def llm_caller_func(gpt_model,query):
    
    gpt_llm=ChatOpenAI(model=gpt_model)

    prompts_template=ChatPromptTemplate.from_messages([
        ("system","You an AI assistant that helps answer the user questions."),
        ("user","Input: {input}\n\n Context:{context}")
        ])

    output_parse=StrOutputParser()

    chain= ({"input": RunnablePassthrough(), "context":chroma_retriever} | prompts_template | gpt_llm | output_parse)
    response=chain.invoke(query)

    return response