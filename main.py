import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("files/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case.
    filename = Path(filepath).stem
    subject = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{subject}", ln=1)

    # Get the content of each text file
    with open(filepath, 'r') as file:
        content = file.read()
    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the PDF
pdf.output("output.pdf")