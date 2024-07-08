import json
import ast
from google.cloud import aiplatform
import os
from dotenv import load_dotenv
x=load_dotenv()
from openai_embedding import get_embedding

query="looking for women's swimsuit"


# build dicts for product names and embs
product_names = {}
product_embs = {}
with open(os.getenv("EMBEDDINGS_FILE")) as f:
    for l in f.readlines():
        try:
            p = json.loads(l.strip().replace("'", "\""))
        except:
            #print("The exception is with: ", l)
            p = ast.literal_eval(l.strip())
        id = p['id']
        #print(id)
        product_names[id] = p['name']
        product_embs[id] = p['embedding']

#query_emb = product_embs['13928']

#print(query_emb)


index_endpoint_id = os.getenv("INDEX_ENDPOINT_ID")
index_endpoint = aiplatform.MatchingEngineIndexEndpoint(index_endpoint_id)

DEPLOYED_INDEX_ID = os.getenv("DEPLOYED_INDEX_ID")

query_embedding = get_embedding(query)

# run query
response = index_endpoint.find_neighbors(
    deployed_index_id = DEPLOYED_INDEX_ID,
    queries = [query_embedding],
    num_neighbors = 10
)

# show the results
#for idx, neighbor in enumerate(response[0]):
#    print(f"{neighbor.distance:.2f} {product_names[neighbor.id]}")

# show the results
number_of_products_for_context=10
context = ""
for idx, neighbor in enumerate(response[0]):
    if number_of_products_for_context > 0:
        context += f"{product_names[neighbor.id]}" + "\n"
        number_of_products_for_context -= 1
    else:
        break

print(context)


prompt=f"""
Return an appropriate response to the query below but based on the context provided after the query.

query:
-----
{query}

context:
-----
{context}
"""

import vertexai
from vertexai.language_models import TextGenerationModel
vertexai.init(project=os.getenv("PROJECT_ID"), location=os.getenv("REGION"))
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained(os.getenv("MODEL"))
response = model.predict(
    prompt,
    **parameters
)
print("Response from Model: ", os.getenv("MODEL")+"\n", f"{response.text}")

from vertexai.preview.generative_models import GenerativeModel, Part

def generate(prompt):
  model = GenerativeModel("gemini-pro")
  responses = model.generate_content(
    prompt,
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    },
  stream=True,
  )

  print("\n\n")
  print("Resonse from Model: ", "Gemini-pro\n")
  for response in responses:
      print(response.candidates[0].content.parts[0].text)

generate(prompt)

