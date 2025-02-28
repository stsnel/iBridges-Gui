# Form implementation generated from reading ui file 'D:\Christine_irods\iBridges-Gui\gui\ui_files\searchDialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_searchDialog(object):
    def setupUi(self, searchDialog):
        searchDialog.setObjectName("searchDialog")
        searchDialog.resize(800, 800)
        searchDialog.setMinimumSize(QtCore.QSize(800, 800))
        searchDialog.setStyleSheet("QWidget\n"
"{\n"
"    color: rgb(86, 184, 139);\n"
"    background-color: rgb(54, 54, 54);\n"
"    selection-background-color: rgb(58, 152, 112);\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"background-color: rgb(85, 87, 83);\n"
"selection-background-color: rgb(58, 152, 112);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"QPushButton#downloadButton, QPushButton#selectSearchButton, QPushButton#startSearchButton\n"
"{\n"
"    color: rgb(54, 54, 54);\n"
"    background-color: rgb(58, 152, 112);\n"
"}\n"
"\n"
"QPushButton#searchExitButton\n"
"{\n"
"color: rgb(58, 152, 112);\n"
"background-color: rgb(54, 54, 54);\n"
"}\n"
"\n"
"QLabel#errorLabel\n"
"{\n"
"    color: rgb(217, 174, 23);\n"
"}\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(searchDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.val5 = QtWidgets.QLineEdit(searchDialog)
        self.val5.setObjectName("val5")
        self.gridLayout.addWidget(self.val5, 7, 1, 1, 1)
        self.key4 = QtWidgets.QLineEdit(searchDialog)
        self.key4.setStyleSheet("")
        self.key4.setObjectName("key4")
        self.gridLayout.addWidget(self.key4, 6, 0, 1, 1)
        self.key1 = QtWidgets.QLineEdit(searchDialog)
        self.key1.setStyleSheet("")
        self.key1.setObjectName("key1")
        self.gridLayout.addWidget(self.key1, 3, 0, 1, 1)
        self.val4 = QtWidgets.QLineEdit(searchDialog)
        self.val4.setObjectName("val4")
        self.gridLayout.addWidget(self.val4, 6, 1, 1, 1)
        self.key5 = QtWidgets.QLineEdit(searchDialog)
        self.key5.setStyleSheet("")
        self.key5.setObjectName("key5")
        self.gridLayout.addWidget(self.key5, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(searchDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.val1 = QtWidgets.QLineEdit(searchDialog)
        self.val1.setObjectName("val1")
        self.gridLayout.addWidget(self.val1, 3, 1, 1, 1)
        self.key2 = QtWidgets.QLineEdit(searchDialog)
        self.key2.setStyleSheet("")
        self.key2.setObjectName("key2")
        self.gridLayout.addWidget(self.key2, 4, 0, 1, 1)
        self.val2 = QtWidgets.QLineEdit(searchDialog)
        self.val2.setObjectName("val2")
        self.gridLayout.addWidget(self.val2, 4, 1, 1, 1)
        self.key3 = QtWidgets.QLineEdit(searchDialog)
        self.key3.setStyleSheet("")
        self.key3.setText("")
        self.key3.setObjectName("key3")
        self.gridLayout.addWidget(self.key3, 5, 0, 1, 1)
        self.val3 = QtWidgets.QLineEdit(searchDialog)
        self.val3.setObjectName("val3")
        self.gridLayout.addWidget(self.val3, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(searchDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_2 = QtWidgets.QLabel(searchDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pathPattern = QtWidgets.QLineEdit(searchDialog)
        self.pathPattern.setStyleSheet("")
        self.pathPattern.setText("")
        self.pathPattern.setObjectName("pathPattern")
        self.verticalLayout_2.addWidget(self.pathPattern)
        self.label = QtWidgets.QLabel(searchDialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.objPattern = QtWidgets.QLineEdit(searchDialog)
        self.objPattern.setStyleSheet("")
        self.objPattern.setObjectName("objPattern")
        self.verticalLayout_2.addWidget(self.objPattern)
        self.label_5 = QtWidgets.QLabel(searchDialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.checksumPattern = QtWidgets.QLineEdit(searchDialog)
        self.checksumPattern.setStyleSheet("")
        self.checksumPattern.setText("")
        self.checksumPattern.setObjectName("checksumPattern")
        self.verticalLayout_2.addWidget(self.checksumPattern)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.startSearchButton = QtWidgets.QPushButton(searchDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.startSearchButton.setFont(font)
        self.startSearchButton.setStyleSheet("")
        self.startSearchButton.setDefault(True)
        self.startSearchButton.setObjectName("startSearchButton")
        self.verticalLayout_2.addWidget(self.startSearchButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(searchDialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.searchResultTable = QtWidgets.QTableWidget(searchDialog)
        self.searchResultTable.setStyleSheet("")
        self.searchResultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.searchResultTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.searchResultTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.searchResultTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.searchResultTable.setObjectName("searchResultTable")
        self.searchResultTable.setColumnCount(3)
        self.searchResultTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.searchResultTable)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectSearchButton = QtWidgets.QPushButton(searchDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.selectSearchButton.setFont(font)
        self.selectSearchButton.setStyleSheet("")
        self.selectSearchButton.setObjectName("selectSearchButton")
        self.horizontalLayout_2.addWidget(self.selectSearchButton)
        self.downloadButton = QtWidgets.QPushButton(searchDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("")
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout_2.addWidget(self.downloadButton)
        self.searchExitButton = QtWidgets.QPushButton(searchDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchExitButton.setFont(font)
        self.searchExitButton.setStyleSheet("")
        self.searchExitButton.setObjectName("searchExitButton")
        self.horizontalLayout_2.addWidget(self.searchExitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.errorLabel = QtWidgets.QLabel(searchDialog)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_2.addWidget(self.errorLabel)

        self.retranslateUi(searchDialog)
        QtCore.QMetaObject.connectSlotsByName(searchDialog)

    def retranslateUi(self, searchDialog):
        _translate = QtCore.QCoreApplication.translate
        searchDialog.setWindowTitle(_translate("searchDialog", "Dialog"))
        self.label_4.setText(_translate("searchDialog", "Value (optional)"))
        self.label_3.setText(_translate("searchDialog", "Key"))
        self.label_2.setText(_translate("searchDialog", "Collection name (wildcard \'%\')"))
        self.label.setText(_translate("searchDialog", "Object name (wildcard \'%\')"))
        self.label_5.setText(_translate("searchDialog", "Checksum (wildcard \'%\')"))
        self.startSearchButton.setText(_translate("searchDialog", "Search"))
        self.label_6.setText(_translate("searchDialog", "Results:"))
        item = self.searchResultTable.horizontalHeaderItem(0)
        item.setText(_translate("searchDialog", "Path"))
        item = self.searchResultTable.horizontalHeaderItem(1)
        item.setText(_translate("searchDialog", "Name"))
        item = self.searchResultTable.horizontalHeaderItem(2)
        item.setText(_translate("searchDialog", "Checksum"))
        self.selectSearchButton.setText(_translate("searchDialog", "Select and Close"))
        self.downloadButton.setText(_translate("searchDialog", "Download Selection"))
        self.searchExitButton.setText(_translate("searchDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchDialog = QtWidgets.QDialog()
    ui = Ui_searchDialog()
    ui.setupUi(searchDialog)
    searchDialog.show()
    sys.exit(app.exec())
