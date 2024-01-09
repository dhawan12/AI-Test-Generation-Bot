# AI-Test-Generation-Bot
Project Overview: The AI Test Generation Bot is designed to process PDF files, extract relevant information, generate embeddings, and create multiple-choice questions based on the content. The project uses technologies such as TensorFlow Hub, PDFMiner, and ReportLab for PDF processing, embedding generation, and PDF export, respectively.

Steps
Step 1: Setting Up the Environment

Ensure that you have the necessary dependencies installed. Key dependencies include TensorFlow, TensorFlow Hub, PDFMiner, and ReportLab.

Step 2: Importing Libraries

  pip install tensorflow tensorflow-hub pdfminer.six reportlab
Step 3: Extracting Text from PDFs

 import asyncio
 from pdfminer.high_level import extract_text
 import tensorflow_hub as hub
from reportlab.pdfgen import canvas
import random
Step 4: Generating Embeddings

async def extract_text_from_pdf(pdf_path):
text = await asyncio.to_thread(extract_text, pdf_path)
return text
Step 5: Generating Multiple-Choice Questions

def generate_multiple_choice_question(embeddings, num_choices=4,        bias_mitigation=True):
return question, choices
Step 6: User Interface

def user_interface():
extracted_texts = loop.run_until_complete(process_pdfs(pdf_paths))
for extracted_text in extracted_texts:
    embeddings = generate_embeddings(extracted_text)
    questions = []
    for _ in range(num_questions):
        question, choices = generate_multiple_choice_question(embeddings, bias_mitigation=apply_bias_mitigation)
        questions.append((question, choices))
    export_to_pdf_multi(questions, difficulty_level)
    print(f"\nTest exported to 'generated_test.pdf'.")
Step 7: Exporting Questions to PDF

def export_to_pdf_multi(questions, difficulty_level, pdf_path=r"C:\Users\bardw\Desktop\PDF Processing\generated_test.pdf"):
c = canvas.Canvas(pdf_path)
c.save()
Step 8: Scalability and Architecture

Consider architectural designs that can handle large volumes of PDF files efficiently. Optimize the code for scalability, ensuring it can process multiple files seamlessly.

Step 9: Evaluation Criteria

Evaluate the AI Test Generation Bot based on the following criteria: Accuracy of PDF processing and information extraction. Quality of generated embeddings, capturing key concepts and relationships. Relevance, clarity, and grammatical correctness of generated test questions. Diversity of question types and difficulty levels. Usability and intuitiveness of the user interface. Ability to handle different types of content through PDF.

Step 10: Documentation

Document the entire project, including setup instructions, code snippets, and explanations for each step. Include details on dependencies, libraries used, and the overall project structure.

Conclusion
The AI Test Generation Bot project provides a robust solution for generating tests from PDF content. The system extracts information, generates embeddings, and creates diverse and relevant multiple-choice questions. Scalability considerations and an evaluation framework ensure the project's effectiveness and usability.


Summary Report
Approach Taken

PDF Processing: Used PDFMiner to extract text from PDF files asynchronously. Embedding Generation: Utilized TensorFlow Hub for generating embeddings using a pre-trained Universal Sentence Encoder.

Question Generation: Developed a function to create multiple-choice questions based on embeddings with an option for bias mitigation.

User Interface: Built a simple command-line interface for user interaction.

Challenges Faced
TensorFlow Compatibility: Faced compatibility issues with TensorFlow versions. Resolved by ensuring the appropriate version is installed.

PDF Text Extraction: Handling variations in PDF formats required adjusting the extraction process.

Suggestions for Improvement
Enhanced Bias Mitigation: Implement more sophisticated bias mitigation strategies for diverse and fair question generation.

User Interface Improvement: Develop a graphical user interface (GUI) for better usability.

Scalability: Optimize the code for scalability, allowing the application to efficiently process a large number of PDF files.


Demo Video Link -
https://drive.google.com/file/d/1PtQnYv2FKnRhNnjODbgkk40qHf8-bwLF/view?usp=drive_link
