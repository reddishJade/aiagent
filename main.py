import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output"
    )  # Optional verbose flag
    args = parser.parse_args()

    # Load api key from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    # Create messages list with user prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    for _ in range(20):
        # Generate response
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
                temperature=0,
            ),
        )

        # Verify usage_metadata is not None
        if response.usage_metadata is None:
            raise RuntimeError("API request failed: usage_metadata is None")

        if verbose:
            # Print token usage information
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        # Add candidates to history
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.function_calls:
            function_responses = []
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=verbose)

                # Sanity checks on function call result
                if function_call_result.parts == []:
                    raise RuntimeError("Function call failed: empty result")
                if function_call_result.parts[0].function_response is None:
                    raise RuntimeError("Function call failed: function_response is None")
                if function_call_result.parts[0].function_response.response is None:
                    raise RuntimeError("Function call failed: response is None")

                # Accumulate function results
                function_responses.append(function_call_result.parts[0])

                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

            # Add function results to messages
            messages.append(types.Content(role="user", parts=function_responses))
        else:
            # Final response reached
            print("Final response:")
            print(response.text)
            return

    # If maximum number of iterations is reached
    print("Error: Maximum number of iterations (20) reached without a final response.")
    sys.exit(1)


if __name__ == "__main__":
    main()
