from google import genai
client=genai.Client(
    api_key="AIzaSyAwjxpH0OQy0zKt3y8rRs5QV0schx6Zbio"
)
response=client.models.generate_content(model="gemini-2.5-flash",contents="hii?")
