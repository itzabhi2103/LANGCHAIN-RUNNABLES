from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    model='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation',
    huggingfacehub_api_token=os.getenv("HF_Token")
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables = ['topic']
)
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables = ['text']
)
parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic': 'AI'}))