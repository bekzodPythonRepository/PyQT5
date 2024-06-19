from PyQt5 import QtCore


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
r.moveTopLeft(QtCore.QPoint(0, 0))
print(r) # PyQt5.QtCore.QRect(0, 0, 400, 300)
r.moveBottomRight(QtCore.QPoint(599, 499))
print(r) # PyQt5.QtCore.QRect(200, 200, 400, 300)
