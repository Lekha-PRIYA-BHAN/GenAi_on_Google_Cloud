import json
import os
from dotenv import load_dotenv
x=load_dotenv()

from google.cloud import aiplatform

# create the index
PROJECT_ID=os.getenv("PROJECT_ID")
REGION=os.getenv("REGION")
STAGING_BUCKET_URI="gs://" + os.getenv("BUCKET_NAME")
aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=STAGING_BUCKET_URI)
print(PROJECT_ID, REGION, STAGING_BUCKET_URI)


# create Index
# generate an unique id for this session
bucket_name = os.getenv("BUCKET_NAME")

## create `IndexEndpoint`
my_index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
    display_name = f"vs-{bucket_name}-index-ep-{UID}",
    public_endpoint_enabled = True
)
