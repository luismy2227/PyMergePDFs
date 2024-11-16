# PyMergePDFs
A usefull library with pdf related functions

## Functions

- mergePDFs.py: Receives a list of pdf routes and a destination location for the resulted merged file
- splitPDF.py: Receives the route of a pdf file and a destination location for the resulted splitted files

## Scripts

- `init.ps1`: It create an env, install required packages (use if you're in a windows)
- `init.sh`: It does the same as the previous one, but if you're from unix.

## Pack

```sh
pip install pyinstaller
pyinstaller --onefile --windowed --icon="public/pdf.ico" "src/pdfTool.py"
```