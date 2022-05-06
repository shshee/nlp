# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'legalretriever.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from conceptualGraph import ConceptualGraph
from enums import GraphTypes
from query_handler import reduce_words
from dataHandler import DataHandler
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
from query import query_data


class Ui_MainWindow(object):
    NumButtons = ['Đồ thị câu truy vấn', 'Đồ thị dữ liệu', 'Đồ thị tương đồng']
    tagOfCurrentTab = GraphTypes.QUERY

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1881, 911)
        MainWindow.setMaximumSize(QtCore.QSize(1881, 911))
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(890, 10, 981, 71))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.comboBox = QtWidgets.QComboBox(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        for _ in query_data:
            self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 861, 871))
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(1, 313)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(900, 470, 961, 421))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(900, 80, 961, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout1")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        font = QtGui.QFont()
        font.setPointSize(4)
        self.canvas.setFont(font)
        self.gridLayout.addWidget(self.canvas, 0, 1, 9, 5)

        self.createVerticalGroupBox()
        buttonLayout = QtWidgets.QVBoxLayout()
        buttonLayout.addWidget(self.verticalGroupBox)
        self.gridLayout.addLayout(buttonLayout, 0, 0)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, 450, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.textEdit.clear)
        self.pushButton.clicked.connect(self.onRetrieveClicked)
        self.tableWidget.itemClicked.connect(self.handleItemClicked)

        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Legal Retriever"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate(
            "MainWindow", "Nhập vào câu hỏi cần tra cứu"))

        for index, query in enumerate(query_data):
            self.comboBox.setItemText(index, _translate("MainWindow", query))
        self.pushButton.setText(_translate("MainWindow", "Tra cứu"))
        self.pushButton_2.setText(_translate("MainWindow", "Xóa "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trích dẫn"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Điều"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Khoản"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mã luật"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Điểm"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Nội dung"))

    def loadData(self):
        dir = "./data/"
        self.dataHandler = DataHandler(
            dir+"laws.json", dir+"articles.json", dir+"rules.json", dir+"lookups.json")

    def onRetrieveClicked(self):
        self.__toQueryView()

        comparison_result = self.dataHandler.compare(self.getGraphFromQuery())
        self.comparison = comparison_result

        self.tableWidget.setRowCount(len(comparison_result))
        for idx, val in enumerate(comparison_result):
            for column in range(5):
                self.tableWidget.setItem(
                    idx, column, QtWidgets.QTableWidgetItem(val[column]))

        self.tableWidget.sortItems(4, QtCore.Qt.DescendingOrder)

    def getGraphFromQuery(self):
        input_value = self.textEdit.toPlainText()
        reduced = reduce_words(
            input_value if input_value else str(self.comboBox.currentText()))

        return ConceptualGraph(reduced)

    def showGraph(self, graph, type):
        self.figure.clf()

        labeldict = {}
        for node in graph.getNodes():
            labeldict[node] = node[0]

        color_for_node = "#000000"
        if type == GraphTypes.QUERY:
            color_for_node = '#0099ff'
        elif type == GraphTypes.DATA:
            color_for_node = "#00ff00"
        elif type == GraphTypes.SIMILARITY:
            color_for_node = "#ff3300"

        nx.draw(graph.getGraph(), labels=labeldict, with_labels=True,
                node_size=200, node_color=color_for_node)

        self.canvas.draw_idle()

    def createVerticalGroupBox(self):
        self.verticalGroupBox = QtWidgets.QGroupBox()

        layout = QtWidgets.QVBoxLayout()
        for i in range(len(self.NumButtons)):
            button = QtWidgets.QPushButton(self.NumButtons[i])
            button.setObjectName(self.NumButtons[i])
            layout.addWidget(button)
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
            self.verticalGroupBox.setLayout(layout)
            if i == 0:
                button.clicked.connect(self.__toQueryView)
            elif i == 1:
                button.clicked.connect(self.__toDataView)
            elif i == 2:
                button.clicked.connect(self.__toSimilarityView)

    def __toQueryView(self):
        self.tagOfCurrentTab = GraphTypes.QUERY
        self.defineGraphToShow("")

    def __toDataView(self):
        self.tagOfCurrentTab = GraphTypes.DATA
        self.handleItemClicked()

    def __toSimilarityView(self):
        self.tagOfCurrentTab = GraphTypes.SIMILARITY
        self.handleItemClicked()

    def handleItemClicked(self):
        indexes = self.tableWidget.selectedIndexes()
        if indexes and len(indexes) == 1:
            itemID = indexes[0].siblingAtColumn(0).data()
            self.defineGraphToShow(itemID)
            self.textBrowser_2.setText(
                self.dataHandler.getContentFromId(itemID))

    def defineGraphToShow(self, itemID):
        if self.tagOfCurrentTab == GraphTypes.DATA:
            graph = self.dataHandler.getDataGraphFromId(itemID)[0][0]
        elif self.tagOfCurrentTab == GraphTypes.SIMILARITY:
            graph = list(filter(lambda c: c[0] == itemID, self.comparison))[
                0][5]
        else:
            graph = self.getGraphFromQuery()

        self.showGraph(graph, self.tagOfCurrentTab)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.loadData()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
