import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from openai import RateLimitError, OpenAIError

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

client = OpenAI(api_key=OPENAI_API_KEY)

def call_openai_chat(
    messages,
    model="gpt-4o",
    max_tokens=1000,
    temperature=0.0
):
    """
    Calls OpenAI Chat Completion API with retry logic
    """
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response

        except RateLimitError:
            # Retry with exponential backoff
            time.sleep(2 ** attempt)

        except OpenAIError as e:
            raise RuntimeError(f"OpenAI API error: {e}")

    raise RuntimeError("OpenAI API failed after retries")
