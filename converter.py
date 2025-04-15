from pdf2docx import Converter
import os

# Pfad zu Files:
pdf_file = os.path.join("exercises", "alle_exercises_zusammen.pdf")
docx_file = os.path.join("exercises", "WS_Handout.docx")

# Konvertierung
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

print(f"Konvertiert: {docx_file}")
