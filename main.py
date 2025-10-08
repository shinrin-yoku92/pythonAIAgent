import os
from dotenv import load_dotenv
from google import genai
import sys



def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("Please provide a prompt as a command line argument.")
        sys.exit(1)
    
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=user_prompt,
    )

    print(response.text)
    print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)



if __name__ == "__main__":
    main()
