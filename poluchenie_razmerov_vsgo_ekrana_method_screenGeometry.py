from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

desktop = QtWidgets.QApplication.desktop()
rect = desktop.screenGeometry()
print(rect.left(),rect.top()) # 0 0
print(rect.width(), rect.height()) # 1920 1080

window.show() # Отображаем окно
sys.exit(app.exec_())
