import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys



def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("Please provide a prompt as a command line argument.")
        sys.exit(1)

    verbose = ("--verbose" in args)
    prompt_args = [arg for arg in args if arg != "--verbose"]

    user_prompt = " ".join(prompt_args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
    )

    print(response.text)
    if verbose:
        print("User prompt: ", user_prompt)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)



if __name__ == "__main__":
    main()
