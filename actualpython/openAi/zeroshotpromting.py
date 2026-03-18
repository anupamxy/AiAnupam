# zero shot prompting is a technique in natural language processing (NLP) where a model is given a task or question without any prior examples or training on that specific task. The model is expected to generate a response based solely on its understanding of the language and the context provided in the prompt. This approach is often used to evaluate the generalization capabilities of language models, as it tests their ability to apply learned knowledge to new and unseen tasks.
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI(
    api_key="AIzaSyAwjxpH0OQy0zKt3y8rRs5QV0schx6Zbio",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
SYSTEM_PROMPT="You are a helpful assistant. you need to answer only coding related answeers. your name is alexa"
response=client.chat.completions.create(model="gemini-2.5-flash",messages=[
    {"role":"system","content":SYSTEM_PROMPT},
    # this is the example of system prompt, you can set the behavior of the model by using system prompt. In this example, we have set the system prompt to "You are a helpful assistant.", which tells the model to behave like a helpful assistant.
    {"role":"user","content":"what is python?"}
    ])
print(response.choices[0].message.content)
# zero shot prompting is a powerful technique that allows language models to demonstrate their understanding of language and context without relying on specific training examples. By providing clear and concise prompts, we can guide the model to generate relevant and accurate responses, even for tasks it has not been explicitly trained on.