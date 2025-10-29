# 🌍 AI Travel Assistant Agent  

An **AI-powered travel assistant** that helps users discover **hotels, flights, buses, trains, famous foods, and tourist places** — all through a single intelligent chat interface.  
The system fetches live information using **DuckDuckGo Search**, speaks results aloud using **Eleven Labs Text-to-Speech (TTS)**, and is built with a **Node.js frontend** and **FastAPI backend**.  

---

## 🚀 Features  

✅ Real-time travel info (Hotels, Flights, Trains, Buses, Food, Places)  
✅ DuckDuckGo-based intelligent search  
✅ Eleven Labs TTS for natural voice responses  
✅ Single chat endpoint for simplicity  
✅ Modular architecture — Node.js frontend + FastAPI backend  
✅ Text + Speech output  

---

## 🏗️ Tech Stack  

**Frontend:**  
- Node.js  
- HTML / CSS / JavaScript  
- Axios  

**Backend:**  
- FastAPI (Python)  
- DuckDuckGo Search integration  
- Eleven Labs Text-to-Speech API  

---

## ⚙️ How It Works  

1. User types a question like **“Best hotels in Manali”**  
2. Backend calls **DuckDuckGo Search** to fetch relevant info  
3. Response text is generated and converted to **speech** using Eleven Labs  
4. Frontend displays text and plays audio  

---

## 🧩 API Endpoint  

| Method | Endpoint | Description |
|:-------|:----------|:------------|
| `POST` | `/chat` | Takes user query → returns AI-generated text and speech response |

**Example Request:**
```json
POST /chat
{
  "query": "Tell me famous foods in Delhi"
}
```

## Example Response:
```
{
  "text": "Here are some famous foods in Delhi: Chole Bhature, Paranthe, and Butter Chicken.",
  "audio_url": "https://elevenlabs-generated-link.mp3"
}
```
## 🖥️ Installation
** 1️⃣ Clone the Repository**
```
git clone https://github.com/Jaikumar2406/trip-AI-MultiAgents.git
cd ai-travel-assistant
```
** 2️⃣ Setup Backend (FastAPI) **
```
pip install -r requirements.txt
uvicorn main:app --reload
```
** Setup Frontend (Node.js) ** 
```
cd frontend
npm install
npm run dev
```
## 💡 Future Enhancements
```
- 🌐 Add multilingual speech

- 🧭 Google Maps integration

- 🏨 Live flight/hotel booking API

- 📱 Mobile app version

```
<img width="1919" height="1027" alt="Screenshot 2025-10-28 140336" src="https://github.com/user-attachments/assets/cef7e468-2d4b-49eb-9fa6-b7181d4bf20f" />



<img width="1913" height="1016" alt="Screenshot 2025-10-28 140512" src="https://github.com/user-attachments/assets/04dddbcb-d8a0-4bf3-a1b4-707fd7bf9154" />

## 🚀 Live Demo

### 🌐 Frontend
[https://trip-ai-multi-agents-9htc.vercel.app/](https://trip-ai-multi-agents-9htc.vercel.app/)

### ⚙️ Backend
[https://trip-ai-multiagents-1.onrender.com/](https://trip-ai-multiagents-1.onrender.com/)

