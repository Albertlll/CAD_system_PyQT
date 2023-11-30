import typing
from PyQt5.QtWidgets import (
    QApplication, QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog, QLabel, QListWidget, QGraphicsPixmapItem,
    QListWidgetItem, QGraphicsItem, QLineEdit, QDoubleSpinBox, QSpinBox
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor, QDropEvent, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QPointF, QEvent, QRect
from PyQt5 import QtCore, QtGui 
from PyQt5 import uic
from py_ui.list_widget import Ui_MainWindow
from constants import *
from wire import Wire


class Element(QGraphicsPixmapItem):
    def __init__(self, main_wind):
        super(QGraphicsPixmapItem, self).__init__()
        self.setFlag(QGraphicsPixmapItem.GraphicsItemFlag.ItemSendsScenePositionChanges)
        self.main_wind = main_wind
        self.type_elem_ind = main_wind.find() 
        self.height = 0.2

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
        self.pars_pos()
        return super().mouseMoveEvent(event)

    def pars_inf(self):
        self.main_wind.object_name.setText(NAMES[self.type_elem_ind])
        self.main_wind.item_img.setPixmap(QPixmap(NORMAL_ICON_PATHS[self.type_elem_ind]))
        self.main_wind.obj_height.setValue(self.height)

        self.pars_pos()
    
    def pars_pos(self):
        self.main_wind.obj_x.setValue(int(self.scenePos().x()))
        self.main_wind.obj_y.setValue(int(self.scenePos().y()))
    
    def mousePressEvent(self, event):

        for item in self.main_wind.view.items():
            if item.type() == 6 or item.type() == 10:
                continue
            if item != self and item.type() == 7:
                path = NORMAL_ICON_PATHS[item.type_elem_ind]
            else:
                path = SELECTED_ICON_PATHS[item.type_elem_ind]
                self.main_wind.selected = item
                self.pars_inf()
            pixmap = QPixmap(path)
            item.setPixmap(pixmap)
            

        if self.main_wind.first_waiting:
            print("буя")
            self.main_wind.first_waiting = False
            self.main_wind.wire = Wire(self.main_wind.scene)
            
            self.main_wind.wire.add_start_item(self)
            # scene_item_pos = self.scenePos().toPoint()
            scene_item_pos = self.get_center_point()
            #self.main_wind.wire.add_point(scene_item_pos)
            return
        
        if not self.main_wind.first_waiting and self.main_wind.wire_painting and self != self.main_wind.wire.start_elem:
            print("чичивап")

            scene_item_pos = self.get_center_point()
            
            self.main_wind.draw_fast_line(QPoint(int(self.main_wind.get_last_point().x()),
                                                 int(self.main_wind.get_last_point().y())),
                                                 scene_item_pos)

            self.main_wind.wire.add_point(scene_item_pos)
            self.main_wind.wire_painting = False
            self.main_wind.wire.add_end_item(self)
            self.main_wind.wires.append(self.main_wind.wire)
            self.main_wind.wire = None

    def get_center_point(self):
        scene_item_pos = self.scenePos().toPoint()
        item_rect = self.pixmap()
        item_rect: QRect
        scene_item_pos : QPoint
        print(item_rect.height())
        print(item_rect.width())
        return QPoint(scene_item_pos.x() + int(item_rect.height() * ICON_SCALE // 2),
                       scene_item_pos.y() + int(item_rect.width() * ICON_SCALE // 2))