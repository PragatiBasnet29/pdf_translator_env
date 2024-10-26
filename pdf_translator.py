import fitz  # PyMuPDF
from tkinter import Tk, filedialog

#select_pdf_file(): Opens a file dialog to select a PDF file and returns its path.
#extract_text_from_pdf(pdf_path): Extracts and returns the text from the selected PDF.
def select_pdf_file():
    # Initialize Tkinter and hide the root window
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF file"
    )
    return file_path

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf: # open the pdf
        for page_num in range(pdf.page_count): #count the no of pages
            page = pdf[page_num]
            text += page.get_text() #Extracts text from each page and appends it to text.
    return text

if __name__ == "__main__":
    pdf_path = select_pdf_file()
    if pdf_path:
        pdf_text = extract_text_from_pdf(pdf_path)
        print(pdf_text[:1000])  # Print the first 1000 characters as a sample
    else:
        print("No file was selected.")
