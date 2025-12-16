import json
from openai_client import call_openai_chat

SYSTEM_PROMPT = """
You are an expert Python code reviewer. Given Python source code from a user, do the following:

1) Identify any bugs, runtime errors, security vulnerabilities, or incorrect logic.
   For each issue provide:
   - title
   - severity (low / medium / high)
   - line numbers or code excerpt
   - short explanation

2) Provide a minimal fixed version of the code that preserves the original behavior.

3) Provide short reproduction steps or unit-test style examples if applicable.

4) Output must be VALID JSON with exactly these keys:
   - issues (array)
   - fixed_code (string)
   - explanation (string)

Respond ONLY with valid JSON wrapped inside markdown triple backticks.
"""

def review_code(code: str) -> dict:
    """
    Sends user Python code to OpenAI for review and returns
    structured feedback (issues, fixed_code, explanation).
    """

    # Safety check
    if not code or not code.strip():
        return {
            "issues": [],
            "fixed_code": "",
            "explanation": "No Python code was provided for review."
        }

    # Prepare messages for chat completion
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Here is the user's Python code:\n\n```python\n{code}\n```"
        }
    ]

    # Call OpenAI
    response = call_openai_chat(messages, max_tokens=2000)

    # ✅ NEW SDK: message is an object, not a dict
    assistant_text = response.choices[0].message.content

    # -------------------------------
    # Extract JSON from markdown
    # -------------------------------
    start = assistant_text.find("```")
    if start != -1:
        end = assistant_text.find("```", start + 3)
        if end != -1:
            json_block = assistant_text[start + 3:end].strip()
        else:
            json_block = assistant_text[start + 3:].strip()
    else:
        json_block = assistant_text.strip()

    # Remove optional "json" language tag
    json_block = json_block.lstrip("json").strip()

    # -------------------------------
    # Parse JSON safely
    # -------------------------------
    try:
        return json.loads(json_block)
    except Exception:
        # Fallback if model response is not valid JSON
        return {
            "issues": [],
            "fixed_code": "",
            "explanation": assistant_text
        }
