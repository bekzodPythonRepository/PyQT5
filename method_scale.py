from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

s = QtCore.QSize(50, 20)
s.scale(70, 60, QtCore.Qt.IgnoreAspectRatio)
print(s) # PyQt5.QtCore.QSize(70, 60)
s = QtCore.QSize(50, 20)
s.scale(70, 60, QtCore.Qt.KeepAspectRatio)
print(s) # PyQt5.QtCore.QSize(70, 28)
s = QtCore.QSize(50, 20)
s.scale(70, 60, QtCore.Qt.KeepAspectRatioByExpanding)
print(s) # PyQt5.QtCore.QSize(150, 60)
