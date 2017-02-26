import os
import weakref
import gc
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QFileDialog, QMessageBox

from RTH.handlers import tab_widget_factory, AbstractTabWidget
from RTH.ui.main import Ui_MainWindow


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = QSettings()

        self.connect_signals()
        self.load_settings()
        self.tab_widgets = weakref.WeakValueDictionary()
        self.show()

    def connect_signals(self):
        self.save.triggered.connect(self.save_file)
        self.tab_widget.tabCloseRequested.connect(self.close_file)
        self.open_folder.triggered.connect(self.open_project)
        self.project_view.doubleClicked.connect(lambda m: self.open_file(self.project_view.model().filePath(m)))

    def load_settings(self):
        pass

    def open_project(self):
        dir_path = QFileDialog.getExistingDirectory(self, options=QFileDialog.ShowDirsOnly)
        if not os.path.exists(os.path.join(dir_path, 'About', 'About.xml')):
            QMessageBox.warning(self, 'RimworldTranslationHelper',
                                'Укажите директорию, которая содержит мод для игры Rimworld', buttons=QMessageBox.Ok)
            return
        project_model = QFileSystemModel()
        project_model.setRootPath(dir_path)
        self.project_view.setModel(project_model)
        self.project_view.setRootIndex(project_model.index(dir_path))
        for col_number in range(1, 4):
            self.project_view.setColumnHidden(col_number, True)

    def open_file(self, file_path):
        if os.path.isdir(file_path):  # TODO
            return
        if file_path in self.tab_widgets:
            self.tab_widget.setCurrentWidget(self.tab_widgets[file_path])
            return
        try:
            widget = tab_widget_factory(file_path, parent=self)
        except Exception as error_msg:
            QMessageBox.critical(self, 'RimworldTranslationHelper',
                                 'При открытии файла произошла ошибка:\n{}'.format(error_msg), buttons=QMessageBox.Ok)
            return
        self.tab_widget.addTab(widget, widget.file_name)
        self.tab_widget.setCurrentWidget(widget)
        self.tab_widgets[file_path] = widget

    def close_file(self, index):
        widget = self.tab_widget.widget(index)  # type: AbstractTabWidget
        widget.deleteLater()
        widget.close()
        self.tab_widget.removeTab(index)

    def save_file(self):
        if not self.tab_widget.count():
            return
        widget = self.tab_widget.currentWidget()
        model = widget.model()
        if not model.is_modified:
            return
        file_path = model.file_path
        tree = model.xml_tree
        tree.write(file_path, encoding=tree.docinfo.encoding, pretty_print=True, xml_declaration=True)
        model.is_modified = False
