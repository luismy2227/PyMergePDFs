import os
from PyPDF2 import PdfReader, PdfWriter


def splitPDF(pdf_file, output_folder=None):
    """
    Split a PDF file into multiple PDF files
    :param pdf_file: PDF file to split
    :param output_folder: Folder to save the split PDF files (optional)
    :return: True if successful, False otherwise
    """

    try:
        pdf = PdfReader(pdf_file)
        pdf_file_name = os.path.basename(pdf_file)
        pdf_file_name = os.path.splitext(pdf_file_name)[0]
        if output_folder is None:
            output_folder = os.path.dirname(pdf_file)
        for page in range(len(pdf.pages)):
            writer = PdfWriter()
            writer.add_page(pdf.pages[page])
            output = os.path.join(output_folder, f"{pdf_file_name}_{page + 1}.pdf")
            with open(output, "wb") as output_pdf:
                writer.write(output_pdf)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    input_file = "../public/output/merged.pdf"
    output_folder = "../public/split"
    splitPDF(input_file, output_folder)
