# downloading the model in machine and then making chat model


from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    device=-1,
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model=ChatHuggingFace(llm=llm)
res=model.invoke("what is the capital of india")

print(res.content)