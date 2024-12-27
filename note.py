from langchain_core.tools import tool

@tool
def note_tool(note):
    """
    Save a note to a local file.

    args:
        note: the text note to save
    """
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
