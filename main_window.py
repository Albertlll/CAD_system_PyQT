import typing
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog, QLabel, QListWidget,
    QListWidgetItem, QGraphicsItem, QLineEdit, QGraphicsLineItem, QGraphicsSceneMouseEvent, QGraphicsSceneWheelEvent
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor, QDropEvent, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QEvent, QLine, QLineF, QRectF, QPointF
from PyQt5 import QtGui 
from PyQt5 import uic
from py_ui.list_widget import Ui_MainWindow
from constants import *
from elements import QGraphicsPixmapItem
from wire import Wire
class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/alan_wires.ui', self)

        self.view: QGraphicsView
        self.list: QListWidget

        self.first_waiting = False
        self.wire_painting = False

        self.wires = []
        self.wire = None
        self.wire : Wire

        self.list.itemClicked.connect(self.add_elem_to_center)

        # self.scene = QGraphicsScene()
        # self.scene.setSceneRect(0, 0, self.graphicsView.rect().height(), self.graphicsView.rect().width())
        # self.graphicsView.setScene(self.scene)

        self.create_view()
        self.pen = QPen()
        self.pen.setWidth(5)
        self.pen.setColor(Qt.black)


        self.count = 0

    def create_view(self):
        self.scene = QGraphicsScene(0, 0, 1000, 1000, self.view)
        self.scene.mouseDoubleClickEvent = self.SceneMouseDoubleClickEvent
        # self.scene.dragMoveEvent = self.ScenedragMoveEvent
        self.view.setScene(self.scene)
        
        self.view.show()
        print(self.scene.sceneRect())
        # self.view.setStyleSheet("""
        # background-color: rgba(255,255,255);
        # border-radius: 30px;

        # """)

        
        # self.view.setGeometry(130, 160, 500, 350)

    # def ScenedragMoveEvent(self, a0=QGraphicsSceneMouseEvent):
    #     print(a0.scenePos())


    def draw_line(self, first_pos, second_pos):

        first_pos_modif= self.modification_coords(second_pos, first_pos)
        self.wire.add_point(first_pos_modif)

        line = QGraphicsLineItem(QLineF(first_pos_modif, second_pos))

        line.setPen(self.pen)
        line.setZValue(0)
        self.scene.addItem(line)
        self.wire.lines.append(line)
        self.wire.elems.append(line)

    def modification_coords(self, first: QPoint, second: QPoint):
            p = QPointF()
            dx = abs(first.x()-second.x())
            dy = abs(first.y() - second.y())
            if(first.x()!=second.x() or first.y()!=second.y()):
                if (dx > dy):
                    p.setX(int(second.x()))
                    p.setY(int(first.y()))
                else:
                    p.setX(int(first.x()))
                    p.setY(int(second.y()))
            else:
                p.setX(int(second.x()))
                p.setY(int(second.y()))
            return p
    
    def get_last_point(self):
        return self.wire.points[-1]
    
    def SceneMouseDoubleClickEvent(self, a0: QGraphicsSceneMouseEvent):
        pos = a0.scenePos()
        print(pos)
        print(self.wire)
        last_point = self.get_last_point()
        last_point : QPoint
        #now_point = self.wire_coords(pos.x(), pos.y(), last_point.x(), last_point.y())
        now_point = pos

        # last_point.setX(last_point.x() - self.graphicsView.x())
        # last_point.setY(last_point.y() - self.graphicsView.y())

        now_point.setX(now_point.x())
        now_point.setY(now_point.y())

        self.draw_line(now_point, last_point)

        # Пока убирать другие способы запоминать куски провода не буду, но использую group
        # Отмена, используется проход по всем элементам


        for item in self.view.items():
            print(item.type())


    # def mouse_checher(self, event):
    #     self.count += 1
    #     if self.wires_painting and self.wire:
    #          last_x = self.wire.points[-1].x()
    #          last_y = self.wire.points[-1].y()

    #          self.graphicsView.scene().addLine(last_x, last_y, event.pos().x(), event.pos().y())
    
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
            self.first_waiting = True
            self.wire_painting = True
            # Тут при нажатии на палец

        else:
            if self.wire_painting:
                print('xbc')
                self.wire_painting = False
                for item in self.view.items():
                    if item in self.wire.lines:
                        self.scene.removeItem(item)

                self.wire = None

            pixmap = QPixmap(self.get_url_to_field(False))
            pic = QGraphicsPixmapItem(self)
            pic.setPixmap(pixmap)
            pic.setScale(ICON_SCALE)
            pic.setZValue(1)
            pic.setPos(pic.get_center_point())
            pic.setPos(self.scene.width() // 2, self.scene.height() // 2)
            pic.setFlags(QGraphicsItem.ItemIsMovable)
            self.scene.addItem(pic)


    # def wire_coords(self, x, y, x1, y1):
    #     if x == x1:
    #         return (x, y)
    #     elif y == y1:
    #         return (x, y)
    #     else:
    #         k = (y - y1) / (x - x1)
    #         b = y - k * x
    #         if abs(k) > 1:
    #             y_new = k * x1 + b
    #             return QPoint(x, round (y_new) )
    #         else:
    #             x_new = (y1 - b) / k
    #             return QPoint(round (x_new) , y)