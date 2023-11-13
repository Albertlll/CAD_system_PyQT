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
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.scene.setSceneRect(0, 0, 800, 600)
        self.view.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(self.view)

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

class WireLengthCounter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Electrical Plan')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.drawing_area = DrawingArea()

        # Create 4 tool buttons
        self.tool_button1 = QToolButton()
        self.tool_button1.setIcon(QIcon('icon1.png'))  # Replace 'icon1.png' with your icon file
        self.tool_button2 = QToolButton()
        self.tool_button2.setIcon(QIcon('icon2.png'))  # Replace 'icon2.png' with your icon file
        self.tool_button3 = QToolButton()
        self.tool_button3.setIcon(QIcon('icon3.png'))  # Replace 'icon3.png' with your icon file
        self.tool_button4 = QToolButton()
        self.tool_button4.setIcon(QIcon('icon4.png'))  # Replace 'icon4.png' with your icon file

        self.statusBar().showMessage('Cursor Coordinates: X=0, Y=0')
        self.drawing_area.view.mouseMoveEvent = self.show_coordinates  # Overriding mouseMoveEvent

        toolbar = self.addToolBar("Tools")
        toolbar.addWidget(self.tool_button1)
        toolbar.addWidget(self.tool_button2)
        toolbar.addWidget(self.tool_button3)
        toolbar.addWidget(self.tool_button4)

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        new_action = QAction('New', self)
        new_action.triggered.connect(self.clear_drawing)
        file_menu.addAction(new_action)

        pen_color_action = QAction('Pen Color', self)
        pen_color_action.triggered.connect(self.drawing_area.set_pen_color)
        file_menu.addAction(pen_color_action)

        self.save_button = QAction(QIcon('save_icon.png'), 'Save', self)  # Replace 'save_icon.png' with your save icon
        self.save_button.triggered.connect(self.save_drawing)
        file_menu.addAction(self.save_button)

        layout = QVBoxLayout()
        layout.addWidget(self.drawing_area)
        self.centralWidget().setLayout(layout)

    def save_drawing(self):
        image = QPixmap(self.drawing_area.size())
        self.drawing_area.render(image)
        image.save('electrical_plan.png')
        print("Drawing saved as electrical_plan.png")

    def show_coordinates(self, event):
        cursor_pos = self.drawing_area.view.mapToScene(event.pos())
        self.statusBar().showMessage(f'Cursor Coordinates: X={cursor_pos.x()}, Y={cursor_pos.y()}')    

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)", options=options)
        if file_name:
            print("Opened file:", file_name)  # Here, you can process the opened file as needed
            pixmap = QPixmap(file_name)
            self.drawing_area.scene.clear()
            self.drawing_area.scene.addPixmap(pixmap)

    def clear_drawing(self):
        self.drawing_area.scene.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WireLengthCounter()
    ex.show()
    sys.exit(app.exec_())
