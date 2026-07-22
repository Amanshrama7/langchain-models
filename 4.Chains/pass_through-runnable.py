from langchain_core.runnables import RunnablePassthrough

pass_thr=RunnablePassthrough()

print(pass_thr.invoke(234))