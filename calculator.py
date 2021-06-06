from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.number_1 = QtWidgets.QPushButton(self.centralwidget)
        self.number_1.setGeometry(QtCore.QRect(10, 110, 51, 41))
        self.number_1.setObjectName("number_1")
        self.number_2 = QtWidgets.QPushButton(self.centralwidget)
        self.number_2.setGeometry(QtCore.QRect(80, 110, 51, 41))
        self.number_2.setObjectName("number_2")
        self.number_3 = QtWidgets.QPushButton(self.centralwidget)
        self.number_3.setGeometry(QtCore.QRect(150, 110, 51, 41))
        self.number_3.setObjectName("number_3")
        self.number_6 = QtWidgets.QPushButton(self.centralwidget)
        self.number_6.setGeometry(QtCore.QRect(150, 160, 51, 41))
        self.number_6.setObjectName("number_6")
        self.number_5 = QtWidgets.QPushButton(self.centralwidget)
        self.number_5.setGeometry(QtCore.QRect(80, 160, 51, 41))
        self.number_5.setObjectName("number_5")
        self.number_4 = QtWidgets.QPushButton(self.centralwidget)
        self.number_4.setGeometry(QtCore.QRect(10, 160, 51, 41))
        self.number_4.setObjectName("number_4")
        self.number_7 = QtWidgets.QPushButton(self.centralwidget)
        self.number_7.setGeometry(QtCore.QRect(10, 210, 51, 41))
        self.number_7.setObjectName("number_7")
        self.number_9 = QtWidgets.QPushButton(self.centralwidget)
        self.number_9.setGeometry(QtCore.QRect(150, 210, 51, 41))
        self.number_9.setObjectName("number_9")
        self.number_8 = QtWidgets.QPushButton(self.centralwidget)
        self.number_8.setGeometry(QtCore.QRect(80, 210, 51, 41))
        self.number_8.setObjectName("number_8")
        self.number_0 = QtWidgets.QPushButton(self.centralwidget)
        self.number_0.setGeometry(QtCore.QRect(80, 260, 51, 41))
        self.number_0.setObjectName("number_0")
        
        self.symbol_cls = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_cls.setGeometry(QtCore.QRect(210, 260, 81, 41))
        self.symbol_cls.setObjectName("symbol_equel")
        
        self.symbol_equel = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_equel.setGeometry(QtCore.QRect(150, 260, 51, 41))
        self.symbol_equel.setObjectName("symbol_equel")
        self.symbol_dot = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_dot.setGeometry(QtCore.QRect(210, 110, 81, 21))
        self.symbol_dot.setObjectName("symbol_dot")
        
        self.Ekran = QtWidgets.QLabel(self.centralwidget)
        self.Ekran.setGeometry(QtCore.QRect(10, 30, 281, 51))
        self.Ekran.setFrameShape(QtWidgets.QFrame.Box)
        self.Ekran.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Ekran.setObjectName("Ekran")

        self.symbol_divide = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_divide.setGeometry(QtCore.QRect(210, 230, 81, 21))
        self.symbol_divide.setObjectName("symbol_divide")
        self.symbol_minus = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_minus.setGeometry(QtCore.QRect(210, 170, 81, 21))
        self.symbol_minus.setObjectName("symbol_minus")
        self.symbol_plus = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_plus.setGeometry(QtCore.QRect(210, 140, 81, 21))
        self.symbol_plus.setObjectName("symbol_plus")
        self.symbol_smile2 = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_smile2.setGeometry(QtCore.QRect(10, 280, 51, 21))
        self.symbol_smile2.setObjectName("symbol_smile2")
        self.symbol_smile1 = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_smile1.setGeometry(QtCore.QRect(10, 260, 51, 21))
        self.symbol_smile1.setObjectName("symbol_smile1")
        self.symbol_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.symbol_multiply.setGeometry(QtCore.QRect(210, 200, 81, 21))
        self.symbol_multiply.setObjectName("symbol_multiply")

        self.is_equel = False

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.Ekran.setText(_translate("MainWindow", "0"))
        self.number_1.setText(_translate("MainWindow", "1"))
        self.number_2.setText(_translate("MainWindow", "2"))
        self.number_3.setText(_translate("MainWindow", "3"))
        self.number_6.setText(_translate("MainWindow", "6"))
        self.number_5.setText(_translate("MainWindow", "5"))
        self.number_4.setText(_translate("MainWindow", "4"))
        self.number_7.setText(_translate("MainWindow", "7"))
        self.number_9.setText(_translate("MainWindow", "9"))
        self.number_8.setText(_translate("MainWindow", "8"))
        self.number_0.setText(_translate("MainWindow", "0"))
        self.symbol_equel.setText(_translate("MainWindow", "="))
        self.symbol_cls.setText(_translate("MainWindow", "C"))
        self.symbol_dot.setText(_translate("MainWindow", "."))
        self.symbol_divide.setText(_translate("MainWindow", "/"))
        self.symbol_minus.setText(_translate("MainWindow", "-"))
        self.symbol_plus.setText(_translate("MainWindow", "+"))
        self.symbol_smile2.setText(_translate("MainWindow", ")"))
        self.symbol_smile1.setText(_translate("MainWindow", "("))
        self.symbol_multiply.setText(_translate("MainWindow", "*"))

    def add_functions(self):
        self.number_0.clicked.connect(lambda: self.write_number(self.number_0.text()))
        self.number_1.clicked.connect(lambda: self.write_number(self.number_1.text()))
        self.number_2.clicked.connect(lambda: self.write_number(self.number_2.text()))
        self.number_3.clicked.connect(lambda: self.write_number(self.number_3.text()))
        self.number_4.clicked.connect(lambda: self.write_number(self.number_4.text()))
        self.number_5.clicked.connect(lambda: self.write_number(self.number_5.text()))
        self.number_6.clicked.connect(lambda: self.write_number(self.number_6.text()))
        self.number_7.clicked.connect(lambda: self.write_number(self.number_7.text()))
        self.number_8.clicked.connect(lambda: self.write_number(self.number_8.text()))
        self.number_9.clicked.connect(lambda: self.write_number(self.number_9.text()))
        self.symbol_divide.clicked.connect(lambda: self.write_number(self.symbol_divide.text()))
        self.symbol_multiply.clicked.connect(lambda: self.write_number(self.symbol_multiply.text()))
        self.symbol_minus.clicked.connect(lambda: self.write_number(self.symbol_minus.text()))
        self.symbol_plus.clicked.connect(lambda: self.write_number(self.symbol_plus.text()))
        self.symbol_dot.clicked.connect(lambda: self.write_number(self.symbol_dot.text()))
        self.symbol_smile1.clicked.connect(lambda: self.write_number(self.symbol_smile1.text()))
        self.symbol_smile2.clicked.connect(lambda: self.write_number(self.symbol_smile2.text()))
        
        
        self.symbol_cls.clicked.connect(self.clear_screen)

        self.symbol_equel.clicked.connect(self.results)

    def write_number(self, number):
        if self.Ekran.text() == "0" or self.is_equel:
            self.Ekran.setText(number)
            self.is_equel = False

        else:
            self.Ekran.setText(self.Ekran.text() + number)
        

    def results(self):
        try:
            if not self.is_equel:
                res = eval(self.Ekran.text())
                self.Ekran.setText(str(res))
                self.is_equel = True
            else:
                error = QMessageBox()
                error.setWindowTitle('Error')
                error.setText('Zachem dva raza tykaesh?')
                error.setIcon(QMessageBox.Warning)

                error.exec()
        except (SyntaxError, ZeroDivisionError):
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('Malo kto mozhet tak delat')
            error.setIcon(QMessageBox.Warning)

            error.exec()


    def clear_screen(self):
        return self.Ekran.setText("0")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
