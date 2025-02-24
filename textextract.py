from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader

    # Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
        reader = PdfReader(pdf_path)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    
def analyze_from_text(api_key, pdf_path, instructions, question, show_logs=False):

    pdf_text = extract_text_from_pdf(pdf_path)

    chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.1, api_key=api_key)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", instructions),
            ("human", f"{question}\n\nHere is the file content:\n{pdf_text}"),
        ]
    )

    chain = prompt | chat

    response = chain.invoke({})
    return response.content
