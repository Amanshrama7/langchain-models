from langchain_huggingface import HuggingFaceEmbeddings
# running locally so no dotenv

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "delhi is the capital of india",
    "paris is the capital of france"
]

vector=embedding.embed_documents(documents)

print(str(vector))