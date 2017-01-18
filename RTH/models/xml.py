from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt
from lxml.etree import parse, XMLParser


class DomItem:
    def __init__(self, node, row, parent=None):
        self.dom_node = node
        # Record the item's location within its parent.
        self.row_number = row
        self.parent_item = parent
        self.child_items = {}

    def node(self):
        return self.dom_node

    def parent(self):
        return self.parent_item

    def child(self, i):
        if i in self.child_items:
            return self.child_items[i]

        if 0 <= i < len(self.dom_node.getchildren()):
            child_node = self.dom_node.getchildren()[i]
            child_item = DomItem(child_node, i, self)
            self.child_items[i] = child_item
            return child_item

        return None

    def row(self):
        return self.row_number


class DomModel(QAbstractItemModel):
    def __init__(self, file_path, parent=None):
        super().__init__(parent)

        self._file_path = file_path
        self._xml_tree = parse(self._file_path, parser=XMLParser(remove_blank_text=True))
        self.root = DomItem(self._xml_tree.getroot(), 0)

    @property
    def file_path(self):
        return self._file_path

    @property
    def xml_tree(self):
        return self._xml_tree

    def columnCount(self, parent=None, *args, **kwargs):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:

            item = index.internalPointer()
            node = item.node()

            if index.column() == 0:
                return node.tag

            if index.column() == 1:
                value = node.text
                return value

        if role == Qt.EditRole:
            if index.column() == 1:
                return index.internalPointer().node().text

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return None
        item = index.internalPointer()
        node = item.node()
        node.text = value
        self.dataChanged.emit(index, index, [Qt.EditRole])
        return True


    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        if index.column() == 0:
            return Qt.NoItemFlags
        if index.column() == 1:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return 'Имя ноды'

            if section == 1:
                return 'Значение'

        return None

    def index(self, row, column, parent=None, *args, **kwargs):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        else:
            return QModelIndex()

    def parent(self, index=None):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent()

        if not parent_item or parent_item == self.root:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        return len(parent_item.node().getchildren())