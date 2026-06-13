from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    model='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation',
    huggingfacehub_api_token=os.getenv("HF_Token")
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables = ['topic']
)
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'cricket'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)