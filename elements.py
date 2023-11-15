from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog, QLabel, QListWidget, QGraphicsPixmapItem,
    QListWidgetItem, QGraphicsItem, QLineEdit
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor, QDropEvent, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QEvent
from PyQt5 import QtGui 
from PyQt5 import uic
from py_ui.list_widget import Ui_MainWindow
from constants import *
from wire import Wire

class QGraphicsPixmapItem(QGraphicsPixmapItem):
    def __init__(self, main_wind):
        super(QGraphicsPixmapItem, self).__init__()
        self.main_wind = main_wind
        self.type_elem_ind = main_wind.find() 
    
    def mousePressEvent(self, event):
        if not self.main_wind.wires_painting:
            for item in self.main_wind.graphicsView.items():
                if item != self and item.type() == 7:
                    path = NORMAL_ICON_PATHS[item.type_elem_ind]
                else:
                    path = SELECTED_ICON_PATHS[item.type_elem_ind]
                pixmap = QPixmap(path)
                item.setPixmap(pixmap)
            return
        
        self.main_wind.wire = Wire()
        self.main_wind.wire.add_start_item(self)
        self.main_wind.wire.add_point(QPoint(self.pixmap().width // 2, self.pixmap().height // 2))

        