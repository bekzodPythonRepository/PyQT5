from PyQt5 import QtCore, QtWidgets, QtGui
import sys

# Добавьте в системные переменные PATH /путь к интерпретатору Python/Lib//site-packages//PyQt5//Qt5//plugins/

#Создаем класс делегата
class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, options, index):
        #Создаем компонент-редактор, используемый для правки значений
        #количества позиции
        editor = QtWidgets.QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setSingleStep(1)
        return editor
    def setEditorData(self, editor, index):
        #Заносим в компонент-редактор значение количества
        value = int(index.model().data(index, QtCore.Qt.EditRole))
        editor.setValue(value)
    def updateEditorGeometry(self, editor, options, index):
        #Указываем размеры компонент-редактора
        editor.setGeometry(options.rect)
    def setModelData(self, editor, model, index):
        #Заносим исправленное значение количества модель
        value = str(editor.value())
        model.setData(index, value, QtCore.Qt.EditRole)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle("Использование делегата")
sti = QtGui.QStandardItemModel(parent=window)
lst1 = ['Дискета', 'Бумага для принтера', 'Барабан для принтера']
lst2 = ["10", "3", "8"]
for row in range(0, 3):
    item1 = QtGui.QStandardItem(lst1[row])
    item2 = QtGui.QStandardItem(lst2[row])
    sti.appendRow([item1, item2])
sti.setHorizontalHeaderLabels(['Повар', 'Кол-во'])
window.setModel(sti)
#Назначаем делегат второму столбцу таблицы
window.setItemDelegateForColumn(1, SpinBoxDelegate())
window.setColumnWidth(0, 150)
window.resize(300, 150)
window.show()
sys.exit(app.exec_())
