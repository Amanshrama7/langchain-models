from langchain_openai import ChatOpenAI
from dotenv import  load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model=ChatOpenAI()

# PYDANTIC CLASS
class Review (BaseModel):
    key_themes: list[str]=Field(description="write all the key themes discussed in the review in a list")
    summary  :str = Field(description="A breif summary of review")
    # literal output will be pos or neg
    sentiment:Literal["pos","neg"] = Field(description="return sentiment of review as positive , negative or neutral")
    pros     :Optional[list[str]] = Field(default= None, description="write all the pros inside the list")
    cons     :Optional[list[str]] = Field(default= None, description="write all the cons  inside the list")


structured_model= model.with_structured_output(Review)
result=structured_model.invoke(""" more complex review the hardware is good, but software is bad """)

print(result)



