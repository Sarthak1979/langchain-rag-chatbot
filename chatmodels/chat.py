from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.1,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

response = model.invoke("Write a poem about the beauty of nature.")
print(response.content)