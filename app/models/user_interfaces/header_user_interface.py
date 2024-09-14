from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class HeaderUserInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.layout = QVBoxLayout()


    def init_ui(self):
        self.label.setStyleSheet("background-color: lightgreen; font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.label)
        return self.layout