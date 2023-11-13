from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog, QLabel, QListWidget, QGraphicsPixmapItem,
    QListWidgetItem
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor, QDropEvent
from PyQt5.QtCore import Qt, QPointF
from PyQt5 import QtGui 
from PyQt5 import uic
from py_ui.list_widget import Ui_MainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/list_widget.ui', self)

        self.graphicsView: QGraphicsView
        self.list: QListWidget

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 400, 400)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.mousePressEvent = self.mouse_click_event

        #self.list.itemClicked.connect(self.clicked)

    def add_items_to_list(self):
        pass
        # self.graphicsView: QGraphicsView

    def mouse_click_event(self, event):
        self.list: QListWidget
        cur_i = self.list.currentItem().icon()
        scale = 80
        cur_i = cur_i.pixmap(scale, scale)
        pic = QGraphicsPixmapItem()
        pic.setPixmap(cur_i)
        pos = event.pos()
        pic.setOffset(pos.x() - scale / 2,
                       pos.y() - scale / 2)
        self.graphicsView.scene().addItem(pic)

