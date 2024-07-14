from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(0, 0, 20, 20)
print(r.intersects(QtCore.QRect(10, 10, 20, 20))) # True
print(r.intersected(QtCore.QRect(10, 10, 20, 20))) # PyQt5.QtCore.QRect(10, 10, 10, 10)
