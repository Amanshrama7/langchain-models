# open source chatbot using  qwen
# using hugging face api ,not running  the model locally


from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint (
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",max_new_tokens=50,  # Controls the max length of the output response
    temperature=0.7 )

model = ChatHuggingFace(llm=llm)

result = model.invoke('what is the capital of india')

print(result.content)