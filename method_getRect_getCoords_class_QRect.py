from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
print(r.getRect(), r.getCoords()) # (10, 15, 400, 300) (10, 15, 409, 314)
