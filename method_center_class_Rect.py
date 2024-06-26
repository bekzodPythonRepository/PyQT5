from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
print(r.center()) # PyQt5.QtCore.QPoint(209, 164)
