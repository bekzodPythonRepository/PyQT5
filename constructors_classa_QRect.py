from PyQt5 import QtCore

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/
r = QtCore.QRect()
print(r.left(), r.top(), r.right(), r.bottom(), r.width(), r.height()) # 0 0 -1 -1 0 0
r = QtCore.QRect(10, 15, 400, 300)
print(r.left(), r.top(), r.right(), r.bottom(), r.width(), r.height()) # 10 15 409 314 400 300
r = QtCore.QRect(QtCore.QPoint(10, 15), QtCore.QSize(400, 300))
print(r.left(), r.top(), r.right(), r.bottom(), r.width(), r.height()) # 10 15 409 314 400 300
r = QtCore.QRect(QtCore.QPoint(10, 15), QtCore.QPoint(409, 314))
print(r.left(), r.top(), r.right(), r.bottom(), r.width(), r.height()) # 10 15 409 314 400 300
r = QtCore.QRect(r)
print(r.left(), r.top(), r.right(), r.bottom(), r.width(), r.height()) # 10 15 409 314 400 300
