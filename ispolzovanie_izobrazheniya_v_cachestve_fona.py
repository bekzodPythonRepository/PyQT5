from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Изображение в качестве фона")
window.resize(300, 100)
pal = window.palette()
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
             QtGui.QBrush(QtGui.QPixmap("background2.jpeg")))
window.setPalette(pal)
label = QtWidgets.QLabel("Текст надписи")
label.setAlignment(QtCore.Qt.AlignCenter)
label.setStyleSheet("background-image: url(background1.jpeg);")
label.setAutoFillBackground(True)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
