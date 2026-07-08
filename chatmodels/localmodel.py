from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint , HuggingFacePipeline 
llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.2,
    )
)

chatmodel = ChatHuggingFace(llm=llm)

result = chatmodel.invoke("What is the capital of France?")

print(result.content)