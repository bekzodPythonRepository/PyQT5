from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
print(r.topLeft(), r.topRight(), r.bottomLeft(), r.bottomRight())
# PyQt5.QtCore.QPoint(10, 15) PyQt5.QtCore.QPoint(409, 15) PyQt5.QtCore.QPoint(10, 314) PyQt5.QtCore.QPoint(409, 314)
