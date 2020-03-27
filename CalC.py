# CalC is a simple python calculator consisting of basic arithmetic operations like addition, subtraction,
# multiplication, division and the unary operator. More scientific operators like the exponential and trignometric functions
# are yet to be added. The GUI was created with the help of PyQt5 Designer tool.
# 
# Date Created : 19th December 2019

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    #UI setup and parameters
    
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 649)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(143, 143, 143);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"background-color: rgb(185, 185, 185);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.b_1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_1.setGeometry(QtCore.QRect(30, 239, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_1.setFont(font)
        self.b_1.setObjectName("b_1")
        self.b_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_2.setGeometry(QtCore.QRect(130, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_2.setFont(font)
        self.b_2.setObjectName("b_2")
        self.b_3 = QtWidgets.QPushButton(self.centralwidget)
        self.b_3.setGeometry(QtCore.QRect(230, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_3.setFont(font)
        self.b_3.setObjectName("b_3")
        self.b_4 = QtWidgets.QPushButton(self.centralwidget)
        self.b_4.setGeometry(QtCore.QRect(30, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_4.setFont(font)
        self.b_4.setObjectName("b_4")
        self.b_5 = QtWidgets.QPushButton(self.centralwidget)
        self.b_5.setGeometry(QtCore.QRect(130, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_5.setFont(font)
        self.b_5.setObjectName("b_5")
        self.b_6 = QtWidgets.QPushButton(self.centralwidget)
        self.b_6.setGeometry(QtCore.QRect(230, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_6.setFont(font)
        self.b_6.setObjectName("b_6")
        self.b_7 = QtWidgets.QPushButton(self.centralwidget)
        self.b_7.setGeometry(QtCore.QRect(30, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_7.setFont(font)
        self.b_7.setObjectName("b_7")
        self.b_8 = QtWidgets.QPushButton(self.centralwidget)
        self.b_8.setGeometry(QtCore.QRect(130, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_8.setFont(font)
        self.b_8.setObjectName("b_8")
        self.b_9 = QtWidgets.QPushButton(self.centralwidget)
        self.b_9.setGeometry(QtCore.QRect(230, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_9.setFont(font)
        self.b_9.setObjectName("b_9")
        self.b_0 = QtWidgets.QPushButton(self.centralwidget)
        self.b_0.setGeometry(QtCore.QRect(30, 510, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_0.setFont(font)
        self.b_0.setObjectName("b_0")
        self.b_equal = QtWidgets.QPushButton(self.centralwidget)
        self.b_equal.setGeometry(QtCore.QRect(130, 510, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_equal.setFont(font)
        self.b_equal.setObjectName("b_equal")
        self.b_add = QtWidgets.QPushButton(self.centralwidget)
        self.b_add.setGeometry(QtCore.QRect(330, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_add.setFont(font)
        self.b_add.setObjectName("b_add")
        self.b_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.b_subtract.setGeometry(QtCore.QRect(330, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_subtract.setFont(font)
        self.b_subtract.setObjectName("b_subtract")
        self.b_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.b_multiply.setGeometry(QtCore.QRect(330, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_multiply.setFont(font)
        self.b_multiply.setObjectName("b_multiply")
        self.b_divide = QtWidgets.QPushButton(self.centralwidget)
        self.b_divide.setGeometry(QtCore.QRect(330, 510, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_divide.setFont(font)
        self.b_divide.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_divide.setObjectName("b_divide")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 371, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: rgb(213, 213, 213)")
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.b_clear = QtWidgets.QPushButton(self.centralwidget)
        self.b_clear.setGeometry(QtCore.QRect(30, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_clear.setFont(font)
        self.b_clear.setStyleSheet("QPushButton{\n"
"background-color: rgb(185, 185, 185);\n"
"}")
        self.b_clear.setObjectName("b_clear")
        self.b_del = QtWidgets.QPushButton(self.centralwidget)
        self.b_del.setGeometry(QtCore.QRect(330, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_del.setFont(font)
        self.b_del.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_del.setObjectName("b_del")
        self.b_unary = QtWidgets.QPushButton(self.centralwidget)
        self.b_unary.setGeometry(QtCore.QRect(230, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_unary.setFont(font)
        self.b_unary.setObjectName("b_unary")
        self.b_dot = QtWidgets.QPushButton(self.centralwidget)
        self.b_dot.setGeometry(QtCore.QRect(130, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b_dot.setFont(font)
        self.b_dot.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_dot.setObjectName("b_dot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 26))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuThemes = QtWidgets.QMenu(self.menuView)
        self.menuThemes.setObjectName("menuThemes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSimple = QtWidgets.QAction(MainWindow)
        self.actionSimple.setObjectName("actionSimple")
        self.actionNoir = QtWidgets.QAction(MainWindow)
        self.actionNoir.setObjectName("actionNoir")
        self.actionBright = QtWidgets.QAction(MainWindow)
        self.actionBright.setObjectName("actionBright")
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuThemes.addAction(self.actionSimple)
        self.menuThemes.addAction(self.actionNoir)
        self.menuThemes.addAction(self.actionBright)
        self.menuView.addAction(self.menuThemes.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Decimal, operational and unary checkers
        
        self.dec=1
        self.oper=1
        self.un=1
        self.cpy="23"

        #Connecting buttons to back-end functions

        self.actionCopy.triggered.connect(lambda: self.cpyf())
        self.actionPaste.triggered.connect(lambda: self.pastef())
        self.actionNoir.triggered.connect(lambda: self.noire())
        self.actionSimple.triggered.connect(lambda: self.simples())
        self.actionBright.triggered.connect(lambda: self.brights())

        self.b_0.clicked.connect(self.digit)
        self.b_1.clicked.connect(self.digit)
        self.b_2.clicked.connect(self.digit)
        self.b_3.clicked.connect(self.digit)
        self.b_4.clicked.connect(self.digit)
        self.b_5.clicked.connect(self.digit)
        self.b_6.clicked.connect(self.digit)
        self.b_7.clicked.connect(self.digit)
        self.b_8.clicked.connect(self.digit)
        self.b_9.clicked.connect(self.digit)
        self.b_clear.clicked.connect(self.erase)
        self.b_unary.clicked.connect(self.negate)
        self.b_add.clicked.connect(self.operation)
        self.b_subtract.clicked.connect(self.operation)
        self.b_multiply.clicked.connect(self.operation)
        self.b_divide.clicked.connect(self.operation)
        self.b_del.clicked.connect(self.delete)
        self.b_dot.clicked.connect(self.decimal)
        self.b_equal.clicked.connect(self.solve)

    # Color Schemes of Calculator (Simple, Noir or Bright)

    def brights(self):
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.b_dot.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_add.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_subtract.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_clear.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_del.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_multiply.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_divide.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.b_unary.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")

    def simples(self):
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(143, 143, 143);\n"
"}\n"
"")
        self.centralwidget.setStyleSheet("QPushButton{\n"
"background-color: rgb(185, 185, 185);\n"
"}")
        self.b_del.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_unary.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_add.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_subtract.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_multiply.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_divide.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_clear.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.b_dot.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.label_1.setStyleSheet("background-color: rgb(213, 213, 213)")
        

    def noire(self):
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.centralwidget.setStyleSheet("QPushButton{\n"
"background-color: rgb(185, 185, 185);\n"
"}")
        self.b_add.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_subtract.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_multiply.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_divide.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_dot.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_del.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_unary.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.b_clear.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        self.label_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")


    # Calculator Back-End Functions
        
    def cpyf(self):
        self.cpy=self.label_1.text()

    def pastef(self):
        self.label_1.setText(self.label_1.text()+self.cpy)
    
    def delete(self):
        s=self.label_1.text()
        if (len(s)!=0):
            self.label_1.setText(s[0:len(s)-1])
            if (s[len(s)-1]=="+" or s[len(s)-1]=="-" or s[len(s)-1]=="x" or s[len(s)-1]=="/"):
                self.oper=1
            elif s[len(s)-1]==".":
                self.dec=1

    def solve(self):
        try:
            s=self.label_1.text()
            s=s.replace("x","*")
            x=eval(s)
            if x==int(x):
                self.label_1.setText(str(int(x)))
                self.dec=1
            else:
                self.label_1.setText(str(round(x,10)))
                self.dec=0
        except ZeroDivisionError:
            self.label_1.setText("Error :-(")
        except SyntaxError:
            self.label_1.setText("Error :-(")
        self.un=1
            

    def operation(self):
        button=self.MainWindow.sender()
        if (self.label_1.text()=="%" and self.oper==1):
            self.label_1.setText(str(100*int(self.label.text())))
        elif (self.oper==1):
            self.label_1.setText(self.label_1.text()+button.text())
            self.oper=0
            self.dec=1
            self.un=0
        else:
            pass
    def decimal(self):
        button=self.MainWindow.sender()
        if (self.dec==1):
            self.label_1.setText(self.label_1.text()+button.text())
            self.dec=0
        else:
            pass

    def negate(self):
        if (self.un==1):
            x=(-1)*float(self.label_1.text())
            if x==int(x):
                x=int(x)
            self.label_1.setText(str(x))

    def erase(self):
        self.label_1.setText('0')
        self.dec=1
        self.oper=1
        self.un=1

    def digit(self):
        button=self.MainWindow.sender()
        if (self.label_1.text()=='0' or self.label_1.text()=="Error :-("):
            self.label_1.setText(button.text())
        else:
            self.label_1.setText(self.label_1.text()+button.text())
        self.oper=1

    # Re-translating UI

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.b_1.setText(_translate("MainWindow", "1"))
        self.b_2.setText(_translate("MainWindow", "2"))
        self.b_3.setText(_translate("MainWindow", "3"))
        self.b_4.setText(_translate("MainWindow", "4"))
        self.b_5.setText(_translate("MainWindow", "5"))
        self.b_6.setText(_translate("MainWindow", "6"))
        self.b_7.setText(_translate("MainWindow", "7"))
        self.b_8.setText(_translate("MainWindow", "8"))
        self.b_9.setText(_translate("MainWindow", "9"))
        self.b_0.setText(_translate("MainWindow", "0"))
        self.b_equal.setText(_translate("MainWindow", "="))
        self.b_add.setText(_translate("MainWindow", "+"))
        self.b_subtract.setText(_translate("MainWindow", "-"))
        self.b_multiply.setText(_translate("MainWindow", "x"))
        self.b_divide.setText(_translate("MainWindow", "/"))
        self.label_1.setText(_translate("MainWindow", "0"))
        self.b_clear.setText(_translate("MainWindow", "C"))
        self.b_del.setText(_translate("MainWindow", "DEL"))
        self.b_unary.setText(_translate("MainWindow", "+/-"))
        self.b_dot.setText(_translate("MainWindow", "."))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSimple.setText(_translate("MainWindow", "Simple"))
        self.actionNoir.setText(_translate("MainWindow", "Noir"))
        self.actionBright.setText(_translate("MainWindow", "Bright"))

# Main Window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
