from fastapi import APIRouter, Query, status, HTTPException
from typing import Annotated
from pydantic import Field
from openai import OpenAI
from app import schemas

from app import app_logic

router = APIRouter()
openai = OpenAI()


@router.post(
    "/ask-ai", status_code=status.HTTP_200_OK, response_model=schemas.ResponseSchemaOut
)
async def ask_ai(
    question: Annotated[
        str, Field(description="simple question to ask AI", max_length=100), Query()
    ],
) -> schemas.ResponseSchemaOut:
    """
    Ask a question to the AI assistant and return the generated answer.

    This endpoint accepts a question string from the client (via query parameter),
    sends it to the application logic layer (`get_answer_from_openai`), and returns
    the AI-generated answer.

    Args:
        question (str): A user-provided question to be asked to the AI.
            Must not exceed 100 characters.

    Returns:
        dict: A dictionary containing the AI's answer in the `answer` field.

    Raises:
        HTTPException: If the input validation fails (e.g., length > 100).
    """

    try:
        return app_logic.get_answer_from_openai(question=question)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {str(e)}"
        )
