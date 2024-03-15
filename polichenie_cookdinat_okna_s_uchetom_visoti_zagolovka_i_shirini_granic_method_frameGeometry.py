from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

window.setGeometry(100, 100, 200, 70)
window.show() # Отображаем окно
rect = window.geometry()
print(rect.left(), rect.top()) # 100 100
print(rect.width(), rect.height()) # 200 700
rect = window.frameGeometry()
print(rect.left(), rect.top()) # 99 69
print(rect.width(), rect.height()) # 202 102
sys.exit(app.exec_())
