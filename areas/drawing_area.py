import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QAction, QMenu, QGraphicsScene, QGraphicsView, QToolButton, QFileDialog, QColorDialog
)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QIcon, QImage, QColor
from PyQt5.QtCore import Qt, QPointF


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        
        self.drawing = False
        self.last_point = QPointF()
        self.pen = QPen()
        self.pen.setWidth(2)
        self.pen.setColor(Qt.black)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.drawing:
                self.drawing = True
                self.last_point = event.pos()
            else:
                end = event.pos()
                self.scene.addLine(self.last_point.x(), self.last_point.y(), end.x(), end.y(), self.pen)
                self.last_point = end

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drawing:
            # Optionally, enable real-time line drawing by adding the line here.
            pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def set_pen_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen.setColor(color)