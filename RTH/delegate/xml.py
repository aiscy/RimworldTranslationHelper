from PyQt5.QtWidgets import QStyledItemDelegate, QLineEdit
from PyQt5.QtCore import Qt


class XMLDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return QLineEdit(parent)

    def setEditorData(self, widget: QLineEdit, index):
        value = index.model().data(index, Qt.EditRole)
        widget.setText(value)

    def setModelData(self, widget: QLineEdit, model, index):
        value = widget.text()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, widget, option, index):
        widget.setGeometry(option.rect)
