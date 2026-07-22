from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda


load_dotenv()

# take feedback and classify it into +ve or -ve and generate response according to it

model=ChatOpenAI()
parser=StrOutputParser()
# this is done get control over the output of prompt1 as it output used in other 2 chains
# pydantic output
class feedback(BaseModel):
      sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template="Classify the feedback into Positive or Negative based on give input \n {feedback}\n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction':parser2.get_format_instructions()})

classifier_chain = prompt1| model|parser2

prompt2=PromptTemplate(
      template="generate an appropriate reply according to the positive response {feedback}",
      input_variables=["feedback"]
)
prompt3=PromptTemplate(
      template="generate an appropriate reply according to the negative response {feedback}",
      input_variables=["feedback"]
)

conditional_chain=RunnableBranch(
      (lambda x:x.sentiment=='positive' , prompt2|model|parser),# (condition,chain)
      (lambda x:x.sentiment=='negative' , prompt3|model|parser),
      RunnableLambda(lambda  x: "could not find sentiment")
)
chain= classifier_chain | conditional_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))
