from PyQt5.QtCore import QUrl, QFile, QTextStream
from PyQt5.QtWidgets import QTreeView, QTextEdit

from RTH.delegate.xml import XMLDelegate
from RTH.models.xml import DomModel

from RTH.utils import ext_dispatcher


@ext_dispatcher
def handler(_):
    raise NotImplementedError


@handler.register('.xml')
def _(file_path: str) -> QTreeView:
    model = DomModel(file_path)
    view = QTreeView()
    view.setModel(model)
    view.expandAll()
    view.setRootIsDecorated(False)
    view.setItemsExpandable(False)
    delegate = XMLDelegate()
    view.setItemDelegate(delegate)
    return view


@handler.register('.txt')
def _(file_path: str) -> QTextEdit:
    file = QFile(file_path)
    stream = QTextStream(file)
    view = QTextEdit
    view.setPlainText(stream.readAll())
    return view
