import os
import PyPDF2
import pyttsx3

# Getting current directory
cwd = os.getcwd()

# Construct the path to the PDF directory and join PDF name to path
pdf_path = os.path.join(cwd, 'samplepdf.pdf')


# Open the PDF file in read-binary mode
with open(pdf_path, 'rb') as file:

    # Create a PDF object
    pdf = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF
    num_pages = len(pdf.pages)

    # Iterate through each page
    for i in range(num_pages):
        # Get the text from the current page
        text = pdf.pages[i].extract_text()

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set the volume
        engine.setProperty('volume', 1.0)

        # Set the rate of speech
        engine.setProperty('rate', 150)

        # Save the audio to a file
        engine.save_to_file(text, 'AudioBook.mp3')

        # Run and wait for the speech to finish
        engine.runAndWait()
    
    print("******************\nAudioBook Created!\n******************\nCheck current folder")
