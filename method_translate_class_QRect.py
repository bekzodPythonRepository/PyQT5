from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

r = QtCore.QRect(0, 0, 400, 300)
r.translate(20, 15)
print(r) # PyQt5.QtCore.QRect(20, 15, 400, 300)
r.translate(QtCore.QPoint(10, 5))
print(r) # PyQt5.QtCore.QRect(30, 20, 400, 300)
