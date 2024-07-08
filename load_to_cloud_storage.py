import os
from dotenv import load_dotenv
x=load_dotenv()
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    #https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    #blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)
    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
    
# read the data and produce the embeddings for each of the rows
bucket_name = os.getenv("BUCKET_NAME")
source_file_name = os.getenv("EMBEDDINGS_FILE")
destination_blob_name = os.getenv("DESTINATION_BLOB_NAME")
upload_blob(bucket_name, source_file_name, destination_blob_name)

print("uploaded the blob ", source_file_name, " to: ", bucket_name)
