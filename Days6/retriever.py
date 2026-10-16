from pathlib import Path
def load_document():
    documents={}
    folder=Path('knowledge')
    for file in folder.glob("*.txt"):
        documents[file.name]=file.read_text(encoding="utf-8")

    return documents

def retrieve(question):
    document=load_document()
    question=question.lower()
    for filename,content in document.items():
        if question in content.lower():
            return filename,content
    return None, None
