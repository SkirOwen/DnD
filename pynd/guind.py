from pynd.imports import *


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        left = QFrame(self)
        left.setFrameShape(QFrame.StyledPanel)

        right = QFrame(self)
        right.setFrameShape(QFrame.StyledPanel)

        middle = QFrame(self)
        middle.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(left)
        splitter1.addWidget(middle)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(right)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QSplitter')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()