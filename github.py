import os
import requests
from dotenv import load_dotenv
from langchain.docstore.document import Document


load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")  # Fixed environment variable name

def fetch_github(owner, repo, endpoint):
    # Corrected API URL
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {github_token}"  # Authorization header
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print("Failed with status code:", response.status_code)
        print("Error message:", response.text)  # Print error details
        return []
    

def fetch_github_issues(owner, repo):
    data = fetch_github(owner,  repo, "issues")
    return load_issues(data)

def load_issues(issues):
    docs = []

    for entry in issues:
        metadata ={
            "author": entry["user"]["login"],
            "comments": entry["comments"],
            "body": entry["body"],
            "label": entry.get("labels", ["No Label"]),

            "created_at":entry["created_at"]
        }

        data = entry["title"]
        if entry["body"]:
            data += entry["body"]
        doc = Document(page_content=data, metadata=metadata)
        docs.append(doc)

    return docs




owner = "techwithtim"
repo = "Flask-Web-App-Tutorial"
endpoint = "issues"

fetch_github_issues(owner, repo)
