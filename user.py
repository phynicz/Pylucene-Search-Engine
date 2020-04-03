from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("RedaiSearch")
        Search.resize(743, 377)
        Search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit = QtWidgets.QLineEdit(Search)
        self.lineEdit.setGeometry(QtCore.QRect(250, 161, 241, 31))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Search)
        self.pushButton.setGeometry(QtCore.QRect(320, 210, 101, 34))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("RedaiSearch", "RedaiSearch"))
        self.pushButton.setText(_translate("Search", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QDialog()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())
