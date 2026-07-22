from langchain_core.runnables import RunnableLambda
# convert any python function into runnable

def word_counter(in_string):
    return len(in_string.split())

lamb_runnable=RunnableLambda(word_counter)

print(lamb_runnable.invoke('My name is aman sharma'))