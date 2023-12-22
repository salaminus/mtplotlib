import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Expl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 1024, 800)
        self.setWindowTitle("Мониторинг метеоданных")
        self.btn = QPushButton('КНОПКА', self)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.txt)

        self.lbl = QLabel(self)
        self.lbl.move(10, 10)
        self.lbl.setText('ЭТО Надпись!')
        self.lbl.resize(150, 50)

        self.textEdit = QLineEdit(self)
        self.textEdit.move(10, 100)
    # Водится пример (2+2), в надписи выводится результат (4)
    def txt(self):
        s = self.textEdit.text()
        self.lbl.setText(str(eval(s)))

app = QApplication(sys.argv)
ex = Expl()
ex.show()
sys.exit(app.exec())