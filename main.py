import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from fileDataRead import readDataFile

class MonitoringApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)

        # Навигация
        self.navTab = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визуализация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnalizeTab.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredictTab.clicked.connect(self.navigate), 4],
            'Мониторинг': [self.btnMonitoringTab.clicked.connect(self.navigate), 5],
            'Экспорт': [self.btnExportTab.clicked.connect(self.navigate), None]
        }

        # Загрузка данных
        self.downloadFileData.clicked.connect(self.loadTable)
        self.clearBtnTableWidget.clicked.connect(self.clearTableWidget)

    def navigate(self):
        # print(self.sender().text())
        print(self.sender().text(), self.navTab[self.sender().text()][1])
        self.tabWidget.setCurrentIndex(self.navTab[self.sender().text()][1])


    def clearTableWidget(self):
        self.tableWidget.clear()

    def loadTable(self):
        data = readDataFile()
        self.tableWidget.setColumnCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(
            ['станция', 'год', 'месяц', 'день', 'час', 'направление ветра', 'осадки', 'температура', 'влажность']
        )
        self.tableWidget.setRowCount(0)
        for i in range(len(data)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(data[i])):
                print(i, j, data[i][j])
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        self.tableWidget.resizeColumnsToContents()

app = QApplication(sys.argv)
ex = MonitoringApp()
ex.show()
sys.exit(app.exec())