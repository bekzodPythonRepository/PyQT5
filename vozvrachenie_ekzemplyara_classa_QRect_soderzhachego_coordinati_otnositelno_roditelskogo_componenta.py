from PyQt5 import QtWidgets, QtCore
import sys

# Не забудьте добавить в PATH  "путь к интерпретатору\\Lib\\site-packages\\PyQt5\\Qt5\\plugins"

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() # Создаем окно

window.setGeometry(QtCore.QRect(100, 100, 100, 70))
rect = window.rect() # экземпляр класса QRect
print(rect.left(), rect.top()) # 0 0
print(rect.width(), rect.height()) # 100 70
window.show() # Отображаем окно
sys.exit(app.exec_())
