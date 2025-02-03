import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage
from extraction import extract_text_from_image
 
def get_ai_response(image_path: str) -> str:
    # Load environment variables from .env file
    load_dotenv()
 
    # Retrieve the Hugging Face API token from environment variables
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
 
    # Initialize the Hugging Face endpoint
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )

    question=extract_text_from_image(image_path)
 
    # Create a ChatHuggingFace instance
    chat_model = ChatHuggingFace(llm=llm)
 
    # Define the messages
    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content=question),
    ]
 
    # Invoke the chat model
    ai_msg = chat_model.invoke(messages)
 
    # Return the AI response
    return ai_msg.content