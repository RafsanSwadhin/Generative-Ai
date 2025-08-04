import os
from dotenv import load_dotenv , find_dotenv
_ = load_dotenv(find_dotenv())

groq_api_key = os.environ["GROQ_API_KEY"]

from langchain_groq import ChatGroq
chatModel = ChatGroq()

chaModel = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"  # or other supported model
)