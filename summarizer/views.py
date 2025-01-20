from django.shortcuts import render
from .forms import DocumentForm
from .utils import extract_text_from_pdf, extract_text_from_image, generate_summary

# Create your views here.
def upload_document(request):
    summary = ""
    key_points = []
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            file_path = document.uploaded_file.path
            summary_length = form.cleaned_data['summary_length']

            # Extract text based on file type
            if file_path.endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            else:
                text = extract_text_from_image(file_path)

            # Generate summary
            ratio = 0.2 if summary_length == 'short' else 0.3 if summary_length == 'medium' else 0.4
            result = generate_summary(text, ratio)  # Get the result from generate_summary

            # Check if result is a string
            if isinstance(result, str):
                summary = result 
            else:
                summary = result['summary']  # Extract summary
                key_points = result['key_points']  # Extract key points

            return render(request, 'summary.html', {'summary': summary, 'key_points': key_points})
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form, 'summary': summary})