from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor


class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor("#701f28"))
        pen = QPen(QColor("#ffd966"))
        painter.setPen(pen)
        center = self.rect().center()
        radius = min(self.rect().width(), self.rect().height())//2 - 10
        painter.drawEllipse(center, radius, radius)

