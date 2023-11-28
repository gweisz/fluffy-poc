import chromadb
import requests

# ChromaDB
chromaDBClient = chromadb.Client()

# Some test documents
collection = chromaDBClient.create_collection("sample_collection")

collection.add(
    documents=["This is a SPAM, it has the word SPAM several times in it! SPAM SPAM SPAM",
               "This is a completely normal posting"],
    metadatas=[{"tag": "spam"}, {"tag": "no-spam"}],
    ids=["doc1", "doc2"],
)

# Query example
NEW_POST = "A new post"

results = collection.query(
    query_texts=[NEW_POST],
    where={"tag": "spam"},
    n_results=1,
)

SPAM_EXAMPLE = results["documents"][0][0]

results = collection.query(
    query_texts=[NEW_POST],
    where={"tag": "no-spam"},
    n_results=1,
)

NO_SPAM_EXAMPLE = results["documents"][0][0]

# chat example

URL = 'http://localhost:11434/api/generate'

PROMPT = "As an AI assistant you job is to decide if new posts can be considered spam. " + \
    "A person is requesting the creation of a new post with the following content: '" + \
    NEW_POST + \
    "'. The following is the closest known example of a post that's considered spam: '" + \
    SPAM_EXAMPLE + \
    "'. And the following is the closest known example of a post that's not considered spam: '" + \
    NO_SPAM_EXAMPLE + \
    "'. Please answer YES or NO only."

DATA = '''{
  "model": "llama2",
  "stream": false,
  "prompt": "''' + PROMPT + '"}'

print("Request: " + DATA)
response = requests.post(URL, data=DATA)
print("Response: " + response.text)
