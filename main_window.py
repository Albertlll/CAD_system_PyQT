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

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/list_widget.ui', self)

        self.graphicsView: QGraphicsView
        self.list: QListWidget

        self.wires_painting = False
        self.wires = []
        self.wire = None

        self.list.itemClicked.connect(self.add_elem_to_center)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.graphicsView.rect().width(), self.graphicsView.rect().height())
        self.graphicsView.setScene(self.scene)

        #self.graphicsView.mouseMoveEvent = self.mouse_move
        #self.list.itemClicked.connect(self.clicked)

    # def mouse_move(self, event):
    #     if self.wires_painting and self.wire:
    #         last_x = self.wire.points[-1].x()
    #         last_y = self.wire.points[-1].y()

    #         self.graphicsView.scene().addLine(last_x, last_y, event.pos().x(), event.pos().y())
    def add_items_to_list(self):
        pass
        # self.graphicsView: QGraphicsView
            
    def find(self):
        index = self.list.currentRow()
        return index
    
    def get_url_to_list(self):
        return NORMAL_ICON_PATHS.get(self.find())
    
    def get_url_to_field(self, is_selected : bool):
        ind = self.find()
        if is_selected:
            return SELECTED_ICON_PATHS[ind]
        return NORMAL_ICON_PATHS[ind]
    

    def clear_outline(self):
        for item in self.main_wind.graphicsView.items():
            if item != self and item.type() == 7:
                path = NORMAL_ICON_PATHS[item.type_elem_ind]
            else:
                path = SELECTED_ICON_PATHS[item.type_elem_ind]
            pixmap = QPixmap(path)
            item.setPixmap(pixmap)



    def add_elem_to_center(self):
        self.list: QListWidget

        if self.find() == 2:
            #self.wires_painting = True
            pass
        else:
            pixmap = QPixmap(self.get_url_to_field(False))
            pic = QGraphicsPixmapItem(self)
            pic.setPixmap(pixmap)
            pic.setScale(ICON_SCALE)

            pic.setPos(self.graphicsView.width() // 2, self.graphicsView.height() // 2)
            pic.setFlags(QGraphicsItem.ItemIsMovable)
            self.graphicsView.scene().addItem(pic)

    def set_properties_view(self, item):
        #Та самая функция
        pass