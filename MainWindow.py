# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'json-editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.json_enter = QtWidgets.QTextEdit(self.centralwidget)
        self.json_enter.setGeometry(QtCore.QRect(20, 30, 401, 501))
        self.json_enter.setObjectName("json_enter")
        self.json_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.json_view.setGeometry(QtCore.QRect(610, 30, 401, 501))
        self.json_view.setObjectName("json_view")
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
        self.actionOPen_File = QtWidgets.QAction(MainWindow)
        self.actionOPen_File.setObjectName("actionOPen_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionReload_File = QtWidgets.QAction(MainWindow)
        self.actionReload_File.setObjectName("actionReload_File")
        self.menuMenu.addAction(self.actionOPen_File)
        self.menuMenu.addAction(self.actionSave_File)
        self.menuMenu.addAction(self.actionReload_File)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOPen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionReload_File.setText(_translate("MainWindow", "Reload File"))
