import sys
import json
from PyQt5 import QtWidgets, Qt, uic, QtGui
from MainWindow import Ui_MainWindow

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
        self.json_view.raise_()
        self.json_view.setText(result)
    
    def on_tree_click(self):
        root_model = QtGui.QStandardItemModel()
        self.treeView.raise_()
        self.treeView.setModel(root_model)
        json_data = json.loads(self.json_enter.toPlainText())
        self._populate(json_data, root_model.invisibleRootItem())
    
    def _beautify(self, json_str):
        return json.dumps(json.loads(json_str), indent=4, sort_keys=True)
    
    def _populate(self, children, parent):
        for child in sorted(children) :
            print(child)
            child_item = QtGui.QStandardItem(child)
            parent.appendRow(child_item)
            if isinstance(children, dict):
                self._populate(children[child], child_item)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
