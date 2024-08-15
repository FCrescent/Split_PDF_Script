#Ce petit script permet de split un fichier PDF en 2
#A refactoriser pour le rendre plus flexible, c-à-d :
#- lui faire demander à l'utilisateur le nom du fichier à split, 
#- lui demander les noms des fichiers finaux et 
# la façon de le split (nbr de pages)

import PyPDF2

input_pdf = 'NameOfPdfToSplit.pdf'

with open(input_pdf, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # Create a new PDF writer for the first 3 pages
    pdf_writer_first = PyPDF2.PdfWriter()
    for page_num in range(3):
        pdf_writer_first.add_page(pdf_reader.pages[page_num])

    # Write the first part to a new file
    with open('NameOfFirstPartFile.pdf', 'wb') as first_part_file:
        pdf_writer_first.write(first_part_file)

    # Create a new PDF writer for the last 2 pages
    pdf_writer_last = PyPDF2.PdfWriter()
    for page_num in range(3, len(pdf_reader.pages)):
        pdf_writer_last.add_page(pdf_reader.pages[page_num])

    # Write the second part to a new file
    with open('NameOfSecondPartFile.pdf', 'wb') as last_part_file:
        pdf_writer_last.write(last_part_file)