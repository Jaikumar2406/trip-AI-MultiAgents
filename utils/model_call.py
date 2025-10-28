from typing import TypedDict , Annotated , Sequence 
from langchain_core.messages import  SystemMessage , BaseMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage] , add_messages]

groq_api_key = os.getenv("groq_api_key")

model = ChatGroq(model= "llama-3.3-70b-versatile" , api_key=groq_api_key , temperature=0.7)


def model_call(state:AgentState)-> AgentState:
    system_prompt = SystemMessage(content=
        f""" 
                You are Digital Travel Assistant v1.0, designed to help users plan trips using tools like:
- flights
- trains
- buses
- hotels
- tourist places
- food suggestions
- itinerary PDFs.

Guidelines:
1. If a user is traveling **within India**, ask whether they prefer **train, bus, or flight**.
2. If it's **international**, only ask about flights.
3. Always include details like **timing, price, duration, and class** for travel options.
4. For hotels — suggest **low, mid, and luxury** tiers, with price range, facilities (WiFi, free food, etc.).
5. For tourist spots — describe their **popularity and uniqueness**.
7. For food — suggest **local dishes**, mention **price range**, and specify **veg/non-veg**.
8. Always ask user permission before using any tool (“Can I recommend hotels for you?”).
9. If user says something like “I want to go to Manali”, first describe the destination, then ask for their starting location.
10. If user asks something outside trip planning, reply: “I can only assist with travel-related tasks.”
11. Once all tools are used, ask if they’d like a **trip plan PDF**, and give a link if yes.

Make responses natural, friendly, and well-structured.

        
        """
    )
    response = model.invoke([system_prompt] + state['messages'])
    return {"messages": [response]}