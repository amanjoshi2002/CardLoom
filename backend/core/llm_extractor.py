import os
from litellm import completion

# Set your Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyDC9I8BmAVmBH3zK0cnWT61Sy-VWhtaxAI"

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