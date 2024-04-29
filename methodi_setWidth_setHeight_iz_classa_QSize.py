from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

s = QtCore.QSize()
s.setWidth(10)
s.setHeight(55)
print(s.width(), s.height()) # 10 55
