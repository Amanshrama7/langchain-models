#  generating embedding for multiple queries or multiple documents

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= OpenAIEmbeddings(model="text-embedding-3-large", dimensions=30)

documents=[
    "delhi is the capital of india",
    "paris is the capital of france"
]

res=embedding.embed_documents(documents)

print(str(res))
# output (2 list = 2 vector of 2 strings in a big list)
