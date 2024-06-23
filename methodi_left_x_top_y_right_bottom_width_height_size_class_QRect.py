from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect(10, 15, 400, 300)
print(r.left(), r.top(), r.x(), r.y(), r.right(), r.bottom()) # 10 15 10 15 409 314
print(r.width(), r.height(), r.size()) # 400 300 PyQt5.QtCore.QSize(400, 300)
