from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.btnMin = QtWidgets.QPushButton("Свернуть")
        self.btnMax = QtWidgets.QPushButton("Развернуть")
        self.btnFull = QtWidgets.QPushButton("Полный экран")
        self.btnNormal = QtWidgets.QPushButton("Нормальный размер")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.btnMin)
        self.vbox.addWidget(self.btnMax)
        self.vbox.addWidget(self.btnFull)
        self.vbox.addWidget(self.btnNormal)
        self.setLayout(self.vbox)
        self.btnMin.clicked.connect(self.on_min)
        self.btnMax.clicked.connect(self.on_max)
        self.btnFull.clicked.connect(self.on_full)
        self.btnNormal.clicked.connect(self.on_normal)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()

    def on_full(self):
        self.showFullScreen()

    def on_normal(self):
        self.showNormal()


if __name__ == '__main__':
    import sys
    # Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Разворачивание и сворачивание окна")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())
