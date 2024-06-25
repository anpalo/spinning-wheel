from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QAction, QTextEdit, QPushButton, QVBoxLayout, QMenu
from circle_widget import CircleWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mr. Lockdall's Random Wheel")
        self.setGeometry(100, 100, 800, 500)  # Adjusted size for simplicity
        self.text_edit = QTextEdit()
        self.text_edit.setMaximumWidth(300)  # Set maximum width here

        self.circle_widget = CircleWidget()  # Assuming CircleWidget is correctly implemented

        self.setup_layout()
        self.create_menu_bar()
        self.setup_buttons()

    def setup_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox_main = QHBoxLayout(central_widget)
        vbox_side = QVBoxLayout()

        vbox_side.addWidget(self.text_edit)
        vbox_side.addWidget(self.setup_buttons())

        hbox_main.addWidget(self.circle_widget)
        hbox_main.addLayout(vbox_side)

    def setup_buttons(self):
        button_widget = QWidget()
        hbox_buttons = QHBoxLayout(button_widget)

        save_list_button = QPushButton("Save List")
        get_old_list_button = QPushButton("Get Old List")
        clear_all_button = QPushButton("Clear All")

        hbox_buttons.addWidget(save_list_button)
        hbox_buttons.addWidget(get_old_list_button)
        hbox_buttons.addWidget(clear_all_button)

        return button_widget

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        open_action = QAction("Open", self)
        file_menu.addAction(open_action)

        save_as_action = QAction("Save As", self)
        file_menu.addAction(save_as_action)

        insert_menu = menu_bar.addMenu("Insert")
        add_wheel_action = QAction("Add New Wheel", self)
        insert_menu.addAction(add_wheel_action)

        style_menu = menu_bar.addMenu("Style")
        color_menu = QMenu("Color Scheme", self)
        fonts_menu = QMenu("Fonts", self)
        style_menu.addMenu(color_menu)
        style_menu.addMenu(fonts_menu)


