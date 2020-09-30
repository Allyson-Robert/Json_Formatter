import sys
import json
from PyQt5 import QtWidgets, Qt, uic, QtGui
from MainWindow import Ui_MainWindow

def contains_nest(indict):
    if isinstance(indict, dict):
        for key in indict:
            if isinstance(indict[key], dict):
                return True
    return False

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Load the converted UI file
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # Set window properties
        self.setWindowTitle("JSON editor")
        self.actionQuit.triggered.connect(self.on_quit)
        
        self.beautify_button.clicked.connect(self.on_beautify_click)
        self.tree_button.clicked.connect(self.on_tree_click)
        self.quotes_button.clicked.connect(self.on_quotes_click)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Qt.Key_Escape:
            self.on_quit()
        
        if (e.modifiers() & Qt.Qt.ControlModifier) and e.key() == Qt.Qt.Key_Return:
            self.on_beautify_click()
    
    def on_open(self):
        print("Opened")
    
    def on_quit(self):
        print("You Quit")
        sys.exit()
    
    def on_beautify_click(self):
        contents = self.json_enter.toPlainText()
        result = self._beautify(contents)
        print(contents, result)
        self.json_view.raise_()
        self.json_view.setText(result)
    
    def on_tree_click(self):
        root_model = QtGui.QStandardItemModel()
        self.treeView.raise_()
        self.treeView.setModel(root_model)
        json_data = json.loads(self.json_enter.toPlainText())
        self._populate(json_data, root_model.invisibleRootItem())
    
    def on_quotes_click(self):
        contents = self.json_enter.toPlainText()
        result = self._swap_quotes(contents)
        self.json_enter.setPlainText(result)
    
    def _beautify(self, json_str):
        return json.dumps(json.loads(json_str), indent=4)
    
    def _populate(self, children, parent):
        # If children is a branch, add and continue
        contains_nest(children)
        if isinstance(children, dict):
            print(children)
            for child in children:
                if isinstance(child, dict):
                    child_item = QtGui.QStandardItem("")
                else :
                    child_item = QtGui.QStandardItem(child)
                parent.appendRow(child_item)
                print(child, child_item)
                self._populate(children[child], child_item)
        elif isinstance(children, list):
            for index in range(len(children)):
                child = children[index]
                if isinstance(child, dict):
                    child_item = QtGui.QStandardItem(str(index))
                else :
                    child_item = QtGui.QStandardItem(child)
                parent.appendRow(child_item)
                print(child, child_item)
                self._populate(child, child_item)
        # If children is a leaf, simply add it
        else :
            print(children)
            parent.appendRow(QtGui.QStandardItem(str(children)))
    
    def _swap_quotes(self, json_str):
        return json_str.replace("'", '"')

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
