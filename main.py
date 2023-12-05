import sys
from main_window import MainForm
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt
import os


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)




if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)



if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    
if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
