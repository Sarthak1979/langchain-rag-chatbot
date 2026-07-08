from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts = [ 
    "hello this is Sarthak Agrawal",
    "I am doing my internship at Growwstacks",
    "I am learning about generative AI and its applications"
]
vector = embeddings.embed_documents(texts)
print(vector)