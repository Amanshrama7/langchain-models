from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import  cosine_similarity
import numpy as np
# running locally so no dotenv
# SEMANTIC SEARCH USING SENTENCE TRANSFORMER  MODEL DOWNLOADED IN MY PC


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "virat kholi is the best batsmen",
    "dhoni is the best caption in indian ciricket history",
    "bumhara is the best bowler"
]
query="Tell me about dhoni"


doc_embedding =embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

score=cosine_similarity([query_embedding],doc_embedding)[0]  # [0]  so output 1 d lisr
# print(cosine_similarity([query_embedding],doc_embedding))

# list(enumerate) assign index to each score so we can know the score after sorting
index, scor =sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print(f"Similarity score is: {scor}")
