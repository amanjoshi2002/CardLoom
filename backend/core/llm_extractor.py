import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Set your Gemini API key
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# # Call the Gemini model using the gemini/ prefix
# response = completion(
#     model="gemini/gemini-2.5-flash", 
#     messages=[{"role": "user", "content": "Hello, how are you?"}]
# )

# print(response.choices[0].message.content)

def llm_extract(text):
    if isinstance(text, list):
        text = "\n".join(text)

    response = completion(
        model="gemini/gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract business card information and return ONLY valid JSON."
                ),
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )

    return response.choices[0].message.content