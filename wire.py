from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog, QLabel, QListWidget,
    QListWidgetItem, QGraphicsItem, QLineEdit, QGraphicsLineItem, QGraphicsItemGroup
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor, QDropEvent, QMouseEvent
from PyQt5.QtCore import Qt, QPointF, QEvent
from PyQt5 import QtGui 
from PyQt5 import uic
from py_ui.list_widget import Ui_MainWindow
from constants import *
from elements import QGraphicsPixmapItem


class Wire():
    def __init__(self, scene: QGraphicsScene):
        self.start_elem = None
        self.end_elem = None
        self.points = []
        self.lines = []
        self.elems = []

        self.start_wire_item_index = 0
        self.end_wire_item_index = 0
        #scene.addItem(self.group)
    
    def add_start_item(self, elem):
        self.start_elem = elem
        self.elems.append(elem)

    def add_end_item(self, elem):
        self.end_elem = elem
        self.elems.append(elem)

    def add_point(self, point):
        self.points.append(point)