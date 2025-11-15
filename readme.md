### The project deals with a small LLM based application that answers questions based on the pdf RentalConditions.pdf

### Have created a FASTAPI that takes gpt model and query from the user to give the response back.

### Have dockerized the application in a local docker container. Refer Dockerfile. Make sure docker desktop is installed on your machine.

### To build docker file

docker build -t stargazer/rag .  

### To run docker file locally

docker run --env-file .env -p 8000:8000 stargazer/rag

### Streamlit frontend can also be hosted on a separate docker image and both the images can interact

### Tech Stack used:

1. Python FastAPI
2. Langchain
3. GPT generative and embeddings LLMs
4. Python Streamlit
5. Chroma vector DB
6. Python Pydantic

## Streamlit app that is hitting the base url - BASE_URL = http://0.0.0.0:8000

![alt text](image.png)