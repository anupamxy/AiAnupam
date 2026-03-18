from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI(
    api_key="AIzaSyAwjxpH0OQy0zKt3y8rRs5QV0schx6Zbio",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
response=client.chat.completions.create(model="gemini-2.5-flash",messages=[
    {"role":"system","content":"You are a helpful assistant."},
    # this is the example of system prompt, you can set the behavior of the model by using system prompt. In this example, we have set the system prompt to "You are a helpful assistant.", which tells the model to behave like a helpful assistant.
    {"role":"user","content":"what is python?"}
    ])
print(response.choices[0].message.content)