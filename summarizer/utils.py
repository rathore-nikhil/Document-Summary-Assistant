import fitz  # PyMuPDF
from PIL import Image
import pytesseract
from transformers import pipeline
import nltk

nltk.download('punkt')

summarizer = pipeline("summarization")

def extract_text_from_pdf(file_path):
    text = ""
    pdf_document = fitz.open(file_path)
    for page in pdf_document:
        text += page.get_text()
    return text

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

def generate_summary(text, ratio=0.2):
    try:
        total_words = len(text.split())
        target_word_count = max(10, int(total_words * ratio)) 
        max_length = min(1000, target_word_count + 20)  
        min_length = max(5, int(target_word_count / 2))

        # Use the summarization pipeline
        summary = summarizer(
            text, 
            max_length=max_length, 
            min_length=min_length, 
            do_sample=False
        )[0]["summary_text"]

        # Highlight key points by extracting sentences
        key_points = extract_key_points(text)

        return {
            "summary": summary,
            "key_points": key_points
        }
    except ValueError:
        return "Text is too short to summarize."

def extract_key_points(text, max_points=5):
    # Split the text into sentences using a simple method
    sentences = text.replace('!', '.').replace('?', '.').split('. ')
    
    # Define keywords for identifying key points
    keywords = ['important', 'key', 'notable', 'significant', 'main', 'highlight', 'crucial', 'essential', 'noteworthy', 'critical']
    key_points = []

    # Score sentences based on keyword presence and length
    sentence_scores = []
    for sentence in sentences:
        score = 0
        # Increase score for each keyword found
        for keyword in keywords:
            if keyword in sentence.lower():
                score += 1
        # Increase score for longer sentences
        if len(sentence.split()) > 15:
            score += 1
        
        # Append the sentence and its score
        sentence_scores.append((sentence.strip(), score))

    # Sort sentences by score in descending order
    sentence_scores.sort(key=lambda x: x[1], reverse=True)

    # Select the top scoring sentences as key points
    for sentence, score in sentence_scores[:max_points]:
        if score > 0:  # Only include sentences with a positive score
            key_points.append(sentence)

    return key_points