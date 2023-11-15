from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog, QLabel, QListWidget,
    QListWidgetItem, QGraphicsItem, QLineEdit
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor, QDropEvent, QMouseEvent
from PyQt5.QtCore import Qt, QPointF, QEvent
from PyQt5 import QtGui 
from PyQt5 import uic
from py_ui.list_widget import Ui_MainWindow
from constants import *
from elements import QGraphicsPixmapItem




class Wire():
    def __init__(self):
        self.start_elem = None
        self.end_elem = None
        self.points = []
    
    def add_start_item(self, elem):
        self.start_elem = elem

    def add_end_item(self, elem):
        self.end_elem = elem
    
    def add_point(self, point):
        self.points.append(point)