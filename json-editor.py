import sys
import json
from PyQt5 import QtWidgets, Qt, uic
from MainWindow import Ui_MainWindow


def beautify(json_str):
    return json.dumps(json.loads(json_str), indent=4, sort_keys=True)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Load the converted UI file
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # Set window properties
        self.setWindowTitle("JSON editor")
        self.actionQuit.triggered.connect(self.on_quit)
        
        self.beautify_button.clicked.connect(self.on_beautify_click)
    
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
        result = beautify(contents)
        self.json_view.setText(result)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
