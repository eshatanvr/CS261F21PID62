# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
import csv

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def loaddata(self):
        property_titel = []
        area = []
        price = []
        location = []
        bedroom = []
        bathroom = []
        discryption = []
        with open('nn.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                property_titel.append(lines[0])
                discryption.append(lines[1])
                price.append(lines[2])
                bedroom.append(lines[3])
                bathroom.append(lines[4])
                location.append(lines[5])
                area.append(lines[6])

        row = 0
        self.tableWidget.setRowCount(len(property_titel))
        for title in property_titel:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
            row = row + 1
        row = 0
        for ar in area:
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
            row = row + 1
        row = 0
        for lo in location:
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
            row = row + 1
        row = 0
        for pr in price:
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
            row = row + 1
        row = 0
        for bd in bedroom:
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
            row = row + 1
        row = 0
        for ba in bathroom:
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
            row = row + 1
        row = 0
        for ds in discryption:
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
            row = row + 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1425, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -60, 1511, 981))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Screenshot 2021-10-23 072704.png"))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(510, 20, 800, 811))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setRowCount(1200025)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
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
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 10, 191, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons8-pixar-lamp-2-160.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(53)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 40, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons8-imdb-48.png"))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 350, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 78)
        self.progressBar.setObjectName("progressBar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 400, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 431, 441))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("photo-1569982175971-d92b01cf8694.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 220, 101, 91))
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("icons8-play-100.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 220, 101, 91))
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("icons8-pause-button-100.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 220, 101, 91))
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons8-stop-100.png"))
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 550, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 450, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 470, 51, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("icons8-search-48.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 540, 51, 41))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("icons8-filter-48.png"))
        self.label_13.setObjectName("label_13")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 500, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 550, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 500, 51, 28))
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.tableWidget.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.progressBar.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_7.raise_()
        self.label_11.raise_()
        self.comboBox.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.lineEdit.raise_()
        self.comboBox_3.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1425, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cine-Scrape"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Certificate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ratings"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Votes"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Cine-Scrape</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Remaining Data: 45 out of 24000 </span><span style=\" color:#ffffff;\">pages</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Search By:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Sort By:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Names"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Genre"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Duration"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Names"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Votings"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Duration"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Ratings"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton.clicked.connect(lambda: self.loaddata())
        # def Open_file(self):
        #     try:
        #         self.all_data = pd.read_csv('nn.csv')
        #         print("Opened")
        #     except:
        #         print("Error occured while opening the file")
        #
        # def DataHead(self):
        #     NumRows = len(self.all_data.index)
        #     self.tableWidget.setColumnCount(len(self.all_data.columns))
        #     self.tableWidget.setRows(NumRows)
        #     self.tableWidget.setHorizontalHeaderLables(self.all_data.columns)
        #
        #     for i in range(NumRows):
        #         for j in range(len(self.all_data.columns)):
        #             self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
        #     self.tableWidget.resizeColumnsToContents()
        #     self.tableWidget.resizeRowsToContents()
        # self.label_8.mousePressEvent = self.DataHead(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())




