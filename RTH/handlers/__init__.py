import inspect
import os
from pprint import pprint
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTreeView

from RTH.delegate.xml import XMLDelegate
from RTH.models.xml import DomModel


class AbstractTabWidget:
    def __init__(self, path, parent=None):
        super().__init__()
        self._path = path
        self._parent = parent
        self._file_object = None
        self._file_name = os.path.basename(path)
        self._is_modified = False  # Флаг для проверки был ли изменен файл
        self._create()

    def _create(self):
        raise NotImplementedError

    def _save(self):
        raise NotImplementedError

    def _close(self):
        raise NotImplementedError

    @property
    def file_name(self):
        return self._file_name

    def save(self) -> None:
        if self._is_modified:
            self._save()
            self._is_modified = False

    def close(self) -> None:
        if self._is_modified:
            pass  # TODO Запрос сохранения
        self._close()


class XML(AbstractTabWidget, QTreeView):
    def _create(self):
        self.setParent(self._parent)
        self.expandAll()
        self.setRootIsDecorated(False)
        self.setItemsExpandable(False)
        model = DomModel(self._path)
        model.dataChanged.connect(lambda: print('Data Changed'))
        self.setModel(model)
        delegate = XMLDelegate()
        self.setItemDelegate(delegate)

    def _save(self):
        pass

    def _close(self):
        pass


def tab_widget_factory(path, parent=None) -> AbstractTabWidget:
    ext = os.path.splitext(path)[1].replace('.', '')
    for subclass in AbstractTabWidget.__subclasses__():
        if subclass.__name__.lower() == ext:
            return subclass(path, parent)