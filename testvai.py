import vertexai
from vertexai.language_models import TextGenerationModel

query="looking for a low profile cap"

prompt=f"""
Return an appropriate response to the query below but based on the context provided after the query.
{query}

{context}
"""

vertexai.init(project="manish-learning", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")
response = model.predict(
    """What is google?""",
    **parameters
)
print(f"Response from Model: {response.text}")
