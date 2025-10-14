import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions


def main():
    load_dotenv()

    # Get command line arguments excluding the script name
    args = sys.argv[1:]

    # Check if there are any arguments provided
    if not args:
        print("Please provide a prompt as a command line argument.")
        sys.exit(1)

    # Check for verbose flag
    verbose = ("--verbose" in args)
    prompt_args = [arg for arg in args if arg != "--verbose"]

    # Join the arguments to form the complete prompt
    user_prompt = " ".join(prompt_args)

    # Prepare the message for the API
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # Initialize the GenAI client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Generate content using the specified model
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
        )
    )

    # Print the response text
    if response.function_calls:
        print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
    else:
        print(response.text)
    if verbose:
        print("User prompt: ", user_prompt)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)



if __name__ == "__main__":
    main()
