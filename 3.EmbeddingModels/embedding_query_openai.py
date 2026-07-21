#  generating embedding for only 1 string

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding= OpenAIEmbeddings(model="text-embedding-3-large", dimensions=30)

vector=embedding.embed_query("Delhi is the Capital of India")

print(str(vector))
