import json
import os
from dotenv import load_dotenv
x=load_dotenv()

from google.cloud import aiplatform

# generate a unique id for this session
from datetime import datetime
UID = datetime.now().strftime("%m%d%H%M")

# create the index
PROJECT_ID=os.getenv("PROJECT_ID")
REGION=os.getenv("REGION")
STAGING_BUCKET_URI="gs://" + os.getenv("BUCKET_NAME")
aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=STAGING_BUCKET_URI)
print(PROJECT_ID, REGION, STAGING_BUCKET_URI)


# create Index
# generate an unique id for this session
bucket_name = os.getenv("BUCKET_NAME")
BUCKET_URI = f"gs://{bucket_name}"
index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
    display_name=f"{bucket_name}-index-{UID}",
    contents_delta_uri=STAGING_BUCKET_URI,
    dimensions=os.getenv("DIMENSIONS"),
    approximate_neighbors_count=os.getenv("APPROXIMATE_NEIGHBORS_COUNT"),
    distance_measure_type=os.getenv("DISTANCE_MEASURE_TYPE")
)

print("********Created index with name: ", f"{bucket_name}-index-{UID}")
print(index)

## create `IndexEndpoint`
index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
    display_name = f"vs-{bucket_name}-index-ep-{UID}",
    public_endpoint_enabled = True
)

print("********Created index endpoint with name: ", f"vs-{bucket_name}-index-ep-{UID}")
print(index_endpoint)

DEPLOYED_INDEX_ID=f"deployed_ep_{UID}"
index_endpoint.deploy_index(index = index, deployed_index_id = DEPLOYED_INDEX_ID)

print("********Created Deployed index endpoint: ", DEPLOYED_INDEX_ID)



