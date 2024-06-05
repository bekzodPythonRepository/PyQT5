from PyQt5 import QtCore


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect()
r.setTopLeft(QtCore.QPoint(10, 5))
r.setBottomRight(QtCore.QPoint(39, 19))
print(r) # PyQt5.QtCore.QRect(10, 5, 30, 15)
r.setTopRight(QtCore.QPoint(39, 5))
r.setBottomRight(QtCore.QPoint(10, 19))
print(r) # PyQt5.QtCore.QRect(10, 5, 1, 15)
