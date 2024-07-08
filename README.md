# genai_on_google_cloud

This repository gets you started with using VertexAI's GenAI models such as `text-bison` and `gemini-pro`. For grounding of natural language queries we leverage `Vector Search`. It will store the embeddings. In this repository we use OpenAI for doing the embeddings. We will ultimately implement the following architecture that will address many a GenAI application pattern such as *chatbot* or *semantic search*.

![image](https://github.com/Lekha-PRIYA-BHAN/GenAi_on_Google_Cloud/assets/167432155/3bb61a46-23fe-42d0-85fe-e00f7fb2bf01)


Note: In this release we provide a python file to perform the queries instead of a GUI. We implement the *semantic search* in this release.

## Steps

1. Prerequisites including environment setup
2. Setup `Vector Search` with Embeddings
3. Running natural language queries using LLMs such as `text-bison` or `gemini-pro`.


## Prerequisites

1. Ensure you have a Google Cloud `project` that will be used to create all the cloud resources
2. Ensure that you have enabled the required apis in your google project as described [here](https://cloud.google.com/vertex-ai/docs/vector-search/quickstart#enable-apis).
3. Ensure you have an OpenAI key. This will be used for performing the embeddings
4. Install `gcloud` cli on your workstation from where you have cloned this repository
5. Set the access permissions for your *user account* (if you are using that) or the *service account* (if you are using that) as described [here](https://cloud.google.com/vertex-ai/docs/vector-search/quickstart#permissions).
6. Create a *Cloud Storage* bucket using Google Cloud console or gcloud cli. Note the *name* of the bucket as you will need it to update the environment.
7. Edit the `env.txt` file based on the specific parameter values in your environment; rename the file to `.env`
8. On Windows 10 command prompt run `1. setup-env.bat`, and `2. prepare-env.bat` in this order
9. In case of error contact `manish.gupta11@kyndryl.com`

## Vertex AI Vector Search

1. On a Windows 10 command prompt run `3. setup_vector_search.bat`
2. Edit the .env file to set the parameters `INDEX_ENDPOINT_ID` and `DEPLOYED_INDEX_ID` the values for which you would have gotten after completion of the previous step
3. Note we are using `products.json` under the `data` folder as example data to query. This data is about some products. But you can replace the *product names* with the *chunks* from your chunkified documents (.pdf, .docx, etc) - each line will correspond to a chunk. The Step 1 above reads this file and creates embedding for the product names - see file `data_emb.json`*.* If you do not want to regenerate these embeddings then you should mask the line `call python generate_openai_embeddings.py` in the file `3. setup_vector_search.bat`.

The output of Step 1 would be something like this:

```
(envbot) C:\Users\MANISHGUPTA\OneDrive - kyndryl\manish\openai\openai-cookbook\apps\langchain\vertexai>"3. setup_vector_search.bat"

(envbot) C:\Users\MANISHGUPTA\OneDrive - kyndryl\manish\openai\openai-cookbook\apps\langchain\vertexai>call python generate_openai_embeddings.py
Embeddings generated. Check:  ./data/data_emb.json

(envbot) C:\Users\MANISHGUPTA\OneDrive - kyndryl\manish\openai\openai-cookbook\apps\langchain\vertexai>call python load_to_cloud_storage.py
File ./data/data_emb.json uploaded to data_emb.json.
uploaded the blob  ./data/data_emb.json  to:  mg-vs-bucket

(envbot) C:\Users\MANISHGUPTA\OneDrive - kyndryl\manish\openai\openai-cookbook\apps\langchain\vertexai>call python prepare_vector_search.py
manish-learning us-central1 gs://mg-vs-bucket
Creating MatchingEngineIndex
Create MatchingEngineIndex backing LRO: projects/439319997296/locations/us-central1/indexes/3987730761850552320/operations/522751189834530816
MatchingEngineIndex created. Resource name: projects/439319997296/locations/us-central1/indexes/3987730761850552320
To use this MatchingEngineIndex in another session:
index = aiplatform.MatchingEngineIndex('projects/439319997296/locations/us-central1/indexes/3987730761850552320')
********Created index with name:  mg-vs-bucket-index-12161523
<google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex object at 0x000001B70E1E5590>
resource name: projects/439319997296/locations/us-central1/indexes/3987730761850552320
Creating MatchingEngineIndexEndpoint
Create MatchingEngineIndexEndpoint backing LRO: projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288/operations/2019635115981799424
MatchingEngineIndexEndpoint created. Resource name: projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288
To use this MatchingEngineIndexEndpoint in another session:
index_endpoint = aiplatform.MatchingEngineIndexEndpoint('projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288')
********Created index endpoint with name:  vs-mg-vs-bucket-index-ep-12161523
<google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint.MatchingEngineIndexEndpoint object at 0x000001B710837B10>
resource name: projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288
Deploying index MatchingEngineIndexEndpoint index_endpoint: projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288
Deploy index MatchingEngineIndexEndpoint index_endpoint backing LRO: projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288/operations/5874716397010944000
MatchingEngineIndexEndpoint index_endpoint Deployed index. Resource name: projects/439319997296/locations/us-central1/indexEndpoints/4305234535580172288
********Created Deployed index endpoint:  deployed_ep_12161523
```

## Run Queries

In this release we provide a file, named `query.py`, to try out natural language queries. In future we will provide a GUI.

Ensure that you have taken cognizance of Step 2 in the previous section.

Now edit `query.py` and set your natural language query in line 9. You can open file `data/products.json` to craft your query.

Now execute: `python query.py` in the command prompt. You will see a response as below:

```
(envbot) C:\Users\MANISHGUPTA\OneDrive - kyndryl\manish\openai\openai-cookbook\apps\langchain\vertexai>python query.py
MW Women's Swimsuit Two Piece Black Tankini with Bikini Bottoms
Womens MW Tankini Boyshorts Swimsuit Swimwear Fashion prints S-XXL
Womens MW Tankini Boyshorts Swimsuit Swimwear Crisscross Back Multiple Prints S-xxl
Gottex Women's Andromeda Bandeau One Piece Swimsuit
Gottex Women's Chain Reaction Halter One Piece Swimsuit
Gottex Women's Salome V Neck One Piece Swimsuit
Womens swimsuit MW Swimwear Set Halter w/ Boyshorts 2 piece bikini multiple prints
Womens One Piece/bikini Monokini Swimsuit w/ Fringe MW Multiple Prints and Solids
TYR Sport Women's Great White Diamondback Swim Suit
Womens long tankini bikini swimsuit Marina West 2 piece multiple prints bra straps

2023-12-16 18:00:29.796898: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
WARNING:tensorflow:From C:\Users\MANISHGUPTA\OneDrive - kyndryl\manish\openai\openai-cookbook\apps\langchain\vertexai\envbot\Lib\site-packages\keras\src\losses.py:2976: The name tf.losses.sparse_softmax_cross_entropy is deprecated. Please use tf.compat.v1.losses.sparse_softmax_cross_entropy instead.

Response from Model:  text-bison
  Based on the context provided, here are some women's swimsuits that you might be interested in:

- MW Women's Swimsuit Two Piece Black Tankini with Bikini Bottoms
- Womens MW Tankini Boyshorts Swimsuit Swimwear Fashion prints S-XXL
- Womens MW Tankini Boyshorts Swimsuit Swimwear Crisscross Back Multiple Prints S-xxl
- Womens swimsuit MW Swimwear Set Halter w/ Boyshorts 2 piece bikini multiple prints
- Womens One Piece/bikini Monokini Swimsuit w/ Fringe MW Multiple Prints and Solids

These swimsuits come in various styles, including tankinis, one-pieces, and bikinis. They also feature different prints and colors, so you can find the perfect one to suit your taste.
Resonse from Model:  Gemini-pro

Based on the provided context, here are some women's swimsuits that you
 might be interested in:

* MW Women's Swimsuit Two Piece Black
 Tankini with Bikini Bottoms
* Womens MW Tankini Boyshorts Swimsuit Swimwear Fashion prints S-XXL
* Womens MW Tankini Boyshorts Swim
suit Swimwear Crisscross Back Multiple Prints S-xxl
* Womens swimsuit MW Swimwear Set Halter w/ Boyshorts 2 piece bikini multiple prints

* Womens One Piece/bikini Monokini Swimsuit w/ Fringe MW Multiple Prints and Solids

These swimsuits are available in a variety of styles and colors, so you're sure to find one that you love.
