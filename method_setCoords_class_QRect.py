from PyQt5 import QtCore


# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect()
r.setCoords(10,10, 100, 500)
print(r) # PyQt5.QtCore.QRect(10, 10, 100, 500)
r.setCoords(10, 10,109, 509)
print(r) # PyQt5.QtCore.QRect(10, 10, 109, 509)
