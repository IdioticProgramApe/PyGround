import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.is_clicked)
        button.clicked.connect(self.is_toggled)
        
        self.setFixedSize(QSize(400, 300))
        
        self.setCentralWidget(button)
        
    def is_clicked(self):
        print("clicked")
        
    def is_toggled(self, checked: bool):
        print(f"Checked?: {checked}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
