from PyQt5 import QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget() #Родительский компонент-окно
window.setWindowTitle("QHBoxLayout")
window.resize(300, 60)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
hbox = QtWidgets.QHBoxLayout() #создаем контейнер
hbox.addWidget(button1) #Добавляем компоненты
hbox.addWidget(button2)
window.setLayout(hbox) #Передаем ссылку радителю
window.show()
sys.exit(app.exec_())
