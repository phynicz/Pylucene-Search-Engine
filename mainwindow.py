import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import time


app = QtWidgets.QApplication(sys.argv)


class MyStream(QtCore.QObject):
    message = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

    def flush(self):
        pass

class Ui_RedaiSearch(QtWidgets.QWidget):
    def setupUi(self, RedaiSearch):
        RedaiSearch.setObjectName("RedaiSearch")
        RedaiSearch.resize(743, 377)
        RedaiSearch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(RedaiSearch)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 160, 91, 34))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pushButton.setObjectName("pushButton")

        self.search_query = QtWidgets.QLineEdit(self.centralwidget)
        self.search_query.setGeometry(QtCore.QRect(350, 110, 331, 32))
        self.search_query.setStyleSheet("color: rgb(0, 0, 0);")
        self.search_query.setObjectName("search_query")
        

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 101, 34))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 310, 91, 34))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 290, 230))
        self.textEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(1)

        
        RedaiSearch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RedaiSearch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 30))
        self.menubar.setObjectName("menubar")
        RedaiSearch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RedaiSearch)
        self.statusbar.setObjectName("statusbar")
        RedaiSearch.setStatusBar(self.statusbar)

        self.retranslateUi(RedaiSearch)
        QtCore.QMetaObject.connectSlotsByName(RedaiSearch)
  


    def retranslateUi(self, RedaiSearch):
        _translate = QtCore.QCoreApplication.translate
        RedaiSearch.setWindowTitle(_translate("RedaiSearch", "RedaiSearch"))
        self.pushButton.setText(_translate("RedaiSearch", "Search"))
        self.pushButton_2.setText(_translate("RedaiSearch", "Extract"))
        self.pushButton_2.clicked.connect(self.extracting)
        self.pushButton_3.setText(_translate("RedaiSearch", "Index"))
        self.pushButton_3.clicked.connect(self.IndexDocs)
        textvalue = self.search_query.text()
        self.pushButton.clicked.connect(lambda v=textvalue: self.searching(v))

     
                
        

    @QtCore.pyqtSlot()
    def extracting(self):
        cmd = "python extract.py"
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True) # +++
        while True:
            line = output.stdout.readline()
            line1 = output.stderr.readline()
            if line:
                print (line.rstrip())
            elif line1:
                print (line1.rstrip())
            else:
                break 
                   

             

    @QtCore.pyqtSlot()
    def IndexDocs(self):
        cmd = "python IndexFiles1.py text"
        output = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True) # +++
        while True:
            line = output.stdout.readline()
            line1 = output.stderr.readline()
            if line:
                print (line.rstrip())
            elif line1:
                print (line1.rstrip())
            else:
                break


    @QtCore.pyqtSlot()            
    def searching(self, textvalue):
        textvalue = self.search_query.text()
        out = 'search.txt'             #create a new file with filename and extension of .txt
        file = open(out, "w")             #open file in write mode
        file.write(textvalue)                    #write content of data to opened file
        file.close()
        cmd = "python SearchFiles.py"
        output = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)

        while True:
            line = output.stdout.readline()
            if line:
                print (line.rstrip())
            else:
                break             
        

    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(message)


if __name__ == "__main__":
    import sys
    RedaiSearch = QtWidgets.QMainWindow()
    ui = Ui_RedaiSearch()
    ui.setupUi(RedaiSearch)
    RedaiSearch.show()
    myStream = MyStream()
    myStream.message.connect(ui.on_myStream_message)
    sys.stdout = myStream
    sys.exit(app.exec_())
