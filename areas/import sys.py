import sys
from PyQt5.QtWidgets import (QApplication,
QLabel,
QWidget, QMainWindow)

class lol(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.initUI()
        self.setMouseTracking (True)
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 200) 
        self.setWindowTitle('Mouse Tracker') 
        self.label = QLabel(self) 
        self.label.resize (200, 40) 
        self.show()

    def mouseMoveEvent(self, event):
        print(event.pos())


app = QApplication(sys.argv)
ex = lol()
sys.exit(app.exec_())