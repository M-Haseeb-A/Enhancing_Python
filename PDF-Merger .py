from pypdf import PdfWriter

merger = PdfWriter()
files = [
    "Enter your PDF's here you want to merge"
]
for file in files:
    merger.append(file)

name  = input("Enter the name you want to give to new PDF :")

merger.write(name)
merger.close()