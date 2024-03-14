from openai import OpenAI
import os 

# getting the Environment Varaible
api_key_openai = os.environ.get('OPENAPI_KEY')

# initializing the OpenAI library
client = OpenAI(api_key=api_key_openai)

# asking the question
question = input('Question: ')

# creating the message
message = [
    {
        'role': 'user',
        'content': question
    }
]

# Send the message to OpenAI
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=message,
    temperature=0
)

# Printing the response
print(response.choices[0].message.content)

