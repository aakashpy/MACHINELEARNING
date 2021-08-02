from StartD import *
from Colsort import *
from Rowsort import *
from Fcol import *
from XYform import *
from showt import *
from GUI import *
import pandas as pd
import sys
import seaborn as sns
import collections
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix

class Open:
    def __init__(self):
        global df
        df=0
        ui.actionNew.triggered.connect(self.opendataset)
        ui.actionColumns.triggered.connect(lambda: ColForm.show())
        ui.actionRows.triggered.connect(lambda: RowForm.show())
        ui.actionExit.triggered.connect(MainWindow.close)
        ui.actionExit.triggered.connect(StartupDialog.close)
        ui.actionExit.triggered.connect(ColForm.close)
        ui.actionExit.triggered.connect(RowForm.close)
        ui.actionExit.triggered.connect(FForm.close)
        ui.actionExit.triggered.connect(TForm.close)
        ui.actionExit.triggered.connect(SForm.close)
        ui.Xlist.itemDoubleClicked.connect(self.Xaxis)
        ui.Ylist.itemDoubleClicked.connect(self.Yaxis)
        ui.Huelist.itemDoubleClicked.connect(self.Hueaxis)
        ui.Generate.clicked.connect(self.Graph)
        ui.ClearandClose.clicked.connect(self.cleargraph)
        ui.actionReset.triggered.connect(self.resettable)
        ui.COLbtn.clicked.connect(lambda: FForm.show())
        ui.encodebtn.clicked.connect(self.encode_dummies)
        ui.Done.clicked.connect(self.done)
        ui.XYtrain.clicked.connect(lambda: TForm.show())
        ui.XYtrain.clicked.connect(lambda: ui.Train.setEnabled(False))
        ui.Train.clicked.connect(self.train_model)
        ui.Predictbtn.clicked.connect(self.train_model)
        ui.Reset.clicked.connect(self.reset)
        ui.COLlist.itemDoubleClicked.connect(self.Rem_fcol)
        ui.showtable.clicked.connect(lambda: SForm.show())
        ui1.pushButton_2.clicked.connect(StartupDialog.close)
        ui1.pushButton.clicked.connect(self.opendataset)
        ui1.pushButton.clicked.connect(StartupDialog.close)
        ui2.listWidget.itemDoubleClicked.connect(self.showcol)
        ui2.listWidget_2.itemDoubleClicked.connect(self.removecol)
        ui2.Show.clicked.connect(self.readsortedcolumns)
        ui3.pushButton.clicked.connect(self.expand)
        ui3.pushButton_2.clicked.connect(self.Sort_per_Rows)
        ui3.pushButton_3.clicked.connect(self.Sort_cus_Rows)
        ui4.Fcollist.itemDoubleClicked.connect(self.Add_fcol)
        ui4.pushButton.clicked.connect(self.check)
        ui4.pushButton.clicked.connect(lambda: FForm.close())
        ui5.listWidget.itemDoubleClicked.connect(self.Xlist)
        ui5.Xtrainlist.itemDoubleClicked.connect(self.Alist)
        ui5.pushButton.clicked.connect(self.Apply)

    def opendataset(self):
        try:
            global name
            name = QtWidgets.QFileDialog.getOpenFileName(None, 'Open CSV', "*.csv")
            ui.Datatabs.setEnabled(True)
            ui.menubar.setEnabled(True)
            self.readdata(name[0])
            self.datadescribe()
        except:
            ui1.label.setText("Error occurred")
            ui1.pushButton.setEnabled(True)
            ui1.pushButton_2.setEnabled(True)
            StartupDialog.resize(414, 134)
            StartupDialog.show()

    def readdata(self, name):
        global data,col_list
        col_list=[]
        self.clear()
        ui.Datatable.clear()
        data = pd.read_csv(name)
        ui.Datatable.setColumnCount(len(data.columns))
        ui.Datatable.setRowCount(len(data.index))
        ui.Datasetname.setText(name)
        columns = data.columns
        for x in columns:
            ui.Xlist.addItem(x)
            ui.Ylist.addItem(x)
            ui.Huelist.addItem(x)
            ui2.listWidget.addItem(x)
            ui4.Fcollist.addItem(x)
        ui.Datatable.setHorizontalHeaderLabels(data.columns)
        self.reset()
        for i in range(len(data.index)):
            for j in range(len(data.columns)):
                ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.iat[i, j])))

        ui.encodebtn.setEnabled(False)
        ui.Done.setEnabled(False)
        ui.frame_3.setEnabled(False)

    def datadescribe(self):
        ui.DesciptionTable.setColumnCount(len(data.describe().columns))
        ui.DesciptionTable.setHorizontalHeaderLabels(data.describe().columns)
        describe = data.describe()
        for i in range(8):
            for j in range(len(data.describe().columns)):
                ui.DesciptionTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(describe.iat[i, j])))
        return 0

    def Xaxis(self, item):
        ui.Xplot.setText(item.text())

    def Yaxis(self, item):
        ui.Yplot.setText(item.text())

    def Hueaxis(self, item):
        ui.Hueplot.setText(item.text())

    def showcol(self, item):
        ui2.listWidget_2.addItem(item.text())
        ui2.listWidget.takeItem(ui2.listWidget.row(item))
        if ui2.listWidget_2.count() != 0:
            ui2.Show.setEnabled(True)

    def removecol(self, item):
        ui2.listWidget.addItem(item.text())
        ui2.listWidget_2.takeItem(ui2.listWidget_2.row(item))
        if ui2.listWidget_2.count() == 0:
            ui2.Show.setEnabled(False)

    def readsortedcolumns(self):
        global col_list
        col_list = []
        for i in range(ui2.listWidget_2.count()):
            x = ui2.listWidget_2.item(i)
            col_list.append(x.text())
        data = pd.read_csv(name[0], usecols=col_list)
        ui.Datatable.setColumnCount(len(col_list))
        ui.Datatable.setHorizontalHeaderLabels(data.columns)
        for i in range(len(data.index)):
            for j in range(len(data.columns)):
                ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.iat[i, j])))
        ui.Xlist.clear()
        ui.Ylist.clear()
        ui.Huelist.clear()
        for x in col_list:
            ui.Xlist.addItem(x)
            ui.Ylist.addItem(x)
            ui.Huelist.addItem(x)

    def expand(self):
        if ui3.pushButton.text() == "Show Advance Option":
            RowForm.resize(471, 463)
            ui3.pushButton.setText("Hide Advance Option")
            ui3.groupBox.setEnabled(False)
        else:
            RowForm.resize(471, 231)
            ui3.pushButton.setText("Show Advance Option")
            ui3.groupBox.setEnabled(True)

    def Sort_per_Rows(self):
        global datas, df
        df = 1
        datas = pd.read_csv(name[0])
        if ui3.radioButton25.isChecked():
            x = len(datas.index)
            x = int(0.25 * x)
            ui.Datatable.setRowCount(x)
            for i in range(x):
                for j in range(len(datas.columns)):
                    ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(datas.iat[i, j])))

        elif ui3.radioButton50.isChecked():
            x = len(datas.index)
            x = int(0.50 * x)
            ui.Datatable.setRowCount(x)
            for i in range(x):
                for j in range(len(datas.columns)):
                    ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(datas.iat[i, j])))

        elif ui3.radioButton75.isChecked():
            x = len(datas.index)
            x = int(0.75 * x)
            ui.Datatable.setRowCount(x)
            for i in range(x):
                for j in range(len(datas.columns)):
                    ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(datas.iat[i, j])))
        RowForm.close()

    def Sort_cus_Rows(self):
        global datas, df
        df = 1
        if ui3.radioButtonTop.isChecked():
            if ui3.lineEditTop.text().isdigit() and int(ui3.lineEditTop.text()) <= len(data.index):
                ui.Datatable.clear()
                x = int(ui3.lineEditTop.text())
                ui.Datatable.setRowCount(len(data.index) - x)
                ui.Datatable.setHorizontalHeaderLabels(data.columns)
                datas = pd.read_csv(name[0], skiprows=int(ui3.lineEditTop.text()), engine='python')
                for i in range(len(data.index) - x):
                    for j in range(len(data.columns)):
                        ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(datas.iat[i, j])))

        elif ui3.radioButtonBottom.isChecked():
            if ui3.lineEditBottom.text().isdigit() and int(ui3.lineEditBottom.text()) <= len(data.index):
                ui.Datatable.clear()
                x = int(ui3.lineEditBottom.text())
                ui.Datatable.setRowCount(len(data.index) - x)
                ui.Datatable.setHorizontalHeaderLabels(data.columns)
                datas = pd.read_csv(name[0], skipfooter=int(ui3.lineEditBottom.text()), engine='python')
                for i in range(len(data.index) - x):
                    for j in range(len(data.columns)):
                        ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(datas.iat[i, j])))

        elif ui3.radioButtonCus.isChecked():
            try:
                ui.Datatable.clear()
                skip = []
                x = list(ui3.lineEditCus.text())
                for i in x:
                    if i == ',':
                        continue
                    skip.append(int(i))
                ui.Datatable.setRowCount(len(data.index) - len(skip))
                ui.Datatable.setHorizontalHeaderLabels(data.columns)
                datas = pd.read_csv(name[0], skiprows=skip, engine='python')
                for i in range(len(data.index) - len(skip)):
                    for j in range(len(data.columns)):
                        ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(datas.iat[i, j])))
            except:
                pass
        RowForm.close()

    def resettable(self):
        global df
        df = 0
        self.clear()
        data = pd.read_csv(name[0])
        ui.Datatable.setColumnCount(len(data.columns))
        ui.Datatable.setRowCount(len(data.index))
        ui.Datatable.setHorizontalHeaderLabels(data.columns)
        for i in range(len(data.index)):
            for j in range(len(data.columns)):
                ui.Datatable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.iat[i, j])))
        for x in data.columns:
            ui.Xlist.addItem(x)
            ui.Ylist.addItem(x)
            ui.Huelist.addItem(x)
            ui2.listWidget.addItem(x)

    def Graph(self):
        if df == 0:
            dataf = data
        else:
            dataf = datas
        if ui.Countbtn.isChecked():
            if ui.Xplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=1)
                plt.figure(1)
                sns.countplot(x=ui.Xplot.text(), data=dataf)
                plt.show()
            if ui.Yplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=2)
                plt.figure(2)
                sns.countplot(y=ui.Yplot.text(), data=dataf)
                plt.show()
            if ui.Xplot.text() and ui.Hueplot.text():
                plt.close(fig=3)
                plt.figure(3)
                sns.countplot(x=ui.Xplot.text(), data=dataf, hue=ui.Hueplot.text())
                plt.show()
            if ui.Yplot.text() and ui.Hueplot.text():
                plt.close(fig=4)
                plt.figure(4)
                sns.countplot(y=ui.Yplot.text(), data=dataf, hue=ui.Hueplot.text())
                plt.show()
        if ui.Linebtn.isChecked():
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=5)
                plt.figure(5)
                sns.lineplot(x=ui.Xplot.text(), y=ui.Yplot.text(), data=dataf, marker="o", ci=None)
                plt.show()
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text():
                plt.close(fig=6)
                plt.figure(6)
                sns.lineplot(x=ui.Xplot.text(), y=ui.Yplot.text(), hue=ui.Hueplot.text(), data=dataf, marker="o",
                             ci=None)
                plt.show()
        if ui.Scatterbtn.isChecked():
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=9)
                plt.figure(9)
                sns.scatterplot(x=ui.Xplot.text(), y=ui.Yplot.text(), data=dataf, marker="o")
                plt.show()
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text():
                plt.close(fig=10)
                plt.figure(10)
                sns.scatterplot(x=ui.Xplot.text(), y=ui.Yplot.text(), hue=ui.Hueplot.text(), data=dataf,
                                marker="o")
                plt.show()
        if ui.Barbtn.isChecked():
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=11)
                plt.figure(11)
                sns.barplot(x=ui.Xplot.text(), y=ui.Yplot.text(), data=dataf)
                plt.show()
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text():
                plt.close(fig=12)
                plt.figure(12)
                sns.barplot(x=ui.Xplot.text(), y=ui.Yplot.text(), hue=ui.Hueplot.text(), data=dataf)
                plt.show()
        if ui.HBarbtn.isChecked():
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=13)
                plt.figure(13)
                sns.barplot(x=ui.Xplot.text(), y=ui.Yplot.text(), data=dataf, orient='h')
                plt.show()
            if ui.Xplot.text() and ui.Yplot.text() and ui.Hueplot.text():
                plt.close(fig=14)
                plt.figure(14)
                sns.barplot(x=ui.Xplot.text(), y=ui.Yplot.text(), hue=ui.Hueplot.text(), data=dataf, orient='h')
                plt.show()
        if ui.Histobtn.isChecked():
            if ui.Xplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=15)
                plt.figure(15)
                sns.histplot(dataf[ui.Xplot.text()])
                plt.show()
            if ui.Yplot.text() and ui.Hueplot.text() == "":
                plt.close(fig=16)
                plt.figure(16)
                sns.histplot(dataf[ui.Yplot.text()])
                plt.show()

    def cleargraph(self):
        ui.Xplot.clear()
        ui.Yplot.clear()
        ui.Ylist.clear()
        ui.Hueplot.clear()
        for x in data.columns:
            ui.Ylist.addItem(x)
        plt.close()

    def clear(self):
        ui.Xlist.clear()
        ui.Ylist.clear()
        ui.Huelist.clear()
        ui.Xplot.clear()
        ui.Yplot.clear()
        ui.Hueplot.clear()
        ui2.listWidget.clear()
        ui2.listWidget_2.clear()

    def Add_fcol(self, item):
        ui.COLlist.addItem(item.text())
        ui5.listWidget.addItem(item.text())
        ui5.Ytrainbox.addItem(item.text())
        ui4.Fcollist.takeItem(ui4.Fcollist.row(item))

    def Rem_fcol(self, item):
        ui4.Fcollist.addItem(item.text())
        ui.COLlist.takeItem(ui.COLlist.row(item))
        if ui.COLlist.count() == 0:
            ui.encodebtn.setEnabled(False)
            ui.Done.setEnabled(False)

    def check(self):
        if ui.COLlist.count() != -1:
            ui.encodebtn.setEnabled(True)
            ui.Done.setEnabled(True)
        else:
            ui.encodebtn.setEnabled(False)
            ui.Done.setEnabled(False)
        try:
            if ui.nanbtn.isChecked():
                self.nan()
            if ui.meanbtn.isChecked():
                self.mean()
        except:
            print("exception")

    def done(self):
        try:
            global Final_data
            x = data.columns
            y = new_data.columns
            if collections.Counter(x) == collections.Counter(y):
                ui5.Ytrainbox.clear()
                ui5.listWidget.clear()
                Final_data = new_data
                if ui4.Fcollist.count()!=0:
                    col=[]
                    for x in range(ui4.Fcollist.count()):
                        col.append(ui4.Fcollist.item(x).text())
                    Final_data = Final_data.drop(col, axis='columns')
                for x in range(ui.COLlist.count()):
                    ui5.listWidget.addItem(ui.COLlist.item(x).text())
                    ui5.Ytrainbox.addItem(ui.COLlist.item(x).text())
            else:
                ui5.Ytrainbox.clear()
                ui5.listWidget.clear()
                Final_data = new_data
                if ui4.Fcollist.count()!=0:
                    col=[]
                    for x in range(ui4.Fcollist.count()):
                        col.append(ui4.Fcollist.item(x).text())
                    Final_data = Final_data.drop(col, axis='columns')
                new_col = Final_data.columns
                for x in new_col:
                    ui5.listWidget.addItem(x)
                    ui5.Ytrainbox.addItem(x)
            ui5.Xtrainlist.clear()
            ui.frame_3.setEnabled(True)
            ui.linepercent.setEnabled(True)
            ui6.tableWidget.clear()
            ui6.tableWidget.setColumnCount(len(Final_data.columns))
            ui6.tableWidget.setRowCount(len(Final_data.index))
            ui6.tableWidget.setHorizontalHeaderLabels(Final_data.columns)
            for i in range(len(Final_data.index)):
                for j in range(len(Final_data.columns)):
                    ui6.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(Final_data.iat[i, j])))
            ui4.pushButton.setEnabled(True)
        except:
            pass

    def encode_dummies(self):
        global new_data
        try:
            txt = ui.lineEdit.text()
            if new_data[txt].dtype == 'object':
                dummies = pd.get_dummies(new_data[txt], drop_first='True')
                merge = pd.concat([new_data, dummies], axis='columns')
                new_data = merge.drop([ui.lineEdit.text()], axis='columns')
                ui.lineEdit.setText("")
        except:
            ui1.label.setText("Some Error Occured")
            StartupDialog.show()
            ui1.pushButton.hide()
            ui1.pushButton_2.hide()

    def nan(self):
        global new_data
        new_data = data.dropna()

    def mean(self):
        global new_data
        new_data = data
        columns = data.columns
        for x in columns:
            try:
                new_data[x] = new_data[x].fillna(new_data[x].mean())
            except:
                pass

    def Alist(self, item):
        ui5.listWidget.addItem(item.text())
        ui5.Xtrainlist.takeItem(ui5.Xtrainlist.row(item))
        if ui5.Xtrainlist.count() != 0:
            ui5.pushButton.setEnabled(True)
        else:
            ui5.pushButton.setEnabled(False)

    def Xlist(self, item):
        ui5.Xtrainlist.addItem(item.text())
        ui5.listWidget.takeItem(ui5.listWidget.row(item))

    def Apply(self):
        i = 0
        ui5.label.hide()
        ui.Train.setEnabled(False)
        if ui5.Xtrainlist.count() > 0:
            for x in range(ui5.Xtrainlist.count()):
                if ui5.Xtrainlist.item(x).text() == ui5.Ytrainbox.currentText():
                    ui5.label.show()
                    i = 1
            if i == 0:
                ui.Train.setEnabled(True)
                TForm.close()
            else:
                ui.Train.setEnabled(False)

    def train_model(self):
        try:
            percent = float(ui.linepercent.text())
            percent = 1 - (percent / 100)
            xlist = []
            ylist = [ui5.Ytrainbox.currentText()]
            for i in range(ui5.Xtrainlist.count()):
                xlist.append(ui5.Xtrainlist.item(i).text())
            x = Final_data[xlist]
            y = Final_data[ylist]
            if ui.comboBox.currentText()=="Support Vector Machine":
                try:###########################################################     Support Vector Machine Alogorithm
                    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=percent, random_state=0)
                    st_x = StandardScaler()
                    x_train = st_x.fit_transform(x_train)
                    x_test = st_x.transform(x_test)
                    classifier = SVC(kernel='linear', random_state=0)
                    classifier.fit(x_train, y_train)
                    y_pred = classifier.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    print(cm)
                    print(accuracy_score(y_test, y_pred))
                    ui.Accuracylcd.display(accuracy_score(y_test, y_pred) * 100)
                    ui.Reset.setEnabled(True)
                    ui.Predictbtn.setEnabled(True)
                    try:
                        if ui.pretext.text() != "":
                            x = ui.pretext.text().split()
                            for i in range(len(x)):
                                x[i] = float(x[i])
                            a = [x]
                            b = classifier.predict(a)
                            print(b[0])
                            ui.Result.setText(str(b[0]))
                    except:
                        ui1.label.setText("Enter parameters according to columns entered respectively")
                        ui.pretext.setText("")
                        StartupDialog.resize(550, 134)
                        StartupDialog.show()
                        ui1.pushButton.setEnabled(True)
                        ui1.pushButton_2.setEnabled(True)
                except:
                    ui1.label.setText("Model cannot be created")
                    StartupDialog.show()
                    ui1.pushButton.hide()
                    ui1.pushButton_2.hide()

            if ui.comboBox.currentText()=="Logistic Regression":
                try:###########################################################     Logistic Regression Alogorithm
                    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=percent, random_state=0)
                    classifier = LogisticRegression()
                    classifier.fit(x_train, y_train.values.ravel())
                    sc=classifier.score(x_train, y_train)
                    y_pred = classifier.predict(x_test)
                    cm = confusion_matrix(y_test, y_pred)
                    print(cm)
                    ui.Accuracylcd.display(sc * 100)
                    ui.Reset.setEnabled(True)
                    ui.Predictbtn.setEnabled(True)
                    try:
                        if ui.pretext.text()!="":
                            x = ui.pretext.text().split()
                            for i in range(len(x)):
                                x[i] = float(x[i])
                            a=[x]
                            b = classifier.predict(a)
                            print(b[0])
                            ui.Result.setText(str(b[0]))
                    except:
                        ui1.label.setText("Enter parameters according to columns entered respectively")
                        ui.pretext.setText("")
                        StartupDialog.resize(550, 134)
                        StartupDialog.show()
                        ui1.pushButton.hide()
                        ui1.pushButton_2.hide()
                except:
                    ui1.label.setText("Model cannot be created")
                    StartupDialog.show()
                    ui1.pushButton.hide()
                    ui1.pushButton_2.hide()

            if ui.comboBox.currentText() == "Linear Regression":
                try:  ###########################################################     Linear Regression Alogorithm
                    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=percent, random_state=0)
                    classifier = LinearRegression()
                    classifier.fit(x_train, y_train)
                    sc=classifier.score(x_train,y_train)
                    print(sc)
                    ui.Accuracylcd.display(sc * 100)
                    ui.Reset.setEnabled(True)
                    ui.Predictbtn.setEnabled(True)
                    try:
                        if ui.pretext.text() != "":
                            x = ui.pretext.text().split()
                            for i in range(len(x)):
                                x[i] = float(x[i])
                            a = [x]
                            b = classifier.predict(a)
                            print(b[0])
                            ui.Result.setText(str(b[0]))
                    except:
                        ui1.label.setText("Enter parameters according to columns entered respectively")
                        ui.pretext.setText("")
                        StartupDialog.resize(550, 134)
                        StartupDialog.show()
                        ui1.pushButton.hide()
                        ui1.pushButton_2.hide()
                except:
                    ui1.label.setText("Model cannot be created")
                    StartupDialog.show()
                    ui1.pushButton.hide()
                    ui1.pushButton_2.hide()
        except:
            pass

    def reset(self):
        ui.COLlist.clear()
        ui4.Fcollist.clear()
        ui5.Xtrainlist.clear()
        ui5.listWidget.clear()
        ui5.Ytrainbox.clear()
        ui.linepercent.setText("")
        ui.frame_3.setEnabled(False)
        ui.encodebtn.setEnabled(False)
        ui.Done.setEnabled(False)
        ui.Accuracylcd.display('0')
        ui.pretext.setText("")
        ui.Result.setText("")
        for x in data.columns:
            ui4.Fcollist.addItem(x)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    File = open("Diffnes.qss", 'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    StartupDialog = QtWidgets.QDialog()
    ui1 = Ui_StartupDialog()
    ui1.setupUi(StartupDialog)
    StartupDialog.show()
    ColForm = QtWidgets.QWidget()
    ui2 = Ui_FormC()
    ui2.setupUi(ColForm)
    RowForm = QtWidgets.QWidget()
    ui3 = Ui_FormR()
    ui3.setupUi(RowForm)
    FForm = QtWidgets.QWidget()
    ui4 = Ui_FormF()
    ui4.setupUi(FForm)
    TForm = QtWidgets.QWidget()
    ui5 = Ui_FormXY()
    ui5.setupUi(TForm)
    SForm = QtWidgets.QWidget()
    ui6 = Ui_FormS()
    ui6.setupUi(SForm)
    gui = Open()
    sys.exit(app.exec_())
