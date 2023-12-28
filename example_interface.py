import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Expl(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.btn.clicked.connect(self.run)

    def run(self):
        s = self.lineEdit.text()
        self.lbl.setText(s)

app = QApplication(sys.argv)
ex = Expl()
ex.show()
sys.exit(app.exec())