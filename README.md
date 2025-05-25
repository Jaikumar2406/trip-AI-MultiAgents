# 🧠 Multi-AI Travel Assistant (7-Agent System)

An intelligent multi-agent travel planning assistant built using the **ReAct framework** and **DuckDuckGoSearchResults**, capable of interacting with users in a conversational way to plan detailed trips.

---

## 🚀 Features

This project includes **7 specialized AI agents**, each responsible for a core aspect of travel planning:

1. **✈️ Flight Search Agent**  
   Finds flights between two locations with details like departure time, arrival time, duration, and pricing.

2. **🚌 Bus Search Agent**  
   Searches for buses available on a given route, along with timing, fare, and travel duration.

3. **🚆 Train Search Agent**  
   Looks up trains between cities, including class, timing, fare, and estimated duration.

4. **🏨 Hotel Search Agent**  
   Recommends low-budget, mid-range, and luxury hotel options with price, features, and location.

5. **🍽️ Famous Food Search Agent**  
   Suggests local popular foods and dishes from the destination city, including vegetarian/non-vegetarian options and pricing.

6. **🗺️ Tourist Place Search Agent**  
   Lists famous tourist attractions in the destination, their significance, popularity, and best times to visit.

7. **📍 Location Describer Agent**  
   Provides a short, beautiful description of any place mentioned by the user to help them visualize the location.

---

## 🛠️ Tech Stack

- **Framework**: ReAct (Reason + Act agent-based approach)  
- **Search Tool**: DuckDuckGo Search API (via `DuckDuckGoSearchResults`)  
- **Language**: Python  
- **Interface**: Conversational (chat-based interaction)

---

## 💬 How It Works

1. The user interacts in natural language (e.g., “I want to go to Manali”).
2. The system uses the **Location Describer Agent** to describe Manali.
3. It then asks for the starting point and queries respective agents like Flight, Bus, or Train Search.
4. Each agent uses **DuckDuckGoSearchResults** to fetch the most accurate and recent info.
5. Agents collaborate step-by-step using ReAct to recommend transport, hotels, food, and tourist places.
6. After collecting all info, the system can generate a final **itinerary summary**.

---

## 📦 Installation

```bash
git clone https://github.com/jaikumar2406/multi-ai-travel-assistant.git
cd multi-ai-travel-assistant
pip install -r requirements.txt
