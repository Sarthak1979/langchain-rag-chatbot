from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/Deepseek-R1"
) 
model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")

print(response.content)