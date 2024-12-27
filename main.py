from dotenv import load_dotenv
import os

from langchain_cohere import CohereEmbeddings
  # Import Cohere for text generation
from langchain_astradb import AstraDBVectorStore
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from github import fetch_github_issues
from note import note_tool

load_dotenv()

def connect_to_vstore():
    # Load the API key from environment variables
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise ValueError("COHERE_API_KEY environment variable is not set.")

    # Initialize embeddings with the required model parameter
    embeddings = CohereEmbeddings(model="embed-english-v3.0")  # Specify the model you want to use

    # Load other necessary environment variables
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    desired_namespace = os.getenv("ASTRA_DB_KEYSPACE")

    if desired_namespace:
        ASTRA_DB_KEYSPACE = desired_namespace
    else:
        ASTRA_DB_KEYSPACE = None

    # Initialize the vector store
    vstore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name="github",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )
    return vstore

# Connect to the vector store
vstore = connect_to_vstore()

# Ask the user if they want to update the issues
add_to_vectorstore = input("Do you want to update the issues? (y/N): ").lower() in ["yes", "y"]

if add_to_vectorstore:
    owner = "techwithtim"
    repo = "Flask-Web-App-Tutorial"
    issues = fetch_github_issues(owner, repo)

    try:
        vstore.delete_collection()
    except Exception as e:
        print(f"Error deleting collection: {e}")

    # Reconnect to the vector store after deletion
    vstore = connect_to_vstore()
    vstore.add_documents(issues)

# Create a retriever from the vector store
retriever = vstore.as_retriever(search_kwargs={"k": 3})
retriever_tool = create_retriever_tool(
    retriever,
    "github_search",
    "Search for information about github issues. For any questions about github issues, you must use this tool!",
)

# Initialize Cohere for text generation
cohere_client = Cohere(api_key=os.getenv("COHERE_API_KEY"))

# Main loop for user questions
while (question := input("Ask a question about github issues (q to quit): ")) != "q":
    # Use Cohere to generate a response based on the question
    response = cohere_client.generate(
        model="command-xlarge-20221108",  # Specify the model you want to use for text generation
        prompt=question,
        max_tokens=100  # Adjust as needed
    )
    print(response.generations[0].text)  # Print the generated response