import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *

from fileDataRead import readDataFile


class MonitoringApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)

        self.totalData = {}  # Данные метеостанций
        self.data = []  # Данные по текущей метеостанции
        self.listStations = set()
        self.selectedItemListWidget = None

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

        # Визуализация
        self.visualizationBtn.clicked.connect(self.vizualGraph)
        self.clearBtnGraphView.clicked.connect(self.clearVizualGraphView)
        self.pushBtnCheckboxesClear.clicked.connect(self.chekboxesVizClear)
        # Чекбоксы
        self.checkBoxesVisual = [self.checkBoxHumidity,
                                 self.checkBoxPrecipitation,
                                 self.checkBoxDirectionWild,
                                 self.checkBoxTemperature]

        # Кнопки "На главную"
        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnMonitoringtab.clicked.connect(self.homeGo)

    def navigate(self):
        # Навигация по табам
        # print(self.sender().text())
        print(self.sender().text(), self.navTab[self.sender().text()][1])
        self.tabWidget.setCurrentIndex(self.navTab[self.sender().text()][1])

    def homeGo(self):
        # Переход на первую вкладку "Навигация"
        self.tabWidget.setCurrentIndex(0)

    def clearTableWidget(self):
        # Очистка таблицы предпросмотра загружаемых данных
        self.tableWidget.clear()
        self.data = []

    def loadTable(self):
        # Загрузка данных из файла
        fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        print(fname)
        self.data = readDataFile(fname)
        if self.data[0][0] not in self.totalData.keys():
            self.listStations.add(self.data[0][0])
            self.totalData[self.data[0][0]] = self.data

            self.tableWidget.setColumnCount(len(self.data[0]))
            self.tableWidget.setHorizontalHeaderLabels(
                ['станция', 'год', 'месяц', 'день', 'час', 'направление ветра', 'осадки', 'температура', 'влажность']
            )
            self.tableWidget.setRowCount(0)
            for i in range(len(self.data[:int(self.spinBoxCountLineData.text())])):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j in range(len(self.data[i])):
                    # print(self.data[i], len(self.data[i]))
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.data[i][j])))
            self.tableWidget.resizeColumnsToContents()
            self.labelStatusDownloadData.setText(f'Статус: Данные загружены. Всего {len(self.data)} записей.')
        else:
            print('Повторка!')
            self.labelStatusDownloadData.setText(f'Статус: Эти данные уже были загружены.')

        # Заполнение listWidgetStationMeteo
        for item in self.listStations:
            items = [str(self.listWidgetStationMeteo.item(i).text()) for i in
                     range(self.listWidgetStationMeteo.count())]
            # print(items)
            if item not in items:
                self.listWidgetStationMeteo.addItem(item)

    def vizualGraph(self):
        # Выбор станции
        self.selectedItemListWidget = [x.text() for x in self.listWidgetStationMeteo.selectedItems()]
        print(self.selectedItemListWidget)

        beginDataViz = str(self.calendarWidgetViz1.selectedDate()).split('(')[1][:-1]
        endDataViz = str(self.calendarWidgetViz2.selectedDate()).split('(')[1][:-1]
        print(f"Begin: {beginDataViz}, End: {endDataViz}")

        self.graphicsView.clear()

        # Выбор параметров в чекбоксах и отрисовка графика
        if self.checkBoxHumidity.isChecked():  # Влажность
            self.graphicsView.plot(range(len(self.totalData[self.selectedItemListWidget[0]])),
                                   [int(i[-1]) for i in self.totalData[self.selectedItemListWidget[0]]], pen='r')
        if self.checkBoxPrecipitation.isChecked():  # Осадки
            self.graphicsView.plot(range(len(self.totalData[self.selectedItemListWidget[0]])),
                                   [int(i[-3]) for i in self.totalData[self.selectedItemListWidget[0]]], pen='g')
        if self.checkBoxDirectionWild.isChecked():
            self.graphicsView.plot(range(len(self.totalData[self.selectedItemListWidget[0]])),
                                   [int(i[-4]) for i in self.totalData[self.selectedItemListWidget[0]]], pen='b')
        if self.checkBoxTemperature.isChecked():
            self.graphicsView.plot(range(len(self.totalData[self.selectedItemListWidget[0]])),
                                   [int(i[-2]) for i in self.totalData[self.selectedItemListWidget[0]]], pen='y')

    def chekboxesVizClear(self):
        # Сброс чекоксов
        for box in self.checkBoxesVisual:
            box.setChecked(False)

    def clearVizualGraphView(self):
        # Очистка графика
        self.graphicsView.clear()


app = QApplication(sys.argv)
ex = MonitoringApp()
ex.show()
sys.exit(app.exec())
