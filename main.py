import os
from fileextract import analyze_from_file
from textextract import analyze_from_text
from jsonextract import *
from basicgpt import ask_gpt
import json

PDF_PATH = "input/CVjusufML.docx"
TMPL_PATH = "jsonexamples/example3.json"
API_KEY = os.getenv("APIKEY_XENON_OPENAI")
PROMPT = "You analyze PDF or DOC documents of CVs and detect specific details in them, and return them formatted in a json based on a template provided. Extract all the data you can find in the CV in the JSON example provided, and if there isnt such data for a certain field, just leave a simple '/'" 

with open(TMPL_PATH, "r", encoding="utf-8") as file:
    TEMPLATE = json.load(file)
    
QUESTION = "Template of the json is: " + json.dumps(TEMPLATE)

def print_node(json1, node):
    print("Node:", node)
    print(get_json_value(json1, node))


print("File analyze:")
response1 = analyze_from_file(API_KEY, PDF_PATH, instructions=PROMPT, question=QUESTION)
print(response1)
json1 = extract_json(response1)
print_node(json1, "personalInfo.name:")
print_node(json1, "languages.1.proficiency")
print_node(json1, "technicalSkills.programmingLanguages.0")
print_node(json1, "certifications")
print_node(json1, "hobbies.0")
print_node(json1, "projects")
print_node(json1, "projects.0.title")

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