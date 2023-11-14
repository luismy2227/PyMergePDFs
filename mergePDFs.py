import os
from PyPDF2 import PdfWriter


def mergePDFs(*pdfs, **kwargs):
    '''
    Merge PDF files into a single PDF file
    :param pdfs: List of PDF files to merge (args)
    :param kwargs: Optional arguments (output file)
    '''
    output = kwargs.get('output', os.path.join(os.getcwd(), 'output.pdf'))
    merger = PdfWriter()

    for pdf in pdfs:
        merger.append(pdf)
    merger.write(output)
    merger.close()


if __name__ == '__main__':
    input_folder = "./public"
    output_file = "./public/merged.pdf"
    # Get a list of PDF files in the input folder
    pdf_files = ['./public/' +
                 f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    print(pdf_files)

    # Sort the PDF files to merge them in order
    pdf_files.sort()
    mergePDFs(*pdf_files, output=output_file)
