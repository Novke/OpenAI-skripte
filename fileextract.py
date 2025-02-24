import os
import time
import openai
from openai._types import NotGiven
from openai.types.beta.threads import message_create_params


    # pdf_path = "input/CV.pdf"
    # API_KEY = os.getenv("APIKEY_XENON_OPENAI")
    # "You analyze PDF documents and answer questions based on them."

def analyze_from_file(api_key, pdf_path, instructions, question, show_logs=False):
    # OpenAI API Key

    # Initialize OpenAI client
    client = openai.OpenAI(api_key=api_key)

    # Step 1: Upload the PDF file
    with open(pdf_path, "rb") as file:
        uploaded_file = client.files.create(
            file=file,
            purpose="assistants"
        )

    file_id = uploaded_file.id
    if show_logs:
        print(f"File uploaded successfully: {file_id}")

    # Step 2: Create an Assistant (if not already created)
    assistant = client.beta.assistants.create(
        name="PDF Analyzer",
        instructions=instructions,
        model="gpt-4-turbo",
        tools=[{"type": "file_search"}]
    )
    assistant_id = assistant.id
    if show_logs:
        print(f"Assistant created: {assistant_id}")

    # Step 3: Create a thread
    thread = client.beta.threads.create()
    thread_id = thread.id

    # Step 4: Create a message with the file as an attachment
    attachments = [
        message_create_params.Attachment(
            file_id=file_id, 
            tools=[{"type": "file_search"}]
        )
    ]

    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=question,
        attachments=attachments
    )

    # Step 5: Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    if show_logs:
        print("Processing your request...")

    # Step 6: Wait for response and fetch the answer
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run_status.status == "completed":
            break
        time.sleep(2)  # Wait before checking again

    # Step 7: Get the response
    messages = client.beta.threads.messages.list(thread_id=thread_id)

    for msg in messages.data:
        for content_block in msg.content:  # Iterate over content blocks
            if content_block.type == "text":  # Ensure it's text content
                return content_block.text.value  # ✅ Extract only the text value