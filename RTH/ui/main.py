# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.project_view = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_view.sizePolicy().hasHeightForWidth())
        self.project_view.setSizePolicy(sizePolicy)
        self.project_view.setMinimumSize(QtCore.QSize(0, 0))
        self.project_view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.project_view.setSizeIncrement(QtCore.QSize(0, 0))
        self.project_view.setBaseSize(QtCore.QSize(0, 0))
        self.project_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.project_view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.project_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.project_view.setTextElideMode(QtCore.Qt.ElideRight)
        self.project_view.setRootIsDecorated(True)
        self.project_view.setAnimated(True)
        self.project_view.setHeaderHidden(False)
        self.project_view.setObjectName("project_view")
        self.tab_widget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 19))
        self.menubar.setObjectName("menubar")
        self.menuOpen_mod = QtWidgets.QMenu(self.menubar)
        self.menuOpen_mod.setObjectName("menuOpen_mod")
        MainWindow.setMenuBar(self.menubar)
        self.open_folder = QtWidgets.QAction(MainWindow)
        self.open_folder.setObjectName("open_folder")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.save.setObjectName("save")
        self.menuOpen_mod.addAction(self.open_folder)
        self.menuOpen_mod.addAction(self.save)
        self.menubar.addAction(self.menuOpen_mod.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuOpen_mod.setTitle(_translate("MainWindow", "Файл"))
        self.open_folder.setText(_translate("MainWindow", "Открыть директорию..."))
        self.open_folder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.save.setShortcut(_translate("MainWindow", "Ctrl+S"))

