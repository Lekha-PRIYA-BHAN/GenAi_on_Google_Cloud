import os
from dotenv import load_dotenv
x=load_dotenv()

from openai import OpenAI

def get_embedding(text):
    
    client = OpenAI()

    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

#print(len(get_embedding("Your text string goes here")))
