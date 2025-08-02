from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
from tools import tools
from schema import TravelPlan
import os
from pydantic import TypeAdapter
import json


raw_schema = json.dumps(TypeAdapter(TravelPlan).json_schema(), indent=2)
escaped_schema = raw_schema.replace("{", "{{").replace("}", "}}")


SYSTEM_PROMPT = f"""
You are a friendly and intelligent Travel Planning Assistant. 
Tasks:
1. Ask the user about their destination,number of days,interests and budget.
2. Use suggest_trip to get location-based ideas
3. Create a multi day itinerary
4. Call the tool `save_plan(plan, location)` to save the itinerary.
5. Use the returned file path as the `saved_path` value in the JSON response.
6. Return only JSON that matches the schema below.

You MUST respond ONLY with a valid JSON object that fits the schema below.

Do NOT ask follow-up questions. Do NOT write anything outside JSON.
Even if the user's input is incomplete, fill reasonable defaults and respond with valid JSON.

JSON format schema:
{escaped_schema}
"""

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

parser=PydanticOutputParser(pydantic_object=TravelPlan)

prompt=ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder","{chat_history}"),
    ("human", "{query}"),
    ("placeholder","{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent=create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
executor=AgentExecutor(agent=agent, tools=tools, verbose=True)

chat_history = []
print("✈️Travel Planner Agent! Type 'exit' to quit.")

while True:
    q= input("You: ")
    if q.lower() == "exit":
        print("Goodbye! Safe travels! ✈️")
        break

    chat_history.append(HumanMessage(content=q))
    result= executor.invoke({
        "query": q,"chat_history": chat_history })
    
    try:
        output=parser.parse(result["output"])
        print("\n🧭Itinerary:\n", output.itinerary)
        print("\n✨Highlights:\n", output.highlights)
        print("\n📁File:\n", output.saved_path)
        chat_history.append(AIMessage(content=output.itinerary))
    
    except Exception as e:
        print("⚠️Error parsing output:", e)
        print("Raw output:", result["output"])

