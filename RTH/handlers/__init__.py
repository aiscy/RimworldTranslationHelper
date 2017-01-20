from PyQt5.QtWidgets import QTreeView

from RTH.delegate.xml import XMLDelegate
from RTH.models.xml import DomModel


#
# class BaseHandler:
#     def __init__(self, file_path: str):
#         self.file_path = file_path
#         self.view = None
#         self.model = None
#         self.delegate = None
#
#     def open(self):
#         raise NotImplementedError
#
#     def close(self):
#         raise NotImplementedError
#
#     def __call__(self, *args, **kwargs):
#         self.open()


def xml_handler(file_path: str) -> QTreeView:
    model = DomModel(file_path)
    view = QTreeView()
    view.setModel(model)
    view.expandAll()
    view.setRootIsDecorated(False)
    view.setItemsExpandable(False)
    delegate = XMLDelegate()
    view.setItemDelegate(delegate)
    return view


