from ollama import generate
# Regular response
response = generate('llama3.1:8b', 'Why is the sky blue?')
print(response['response'])
