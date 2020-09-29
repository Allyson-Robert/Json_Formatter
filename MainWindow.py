# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'json-editor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 821)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.json_enter = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.json_enter.setGeometry(QtCore.QRect(20, 30, 401, 501))
        self.json_enter.setObjectName("json_enter")
        self.json_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.json_view.setGeometry(QtCore.QRect(610, 30, 401, 501))
        self.json_view.setObjectName("json_view")
        self.beautify_button = QtWidgets.QPushButton(self.centralwidget)
        self.beautify_button.setGeometry(QtCore.QRect(450, 30, 131, 31))
        self.beautify_button.setObjectName("beautify_button")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(20, 540, 991, 301))
        self.console.setObjectName("console")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(610, 30, 401, 501))
        self.treeView.setObjectName("treeView")
        self.tree_button = QtWidgets.QPushButton(self.centralwidget)
        self.tree_button.setGeometry(QtCore.QRect(450, 70, 131, 31))
        self.tree_button.setObjectName("tree_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionReload_File = QtWidgets.QAction(MainWindow)
        self.actionReload_File.setObjectName("actionReload_File")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionOpen_File)
        self.menuMenu.addAction(self.actionSave_File)
        self.menuMenu.addAction(self.actionReload_File)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.beautify_button.setText(_translate("MainWindow", "Beautify"))
        self.tree_button.setText(_translate("MainWindow", "Tree View"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionReload_File.setText(_translate("MainWindow", "Reload File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

