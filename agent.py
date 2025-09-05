from llm_helper import llm

def response_generator(query, context):
    return llm(query, context)
