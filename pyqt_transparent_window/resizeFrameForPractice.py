from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QColor, QPen, QCursor
from PyQt5.QtWidgets import QWidget


class ResizeFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

        self.setMouseTracking(True)

    def paintEvent(self, e):
        painter = QPainter(self)
        pen = QPen(QColor(Qt.blue), 5)
        painter.setPen(pen)
        painter.drawRect(self.rect())
        return super().paintEvent(e)

    def adjustResizeFrame(self, pos, cur_shape):
        x = pos.x()
        y = pos.y()
        self.resize(QSize(x, y))
        resize_frame_min_width = 30
        resize_frame_min_height = 30
        if cur_shape == Qt.SizeHorCursor:
            if x < resize_frame_min_width:
                # left to right
                if x > 0:
                    right_frame = self.geometry()

                    geo = self.geometry()
                    geo.moveLeft(self.mapToGlobal(pos).x())
                    geo = geo.intersected(right_frame)
                    self.setGeometry(geo)

                # left to left
                else:
                    right_frame = self.geometry()

                    geo = self.geometry()
                    geo.moveLeft(self.mapToGlobal(pos).x())
                    geo = geo.united(right_frame)

                    self.setGeometry(geo)
            else:
                resize_frame_min_height = self.height()
                self.setMinimumSize(resize_frame_min_width, resize_frame_min_height)
        elif cur_shape == Qt.SizeVerCursor:
            if y < resize_frame_min_height:
                top_frame = self.geometry()

                geo = self.geometry()
                geo.moveTop(self.mapToGlobal(pos).y())
                geo = geo.united(top_frame)

                self.setGeometry(geo)
            else:
                resize_frame_min_width = self.width()
                self.setMinimumSize(resize_frame_min_width, resize_frame_min_height)
        else:
            self.setMinimumSize(resize_frame_min_width, resize_frame_min_height)

