#  THIS WILL NOT WORK BECUSE I DONT HAVE OPEN AI API KEY

from  langchain_openai import OpenAI
# dotenv load API key to  current file from .env file
from dotenv import load_dotenv

load_dotenv()

# generate openai object define modle
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# in invoke() we enter prompt and get the response from the modle

result= llm.invoke("what is the capital of india")

print(result)


# llms take string is input and give single string as output
