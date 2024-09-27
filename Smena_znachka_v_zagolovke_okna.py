from PyQt5 import QtGui, QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена значка в заголовке окна")
window.resize(300, 100)
ico = QtGui.QIcon("icon.png")
window.setWindowIcon(ico) # Значок для окна
app.setWindowIcon(ico) # Значок для приложения
window.show()
sys.exit(app.exec_())
