from unittest.mock import patch, MagicMock
from app import app_logic
from app import schemas

def test_get_answer_from_openai():
    # Fake response structure that mimics OpenAI's actual API response
    fake_response = MagicMock()
    fake_response.output = [
        MagicMock(content=[MagicMock(text="Hello, this is a test answer!")])
    ]
    with patch("app.app_logic.client.responses.create", return_value=fake_response):
        result = app_logic.get_answer_from_openai("What is AI?")

    assert isinstance(result,schemas.ResponseSchemaOut)
    assert result.answer == 'Hello, this is a test answer!'
