import tiktoken
enc=tiktoken.encoding_for_model("gpt-3.5-turbo")
text="Hello, how are you doing today?"
tokens=enc.encode(text)
print(tokens)

# output [9906, 11, 1268, 527, 499, 3815, 3432, 30]
decoded_text=enc.decode(tokens)
print(decoded_text)