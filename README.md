# Document Summary Assistant

## Overview
The Document Summary Assistant is a web application built using Django that allows users to upload documents (PDFs and images) and receive concise summaries along with key points extracted from the content. This tool leverages advanced natural language processing techniques to provide meaningful insights from lengthy documents.

## Features
* **File Upload:** Users can upload PDF or image files containing text.
* **Text Extraction:** The application extracts text from uploaded documents using OCR for images and text extraction for PDFs.
* **Summarization:** Generates a summary of the document based on user-defined length (short, medium, long).
* **Key Points Extraction:** Identifies and highlights key points from the document.
* **User -Friendly Interface:** Simple and intuitive web interface for easy navigation.

## Technologies Used
* **Backend:** Django 4.2
* **Frontend:** HTML, CSS
* **Text Processing:** Hugging Face Transformers, PyMuPDF, Tesseract OCR
* **Database:** SQLite

## Installation
### Prerequisites
* Python 3.8 or higher
* pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rathore-nikhil/Document-Summary-Assistant.git
   cd Document_Summary_Assistant

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
4. **Run database migrations:**
   ```bash
   python manage.py migrate
5. **Start the development server:**
    ```bash
   python manage.py runserver
6. **Access the application:** Open your web browser and go to **http://127.0.0.1:8000/**.

## Usage
* Navigate to the home page.
* Upload a document (PDF or image).
* Select the desired summary length (short, medium, long).
* Click the "Upload" button.
* View the generated summary and key points on the results page.

