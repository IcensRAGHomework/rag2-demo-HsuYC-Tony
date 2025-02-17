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
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    pdf_text = ""
    for doc in docs:
        pdf_text += doc.page_content + "\n"
    # Define text splitters
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10, chunk_overlap=0, separators=["   第\\s.+\\s章\\s", "第 \\d+ 條\n", "第 \\d+-\\d 條\n"], is_separator_regex=True
    )
    # Split text by splitter
    recursive_chunks = recursive_splitter.split_text(pdf_text)

    return len(recursive_chunks)
