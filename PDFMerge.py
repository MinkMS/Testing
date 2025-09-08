from PyPDF2 import PdfMerger

pdf_files = [
        r"C:\Users\hoang\Downloads\labwork1-webapp.pdf",
        r"C:\Users\hoang\Downloads\labwork2-webapp.pdf",
        r"C:\Users\hoang\Downloads\labwork3-webapp.pdf",
        ]

merger = PdfMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write("Labwork.pdf")
merger.close()

print("PDFs merged successfully!")