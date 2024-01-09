import asyncio
from pdfminer.high_level import extract_text
import tensorflow_hub as hub
from reportlab.pdfgen import canvas
import random

# Function to extract text from a PDF file
async def extract_text_from_pdf(pdf_path):
    text = await asyncio.to_thread(extract_text, pdf_path)
    return text

# Function to generate embeddings using TensorFlow Hub
def generate_embeddings(text):
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    embeddings = embed([text])
    return embeddings.numpy()

# Function to generate multiple-choice question with bias mitigation
def generate_multiple_choice_question(embeddings, num_choices=4, bias_mitigation=True):
    # Placeholder for question generation logic
    # You can use spaCy for text processing and generate questions based on the embeddings
    # Modify this function according to your specific requirements

    # For now, let's create a simple example question
    question = "What is the meaning of the given data?"

    # Generate random choices (you can replace this with a more sophisticated method)
    choices = [f"{chr(65 + i)}. Option {i+1}" for i in range(num_choices)]

    if bias_mitigation:
        # Apply bias mitigation strategies (customize based on your bias identification)
        # For example, ensure diverse representation in choices
        choices = mitigate_bias(choices)

    return question, choices

# Bias mitigation strategy (example)
def mitigate_bias(choices):
    # Implement bias mitigation logic here
    # For instance, ensure diverse representation in choices
    # You can add more sophisticated strategies based on your bias analysis
    return choices

# Function to process PDF files asynchronously
async def process_pdfs(pdf_paths):
    tasks = [extract_text_from_pdf(pdf_path) for pdf_path in pdf_paths]
    return await asyncio.gather(*tasks)

# Function to get user input and generate the test
def user_interface():
    print("Welcome to the AI Test Generation Bot!")

    # Allow the user to customize test settings
    num_questions = int(input("Enter the number of questions (default is 1): ") or 1)
    difficulty_level = input("Enter the difficulty level (easy, medium, hard - default is medium): ") or "medium"
    apply_bias_mitigation = input("Apply bias mitigation? (yes/no - default is yes): ").lower() != "no"

    pdf_paths = input("Enter the paths of the PDF files (comma-separated): ").split(",")
    pdf_paths = [pdf_path.strip().strip('\"') for pdf_path in pdf_paths]

    # Asynchronously process PDF files
    loop = asyncio.get_event_loop()
    extracted_texts = loop.run_until_complete(process_pdfs(pdf_paths))

    # Further processing with extracted_texts
    for extracted_text in extracted_texts:
        embeddings = generate_embeddings(extracted_text)

        # Generate multiple-choice questions based on user settings
        questions = []
        for _ in range(num_questions):
            question, choices = generate_multiple_choice_question(embeddings, bias_mitigation=apply_bias_mitigation)
            questions.append((question, choices))

        # Export the generated test to a PDF
        export_to_pdf_multi(questions, difficulty_level)

        print(f"\nTest exported to 'generated_test.pdf'.")

# Function to export multiple questions to a PDF
def export_to_pdf_multi(questions, difficulty_level, pdf_path=r"C:\Users\bardw\Desktop\PDF Processing\generated_test.pdf"):
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 800, f"Generated Test Questions (Difficulty: {difficulty_level}):")
    y_position = 780
    for idx, (question, choices) in enumerate(questions, start=1):
        c.drawString(100, y_position, f"{idx}. Question: {question}")
        y_position -= 20
        for choice in choices:
            c.drawString(120, y_position, f"{choice}")
            y_position -= 20
        y_position -= 10  # Add some space between questions
    c.save()

if __name__ == "__main__":
    user_interface()
