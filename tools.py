# tools.py
import os
from datetime import datetime
from langchain.tools import StructuredTool
from pydantic import BaseModel
from langchain.tools import Tool


def save_plan(plan: str, location: str) -> str:
    os.makedirs('plans', exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"plans/{location.replace(' ', '_').lower()}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(plan)
    return filename  # Return just the file path


def suggest_trip(city: str) -> str:
    return f"""
Top 5 things to do in {city}:
1. Visit historical sites
2. Try traditional cuisine
3. Explore museums or art districts
4. Go hiking or sightseeing
5. Experience local nightlife or music
"""

class SavePlanInput(BaseModel):
    plan: str
    location: str

tools = [
    StructuredTool.from_function(
        name="save_plan",
        func=save_plan,
        description="Save a travel itinerary to a file. Takes 'plan' and 'location'.",
        args_schema=SavePlanInput
    ),
    Tool(
        name="suggest_trip",
        func=suggest_trip,
        description="Suggests top 5 activities for a given city. Input: city name."
    )
]
