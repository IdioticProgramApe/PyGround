import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me")
        
        self.setFixedSize(QSize(400, 300))
        
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
