from retriever import load_document
from retriever import retrieve

documents=load_document()




filename,content= retrieve("abc")
print(filename)
print()
print(content)