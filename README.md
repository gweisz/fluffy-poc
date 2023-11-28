# Title

Fluffy POC

# Prerequisites

## ChromaDB

`pip install chromadb`

## OLLama

### Run container

`docker run -d -p 11434:11434 --name ollama ollama/ollama`

### Install llama2 within container

`docker exec -it ollama ollama run llama2`

### Test call

`curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "stream": false,
  "prompt": "Why is the sky blue?"
}'`

NOTE: This might take a long time if using the CPU version

# Recomendations

* Setup a new python virtual environment
* upgrade pip
