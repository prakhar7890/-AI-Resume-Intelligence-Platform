from pypdf import PdfReader
from docx import Document


def read_pdf(uploaded_file):

    text = ""

    pdf = PdfReader(uploaded_file)

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(uploaded_file):

    doc = Document(uploaded_file)

    return "\n".join(
        para.text
        for para in doc.paragraphs
    )


def extract_text(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return read_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return read_docx(uploaded_file)

    elif filename.endswith(".txt"):
        return uploaded_file.read().decode(
            "utf-8"
        )

    return None