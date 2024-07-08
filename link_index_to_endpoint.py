# https://cloud.google.com/vertex-ai/docs/vector-search/quickstart#get_an_existing_index
import os
from dotenv import load_dotenv
x=load_dotenv()

from google.cloud import aiplatform

# generate a unique id for this session
from datetime import datetime
UID = datetime.now().strftime("%m%d%H%M")

PROJECT_ID=os.getenv("PROJECT_ID")
REGION=os.getenv("REGION")
STAGING_BUCKET_URI="gs://" + os.getenv("BUCKET_NAME")
aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=STAGING_BUCKET_URI)

index_id = os.getenv("INDEX_ID")
index_endpoint_id = os.getenv("INDEX_ENDPOINT_ID")

index = aiplatform.MatchingEngineIndex(index_id)
index_endpoint = aiplatform.MatchingEngineIndexEndpoint(index_endpoint_id)


DEPLOYED_INDEX_ID=f"deployed_endpoint_{UID}"
index_endpoint.deploy_index(index = index, deployed_index_id = DEPLOYED_INDEX_ID)

print(index_endpoint)

#Resource name: projects/439319997296/locations/us-central1/indexes/8080939873176911872
#To use this MatchingEngineIndex in another session:
#index = aiplatform.MatchingEngineIndex('projects/439319997296/locations/us-central1/indexes/8080939873176911872')
