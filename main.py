import os
from fileextract import analyze_from_file
from textextract import analyze_from_text
from jsonextract import *
from basicgpt import ask_gpt
import json

PDF_PATH = "input/CV.pdf"
TMPL_PATH = "input/example1.json"
API_KEY = os.getenv("APIKEY_XENON_OPENAI")
PROMPT = "You analyze PDF documents of CVs and detect specific details in them, and return them formatted in a json based on a template provided." 

with open(TMPL_PATH, "r", encoding="utf-8") as file:
    TEMPLATE = json.load(file)
    
QUESTION = "Template of the json is: " + json.dumps(TEMPLATE)


print("File analyze:")
response1 = analyze_from_file(API_KEY, PDF_PATH, instructions=PROMPT, question=QUESTION)
print(response1)
json1 = extract_json(response1)
print(get_json_value(json1, "personalInfo.name"))
print(get_json_value(json1, "languages.1.proficiency"))
print(get_json_value(json1, "technicalSkills.programmingLanguages.0"))

# print("Text analyze:")
# TODO exception jer se u promptu salju "" koje treba escapovati
# response2 = analyze_from_text(API_KEY, PDF_PATH, PROMPT, QUESTION)
# print(response2)

# print("Basic question")
# response3 = ask_gpt(
#     API_KEY, 
#     instructions="You are a comedian", 
#     question="Tell me a joke about pigs")
# print(response3)