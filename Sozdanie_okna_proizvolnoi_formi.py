from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
window.setWindowTitle("Создание окна произвольной формы")
window.resize(300, 100)
pixmap = QtGui.QPixmap("mask.png")
pal = window.palette()
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
             QtGui.QBrush(pixmap))
pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
             QtGui.QBrush(pixmap))
window.setPalette(pal)
window.setMask(pixmap.mask())
button = QtWidgets.QPushButton("Закрыть окно")
button.setFixedSize(150, 30)
button.move(75, 135)
button.clicked.connect(QtWidgets.qApp.quit)
window.show()
sys.exit(app.exec_())
