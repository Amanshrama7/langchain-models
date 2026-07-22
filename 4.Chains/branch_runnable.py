from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda ,RunnablePassthrough,RunnableSequence

# if report length greater then given limit than summarize it ,else print report as it is .

load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Summarize the given \n {text}",
    input_variables=['text']
)

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

res=final_chain.invoke({'topic':"Ai"})

print(res)