import json
from openai_embedding import get_embedding
import os
from dotenv import load_dotenv
x=load_dotenv()

def add_embeddings(json_line, json_emb_file):
    # Process each JSON object here
    # For example, you might want to print it or perform some calculations
    json_line['embedding'] = get_embedding(json_line['name'])
    #print(json_line)
    json_emb_file.write(str(json_line))
    json_emb_file.write("\n")
    
    
def read_chunks_file(file_path, json_emb_file):
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Parse the JSON line into a Python dictionary
                json_line = json.loads(line.strip())
                # Process the JSON object
                add_embeddings(json_line, json_emb_file)
            except json.JSONDecodeError as e:
                # Handle potential errors in JSON parsing
                print(f"Error parsing JSON: {e}")
    file.close()

embeddings_file = open(os.getenv("EMBEDDINGS_FILE"), "w")
read_chunks_file(os.getenv("CHUNKS_FILE"), embeddings_file)
embeddings_file.close()

print("Embeddings generated. Check: ", os.getenv("EMBEDDINGS_FILE"))
