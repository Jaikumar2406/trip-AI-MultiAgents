from langgraph.graph import StateGraph ,END 
from typing import TypedDict , Annotated , Sequence
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import BaseMessage , HumanMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import base64
import os
from tools.get_bus_between_city import get_bus_between_city
from tools.get_train_between_station import get_train_between_station
from tools.get_flights_between_airports import get_flights_between_airports
from tools.search_hotels import search_hotels
from tools.famous_food_in_city import famous_food_in_city
from tools.describe_location_beauty import describe_location_beauty
from tools.search_tourist_place import search_tourist_places
from utils.model_call import model_call
from utils.should_continue import should_continue
import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.voice import speak

main = FastAPI()
class UserInput(BaseModel):
    user_input: str

main.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage] , add_messages]

groq_api_key = os.getenv("groq_api_key")

model = ChatGroq(model= "llama-3.3-70b-versatile" , api_key=groq_api_key , temperature=0.7)
tools = [get_flights_between_airports,get_train_between_station ,get_bus_between_city ,search_hotels ,famous_food_in_city,search_tourist_places,describe_location_beauty]

model= model.bind_tools(tools , tool_choice="auto")


graph = StateGraph(AgentState)
graph.add_node("our_agent" , model_call)
tool_node = ToolNode(tools=tools)
graph.add_node("tool" , tool_node)
graph.set_entry_point("our_agent")
graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tool",
        "end": END
    }
)

graph.add_edge("tool", "our_agent")
app = graph.compile()


conversation_memory = {"messages": []}
@main.get("/")
def root():
    return {"message": "Welcome to Trip Assistant v1.0 — Ready to help with your travel!"}

@main.post("/chat")
async def chat(input_data: UserInput):
    global conversation_memory
    user_input = input_data.user_input.strip()

    if user_input.lower() == "exit":
        conversation_memory = {"messages": []}
        speak("Thank you for using Trip Assistant. Have a great trip!")
        return {"reply": "Thank you for using Trip Assistant. Have a great trip!"}

    conversation_memory["messages"].append(HumanMessage(content=user_input))

    try:
        result = app.invoke(conversation_memory)
        conversation_memory = result

        last_message = conversation_memory["messages"][-1]
        reply = last_message.content if hasattr(last_message, "content") else "I'm processing your request..."

        # 🗣️ Generate ElevenLabs audio and return it as base64
        audio_bytes = speak(reply, return_audio=True)
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8") if audio_bytes else None

        return {
            "reply": reply,
            "audio": audio_base64
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
