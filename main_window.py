from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QWidget, QHBoxLayout
from circle_widget import CircleWidget  # Import the CircleWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mr. Lockdall's Random Wheel")
        self.setGeometry(1000, 10, 800, 500)  # Adjusted size to fit both widgets
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Enter items here...")
        self.circle_widget = CircleWidget(self)
        self.setup_layout()

    def setup_layout(self):
        self.text_edit.setMaximumWidth(200)  # Set to your desired width

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()
        hbox.addWidget(self.circle_widget)
        hbox.addWidget(self.text_edit)
        central_widget.setLayout(hbox)
