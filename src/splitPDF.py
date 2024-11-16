import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def splitPDF(pdf_file, output_folder=None):
  '''
  Split a PDF file into multiple PDF files
  :param pdf_file: PDF file to split
  :param output_folder: Folder to save the split PDF files (optional)
  '''
  pdf = PdfFileReader(pdf_file)
  if output_folder is None:
    output_folder = os.path.dirname(pdf_file)
  for page in range(pdf.getNumPages()):
    writer = PdfFileWriter()
    writer.addPage(pdf.getPage(page))
    output = os.path.join(output_folder, f'page_{page + 1}.pdf')
    with open(output, 'wb') as output_pdf:
      writer.write(output_pdf)
      

if __name__ == '__main__':
  input_file = "../public/output/merged.pdf"
  output_folder = "../public/split"
  splitPDF(input_file, output_folder)