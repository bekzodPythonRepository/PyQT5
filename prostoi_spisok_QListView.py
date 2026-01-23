from PyQt5 import QtGui, QtWidgets
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QListView")
lv = QtWidgets.QListView()
sti = QtGui.QStandardItemModel(parent=window)
lst = ['Perl', 'PHP', 'Python', 'Ruby']
for row in range(0, 4):
    if row == 2:
        iconfile = 'python.png'
    else:
        iconfile = 'icon.png'
    item = QtGui.QStandardItem(QtGui.QIcon(iconfile), lst[row])
    sti.appendRow(item)
lv.setModel(sti)
layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(lv)
window.show()
sys.exit(app.exec_())
