# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColSort.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormC(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(478, 373)
        Form.setMinimumSize(QtCore.QSize(241, 373))
        Form.setMaximumSize(QtCore.QSize(478, 373))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/ML.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.ListofColumns = QtWidgets.QLabel(Form)
        self.ListofColumns.setGeometry(QtCore.QRect(40, 9, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        self.ListofColumns.setFont(font)
        self.ListofColumns.setAlignment(QtCore.Qt.AlignCenter)
        self.ListofColumns.setObjectName("ListofColumns")
        self.Columnstodisplay = QtWidgets.QLabel(Form)
        self.Columnstodisplay.setGeometry(QtCore.QRect(276, 9, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        self.Columnstodisplay.setFont(font)
        self.Columnstodisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.Columnstodisplay.setObjectName("Columnstodisplay")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(9, 34, 227, 301))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(242, 34, 227, 301))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.Show = QtWidgets.QPushButton(Form)
        self.Show.setEnabled(False)
        self.Show.setGeometry(QtCore.QRect(201, 341, 75, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Show.sizePolicy().hasHeightForWidth())
        self.Show.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.Show.setFont(font)
        self.Show.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Show.setObjectName("Show")

        self.retranslateUi(Form)
        self.Show.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Column Sort"))
        self.ListofColumns.setText(_translate("Form", "List of Columns"))
        self.Columnstodisplay.setText(_translate("Form", "Columns to display"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Show.setText(_translate("Form", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormC()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
