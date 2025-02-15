from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    pdf_text = ""
    for doc in docs:
        pdf_text += doc.page_content
    # Define text splitter
    char_splitter = CharacterTextSplitter(
        chunk_overlap=0
    )
    # # Split text by splitter
    char_chunks = char_splitter.split_documents(docs)

    return char_chunks[-1]

def hw02_2(q2_pdf):
    print('0')
    pass
