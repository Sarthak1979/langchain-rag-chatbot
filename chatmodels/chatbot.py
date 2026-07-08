from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI 
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage

MODES = {
    "fast": {
        "system": "You are a fast AI assistant. Give short, direct answers.",
        "temperature": 0.3
    },
    "thinking": {
        "system": "You are a thoughtful AI. Explain step by step with reasoning.",
        "temperature": 0.7
    },
    "research": {
        "system": "You are a research AI. Provide detailed, structured, and in-depth answers.",
        "temperature": 0.9
    }
}

# Select mode
print("Select Mode: fast / thinking / research")
mode = input("Mode: ").strip().lower()

if mode not in MODES:
    print("Invalid mode, defaulting to FAST")
    mode = "fast"

config = MODES[mode]

model = ChatMistralAI(model = "mistral-small-latest", temperature=config["temperature"])

messages = [    
    SystemMessage(content=config["system"])
]
print(f"--- Running in {mode.upper()} mode (type 0 to exit) ---")

while True:
    prompt = input ("You : ")
    messages.append(HumanMessage(content=prompt))
   
    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(response.content))
    print("Bot :",response.content)

print(messages)