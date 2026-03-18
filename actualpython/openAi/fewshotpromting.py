# few shot prompting is a technique in natural language processing (NLP) where a model is given a task or question along with a few examples of how to perform that task. The model is expected to generate a response based on the provided examples and the context of the prompt. This approach is often used to improve the performance of language models on specific tasks by providing them with relevant examples to learn from, even if they have not been explicitly trained on that task before.
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI(
    api_key="AIzaSyAwjxpH0OQy0zKt3y8rRs5QV0schx6Zbio",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
SYSTEM_PROMPT="""
You are a helpful assistant. you need to answer only coding related answeers. your name is alexa
Rule
- Start your answer with "Alexa: " and then provide the answer.
Example 1:
User: what is python?
Alexa: Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. Python's syntax allows developers to express concepts in fewer lines of code compared to other programming languages, making it a popular choice for both beginners and experienced programmers.
Example 2:
User: what is a function in python?
Alexa: A function in Python is a reusable block of code that performs a specific task. It
"""
response=client.chat.completions.create(model="gemini-2.5-flash",messages=[
    {"role":"system","content":SYSTEM_PROMPT},
    # this is the example of system prompt, you can set the behavior of the model by using system prompt. In this example, we have set the system prompt to "You are a helpful assistant.", which tells the model to behave like a helpful assistant.
    {"role":"user","content":"what is python?"}
    ])
print(response.choices[0].message.content)