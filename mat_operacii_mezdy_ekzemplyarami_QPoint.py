from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

p1 = QtCore.QPoint(10, 20)
p2 = QtCore.QPoint(5, 9)
print(p1+p2, p1-p2) # PyQt5.QtCore.QPoint(15, 29) PyQt5.QtCore.QPoint(5, 11)
print(p1*2.5, p1/2.0) # PyQt5.QtCore.QPoint(25, 50) PyQt5.QtCore.QPoint(5, 10)
print(-p1, p1==p2, p1!=p2) #  PyQt5.QtCore.QPoint(-10, -20) False True
