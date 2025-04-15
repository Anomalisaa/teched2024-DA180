import os
import re
from PyPDF2 import PdfMerger

# Pfad zum Ordner mit den 'ex*'-Unterordnern
basis_pfad = "./exercises"

# Finde alle 'ex*'-Ordner
exercise_ordner = sorted(
    [d for d in os.listdir(basis_pfad) if os.path.isdir(os.path.join(basis_pfad, d)) and re.match(r"ex\d{2}", d)],
    key=lambda x: int(re.findall(r'\d+', x)[0])
)

pdf_merger = PdfMerger()

for ordner in exercise_ordner:
    ordner_pfad = os.path.join(basis_pfad, ordner)
    # Alle PDFs im Ordner finden und alphabetisch sortieren
    pdfs = sorted(f for f in os.listdir(ordner_pfad) if f.endswith(".pdf"))
    for pdf in pdfs:
        pdf_pfad = os.path.join(ordner_pfad, pdf)
        print(f"Füge hinzu: {pdf_pfad}")
        pdf_merger.append(pdf_pfad)

# Zusammengeführte PDF speichern
ausgabe_pfad = os.path.join(basis_pfad, "alle_exercises_zusammen.pdf")
pdf_merger.write(ausgabe_pfad)
pdf_merger.close()

print(f"\n Ergebnis: {ausgabe_pfad}")
