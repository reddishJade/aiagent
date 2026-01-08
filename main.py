import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

# Parse command line arguments
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

# Create messages list with user prompt
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# Generate response
response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

# Verify usage_metadata is not None
if response.usage_metadata is None:
    raise RuntimeError("API request failed: usage_metadata is None")

# Print token usage information
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Print the response text
print(response.text)
