from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

p = QtCore.QPoint()
print(p.x(),p.y()) # 0 0
p1 = QtCore.QPoint(10,88)
print(p1.x(),p1.y()) # 10 88
p2 = QtCore.QPoint(QtCore.QPoint(10,88))
print(p2.x(),p2.y()) # 10 88
