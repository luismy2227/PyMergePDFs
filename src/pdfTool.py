from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QLabel,
)
from PyQt5.QtGui import QIcon
import sys
import os
from splitPDF import splitPDF
from mergePDFs import mergePDFs


class PDFTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        icon_path = os.path.join(os.path.dirname(__file__), "..", "public", "pdf.ico")
        self.setWindowIcon(QIcon(icon_path))

    def initUI(self):
        self.setWindowTitle("PDF Merger & Splitter")
        self.setGeometry(300, 300, 500, 250)

        layout = QVBoxLayout()

        # Add buttons
        self.mergeButton = QPushButton("Merge PDFs", self)
        self.mergeButton.clicked.connect(self.mergePDFs)
        layout.addWidget(self.mergeButton)

        self.splitButton = QPushButton("Split PDF", self)
        self.splitButton.clicked.connect(self.splitPDF)
        layout.addWidget(self.splitButton)

        self.statusLabel = QLabel("", self)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

    def show_message(self, title, message, is_error=False):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical if is_error else QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def mergePDFs(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select PDF files to merge", "", "PDF Files (*.pdf)"
        )
        if not files:
            self.show_message(
                "No Files Selected", "Please select PDF files to merge.", True
            )
            return

        output_file, _ = QFileDialog.getSaveFileName(
            self, "Save Merged PDF As", "", "PDF Files (*.pdf)"
        )
        if not output_file:
            self.show_message(
                "No Output File", "Please specify an output file for merging.", True
            )
            return

        if mergePDFs(*files, output=output_file):
            self.show_message("Success", f"Merged PDF saved at {output_file}")
        else:
            self.show_message("Error", "Failed to merge PDFs.", True)

    def splitPDF(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Select a PDF file to split", "", "PDF Files (*.pdf)"
        )
        if not file:
            self.show_message(
                "No File Selected", "Please select a PDF file to split.", True
            )
            return

        output_folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if not output_folder:
            self.show_message(
                "No Output Folder",
                "Please specify an output folder for splitting.",
                True,
            )
            return

        if splitPDF(file, output_folder):
            self.show_message(
                "Success", f"PDF split into pages saved at {output_folder}"
            )
        else:
            self.show_message("Error", "Failed to split PDF.", True)


def main():
    app = QApplication(sys.argv)
    tool = PDFTool()
    tool.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
