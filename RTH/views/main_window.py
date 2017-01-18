import os
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QFileDialog, QMessageBox, QTreeView

from RTH.models.xml import DomModel
from RTH.delegate.xml import XMLDelegate
from RTH.ui.main import Ui_MainWindow


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = QSettings('SlowSoft', 'RimworldTranslationHelper')

        self.connect_signals()
        self.load_settings()
        self.load_models()
        self.opened_files = {}

        self.show()

    def connect_signals(self):
        self.tab_widget.tabCloseRequested.connect(self.close_xml)
        self.open_folder.triggered.connect(self.open_project)
        self.project_view.doubleClicked.connect(lambda m: self.open_xml(self.project_view.model().filePath(m)))

    def load_settings(self):
        pass

    def load_models(self):
        pass

    def open_project(self):
        dir_path = QFileDialog.getExistingDirectory(self, options=QFileDialog.ShowDirsOnly)
        if not os.path.exists(os.path.join(dir_path, 'About', 'About.xml')):
            QMessageBox.warning(self, 'RimworldTranslationHelper', 'Укажите директорию, которая содержит мод для игры Rimworld', buttons=QMessageBox.Ok)
            return
        project_model = QFileSystemModel()
        project_model.setRootPath(dir_path)
        self.project_view.setModel(project_model)
        self.project_view.setRootIndex(project_model.index(dir_path))
        for col_number in range(1, 4):
            self.project_view.setColumnHidden(col_number, True)

    def open_xml(self, file_path):
        if os.path.isdir(file_path):  # TODO
            return
        if file_path in self.opened_files:
            self.tab_widget.setCurrentWidget(self.opened_files[file_path]['view'])
            return
        try:
            model = DomModel(file_path)
        except Exception as error_msg:
            QMessageBox.critical(self, 'RimworldTranslationHelper', 'При открытии файла произошла ошибка:\n{}'.format(error_msg), buttons=QMessageBox.Ok)
            return
        view = QTreeView()
        view.setModel(model)
        view.expandAll()
        view.setItemsExpandable(False)
        delegate = XMLDelegate()
        view.setItemDelegate(delegate)
        index = self.tab_widget.addTab(view, os.path.basename(file_path))
        self.tab_widget.setCurrentIndex(index)
        self.opened_files[file_path] = {'view': view, 'model': model, 'delegate': delegate}

    def close_xml(self, index):
        widget = self.tab_widget.widget(index)
        file_path = widget.model().file_path
        self.opened_files.pop(file_path)
        self.tab_widget.removeTab(index)
        widget.deleteLater()  # TODO Make some tests