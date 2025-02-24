import os
from fileextract import analyze_from_file
from textextract import analyze_from_text
from basicgpt import ask_gpt

PDF_PATH = "input/CV.pdf"
API_KEY = os.getenv("APIKEY_XENON_OPENAI")
PROMPT = "You analyze PDF documents of CVs and detect specific details in them" 
QUESTION = "What is the education of this candidate?"

print("File analyze:")
response1 = analyze_from_file(API_KEY, PDF_PATH, instructions=PROMPT, question=QUESTION)
print(response1)

print("Text analyze:")
response2 = analyze_from_text(API_KEY, PDF_PATH, PROMPT, QUESTION)
print(response2)

print("Basic question")
response3 = ask_gpt(
    API_KEY, 
    instructions="You are a comedian", 
    question="Tell me a joke about pigs")
print(response3)