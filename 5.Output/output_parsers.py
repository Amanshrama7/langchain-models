from langchain_huggingface import  ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser

# advatage of pydantic easy integration anf data validation

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
class person(BaseModel):
    name: str =Field(description="Name if person")
    age: int  =Field(gt=18, description="age of person")

parser=PydanticOutputParser(pydantic_object=person)


template= PromptTemplate(
    template="Generate the name ,age of fuactional {place} person\n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser

res=chain.invoke({"topic":"Indian"})

print (res)