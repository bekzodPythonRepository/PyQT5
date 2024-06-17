from PyQt5 import QtCore


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
r.moveTo(0, 0)
print(r) # PyQt5.QtCore.QRect(0, 0, 400, 300)
r.moveTo(QtCore.QPoint(10, 10))
print(r) # PyQt5.QtCore.QRect(10, 10, 400, 300)
r.moveLeft(5)
r.moveTop(0)
print(r) # PyQt5.QtCore.QRect(5, 0, 400, 300)
