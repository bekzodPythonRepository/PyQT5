from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

s1 = QtCore.QSize()
s2 = QtCore.QSize(10, 55)
s3 = QtCore.QSize(s2)
print(s1) # PyQt5.QtCore.QSize(-1, -1)
print(s2, s3) # PyQt5.QtCore.QSize(10, 55) PyQt5.QtCore.QSize(10, 55)
