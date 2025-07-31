from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

def generate_itinerary(location, budget, days, interests):
    template = """
You are a travel expert. Create a detailed {days}-day travel itinerary for someone visiting {location}.
They have a budget of {budget} INR and are interested in {interests}.

Include:
- Daily breakdown
- Places to visit
- Activities
- Food suggestions
- Approximate cost per day

Make it fun, local, and realistic.
"""

    prompt = PromptTemplate.from_template(template)
    llm = OpenAI(temperature=0.7)
    chain = prompt | llm
    return chain.invoke({
        "location": location,
        "budget": budget,
        "days": days,
        "interests": interests
    })
