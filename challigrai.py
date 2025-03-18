import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, 
                           QToolBar, QFileDialog, QComboBox, QMessageBox)
from PyQt6.QtCore import Qt
from dashscope import Generation

API_KEY = "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"

class ChalligraiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Challigrai")
        self.setGeometry(100, 100, 800, 600)
        
        # Create text editor
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # Create toolbar
        self.create_toolbar()
        
        # Initialize Qwen API
        Generation.api_key = API_KEY

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.setMovable(True)
        
        # File menu
        file_menu = toolbar.addMenu("File")
        
        # New document action
        new_action = file_menu.addAction("New")
        new_action.triggered.connect(self.new_document)
        
        # Open file action
        open_action = file_menu.addAction("Open")
        open_action.triggered.connect(self.open_file)
        
        # Save file action
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_file)
        
        # Close action
        close_action = file_menu.addAction("Close")
        close_action.triggered.connect(self.close)
        
        # Add tone selector
        self.tone_selector = QComboBox()
        self.tone_selector.addItems([
            "Inspirational",
            "Professional",
            "Casual",
            "Poetic",
            "Technical",
            "Humorous"
        ])
        self.tone_selector.currentTextChanged.connect(self.update_tone)
        toolbar.addWidget(self.tone_selector)

    def new_document(self):
        self.text_edit.clear()
        self.setWindowTitle("Challigrai - New Document")

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Text File", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    self.text_edit.setText(file.read())
                self.setWindowTitle(f"Challigrai - {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Text File", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
                self.setWindowTitle(f"Challigrai - {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")

    def update_tone(self, tone):
        # Here we would implement the AI integration with Qwen
        # This is a placeholder for the actual implementation
        current_text = self.text_edit.toPlainText()
        if current_text:
            try:
                response = Generation.call(
                    model='qwen-max',
                    prompt=f"Continue the following text in a {tone} tone:\n{current_text}",
                    max_tokens=100
                )
                if response.status_code == 200:
                    self.text_edit.append("\n" + response.output.text)
                else:
                    QMessageBox.warning(self, "Warning", "Could not generate continuation")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"AI generation error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = ChalligraiApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 