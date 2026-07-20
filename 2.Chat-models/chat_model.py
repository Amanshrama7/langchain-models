from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# TEMPERATURE = parameter define randomness of model's output 
# max_completion_tokens can restrict no. of words(approx) in response by model

model=ChatOpenAI(model='gpt-4',temperature=0, max_completion_tokens=10)

result=model.invoke("what is the capital of india?")

print(result.content)

# result.conten give actual answer oterwise chat model will give meta data
