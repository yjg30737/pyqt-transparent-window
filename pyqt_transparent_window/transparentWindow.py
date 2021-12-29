from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqt_resize_frame.resizeFrame import ResizeFrame


class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__n_margin = 10
        self.__pressed = False
        self.__initUi()

    def __initUi(self):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

        self.__cursor = QCursor()

        self.setMouseTracking(True)

        self.setFixedSize(200, 200)

        self.__resizeFrame = ResizeFrame()
        self.__resizeFrame.deactivated.connect(self.__resizeStop)

    def paintEvent(self, e):
        painter = QPainter(self)
        pen = QPen(QColor(Qt.white), self.__n_margin // 2)
        painter.setPen(pen)
        painter.drawRect(self.rect())
        return super().paintEvent(e)

    def setCursorShapeByPosition(self, x, y, width, height):
        if self.__pressed:
            pass
        else:
            # Top left
            if x < self.__n_margin and y < self.__n_margin:
                self.__cursor.setShape(Qt.SizeFDiagCursor)
                self.setCursor(self.__cursor)

            # Top right
            elif x > width-self.__n_margin and y < self.__n_margin:
                self.__cursor.setShape(Qt.SizeBDiagCursor)
                self.setCursor(self.__cursor)

            # Bottom left
            elif x < self.__n_margin and y > height-self.__n_margin:
                self.__cursor.setShape(Qt.SizeBDiagCursor)
                self.setCursor(self.__cursor)

            # Bottom right
            elif x > width-self.__n_margin and y > height-self.__n_margin:
                self.__cursor.setShape(Qt.SizeFDiagCursor)
                self.setCursor(self.__cursor)

            # Horizontal
            elif y < height and (x > width-self.__n_margin or x < self.__n_margin):
                self.__cursor.setShape(Qt.SizeHorCursor)
                self.setCursor(self.__cursor)

            # Vertical
            elif x < width and (y > height-self.__n_margin or y < self.__n_margin):
                self.__cursor.setShape(Qt.SizeVerCursor)
                self.setCursor(self.__cursor)

    def mouseMoveEvent(self, e):
        p = e.pos()

        x = p.x()
        y = p.y()
        width = self.width()
        height = self.height()

        self.setCursorShapeByPosition(x, y, width, height)
        self.__adjustResizeFrame(pos=p, cur_shape=self.cursor().shape())

        return super().mouseMoveEvent(e)

    def __initResizeFrame(self):
        self.__resizeFrame.setMinimumSize(self.size())
        self.__showResizeFrame()

    def __showResizeFrame(self):
        f = self.__resizeFrame.isVisible()
        self.__resizeFrame.setVisible(not f)

    def __adjustResizeFrame(self, pos, cur_shape):
        self.__resizeFrame.adjustResizeFrame(pos, cur_shape)

    def __setWindowAsResizeFrame(self):
        self.setFixedSize(self.__resizeFrame.size())
        self.__showResizeFrame()

    def enterEvent(self, e):
        p = e.pos()
        x = p.x()
        y = p.y()

        width = self.width()
        height = self.height()

        self.setCursorShapeByPosition(x, y, width, height)

        return super().enterEvent(e)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__resizeStart()
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__resizeEnd()
        return super().mouseReleaseEvent(e)

    def __resizeStart(self):
        self.__pressed = True
        self.__initResizeFrame()

    def __resizeEnd(self):
        self.__pressed = False
        self.__setWindowAsResizeFrame()

    def __resizeStop(self):
        self.__pressed = False
        self.__showResizeFrame()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    capturer = TransparentWindow()
    capturer.show()
    app.exec_()