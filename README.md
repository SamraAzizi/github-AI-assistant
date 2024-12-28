# GitHub Issues Analyzer

This project is a GitHub Issues Analyzer that leverages LangChain, Cohere, and AstraDB Vector Store to fetch, process, and analyze GitHub issues from a specified repository. The application integrates tools for managing and searching GitHub issues, saving notes, and generating responses using Cohere's language model.

## Features

### Fetch GitHub Issues:
- Retrieves GitHub issues from a specified repository using the GitHub API.

### Vector Store Integration:
- Uses AstraDB Vector Store to store and retrieve issue data.

### Embeddings:
- Employs Cohere embeddings to encode issue data for efficient storage and retrieval.

### Question and Answer:
- Allows users to ask questions about GitHub issues, using Cohere for text generation.

### Notes Management:
- Provides functionality to save notes locally.

## Installation

### Prerequisites
- Python 3.8+
- A GitHub Personal Access Token
- A Cohere API Key
- AstraDB credentials

### Environment variable setup (.env file)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

```

# Usage
# Running the Application

# Start the application:

# Run the command in the terminal
python main.py

# Follow the prompts to:
# - Update GitHub issues in the vector store.
# - Ask questions about GitHub issues.

# Saving Notes
# Use the note_tool to append text notes to notes.txt.

# File Descriptions

## github.py
# Handles fetching and processing GitHub issues using the GitHub API.
# Defines the following functions:
# - fetch_github(owner, repo, endpoint)
# - fetch_github_issues(owner, repo)
# - load_issues(issues)

## main.py
# Coordinates the main application logic.
# - Connects to the AstraDB vector store.
# - Manages issue fetching, storage, and retrieval.
# - Integrates Cohere for embeddings and text generation.

## note.py
# Defines the note_tool for saving notes to a local file (notes.txt).

# Requirements
# Ensure you have the following Python libraries installed:
# - requests
# - python-dotenv
# - langchain
# - cohere
# - langchain_cohere
# - langchain_astradb

# Example Workflow
# Fetch issues from a repository:
# - Specify the owner and repository name in main.py.
# - Store issues in AstraDB Vector Store.
# - Ask questions about the issues and get AI-generated responses.
# - Save any relevant notes.

# Future Enhancements
# - Add support for fetching more GitHub metadata (e.g., pull requests).
# - Expand the note-taking tool to support tagging and categorization.
# - Implement a web interface for easier interaction.

# Troubleshooting
# - Ensure the .env file is correctly configured.
# - Verify that your GitHub token has sufficient permissions to access repository issues.
# - Check the network connection if API calls fail.
