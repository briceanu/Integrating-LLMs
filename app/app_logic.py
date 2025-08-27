import os
from openai import OpenAI
from dotenv import load_dotenv
from app import schemas

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)  # load from env var


def get_answer_from_openai(question: str):
    """
    Send a question to the OpenAI API and return the assistant's answer.

    This function uses the OpenAI `responses.create` endpoint with the
    specified model (`gpt-4.1`) to generate an answer to the provided
    question. The raw API response is parsed to extract the text content
    of the first output message.

    Args:
        question (str): The input question to ask the AI model.

    Returns:
        schemas.ResponseSchemaOut: A Pydantic schema containing the
        extracted answer text in the `answer` field.
    """

    response = client.responses.create(model="gpt-4.1", input=question)
    data = response.output[0].content[0].text
    return schemas.ResponseSchemaOut(answer=data)
