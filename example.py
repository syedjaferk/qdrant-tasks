from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus


client = QdrantClient(host="localhost", port=6333)
print(client)

my_collection = "first_collection"

first_collection = client.recreate_collection(
    collection_name=my_collection,
    vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE)
)
print(first_collection)

collection_info = client.get_collection(collection_name=my_collection)
print(list(collection_info))