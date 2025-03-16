from src.inference.gemini import ChatGemini
from src.agent.computer import ComputerAgent
from src.inference.groq import AudioGroq
from src.speech import Speech
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGemini(model='gemini-2.0-flash', api_key=google_api_key, temperature=0)
audio_llm = AudioGroq(model='whisper-large-v3', mode='translations', api_key=groq_api_key, temperature=0)

agent = ComputerAgent(llm=llm, use_vision=False, verbose=True, max_iteration=20)

# 音声モードを自動選択
speech = Speech(llm=audio_llm, verbose=True)    
user_query = speech.invoke()
print(f'Enter your query: {user_query.content}')

agent_response = agent.invoke(user_query)
print(agent_response)