import argparse
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=args.user_prompt,
)

# Verify usage_metadata is not None
if response.usage_metadata is None:
    raise RuntimeError("API request failed: usage_metadata is None")

# Print token usage information
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
