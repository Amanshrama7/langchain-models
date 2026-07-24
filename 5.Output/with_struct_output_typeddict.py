# using model capable of generating structured output
from langchain_openai import ChatOpenAI
from dotenv import  load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model=ChatOpenAI()
#schema
class Review (TypedDict):
    key_themes: Annotated[list[str],"write all the key themes discussed in the review in a list"]
    summary  :Annotated[str, "A breif summary of review"]
    # literal output will be pos or neg
    sentiment:Annotated[Literal["pos","neg"],"return sentiment of review as positive , negative or neutral"]
    # optional
    pros     :Annotated[Optional[list[str]],"write all the pros inside the list"]
    cons     :Annotated[Optional[list[str]],"write all the cons  inside the list"]


structured_model= model.with_structured_output(Review)
result=structured_model.invoke(""" more complex review the hardware is good, but software is bad """)

print(result)
print(result["summary"])
print(result["sentiment"])
