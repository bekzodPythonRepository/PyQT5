from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

window.move(10, 10)
print(window.x(), window.y()) # 10 10
window.show() # Отображаем окно
sys.exit(app.exec_())
