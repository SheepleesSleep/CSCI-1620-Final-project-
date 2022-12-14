# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Area_Calculator(object):
    def setupUi(self, Area_Calculator):
        Area_Calculator.setObjectName("Area_Calculator")
        Area_Calculator.resize(400, 400)
        Area_Calculator.setMinimumSize(QtCore.QSize(400, 400))
        Area_Calculator.setMaximumSize(QtCore.QSize(400, 400))
        self.button_circle = QtWidgets.QPushButton(Area_Calculator)
        self.button_circle.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.button_circle.setObjectName("button_circle")
        self.button_rectangle = QtWidgets.QPushButton(Area_Calculator)
        self.button_rectangle.setGeometry(QtCore.QRect(200, 30, 75, 23))
        self.button_rectangle.setObjectName("button_rectangle")
        self.button_square = QtWidgets.QPushButton(Area_Calculator)
        self.button_square.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.button_square.setObjectName("button_square")
        self.button_triangle = QtWidgets.QPushButton(Area_Calculator)
        self.button_triangle.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.button_triangle.setObjectName("button_triangle")
        self.input1 = QtWidgets.QPlainTextEdit(Area_Calculator)
        self.input1.setEnabled(False)
        self.input1.setGeometry(QtCore.QRect(110, 70, 104, 21))
        self.input1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input1.setObjectName("input1")
        self.input2 = QtWidgets.QPlainTextEdit(Area_Calculator)
        self.input2.setEnabled(False)
        self.input2.setGeometry(QtCore.QRect(110, 100, 104, 21))
        self.input2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input2.setObjectName("input2")
        self.top_label = QtWidgets.QLabel(Area_Calculator)
        self.top_label.setEnabled(False)
        self.top_label.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.top_label.setObjectName("top_label")
        self.bottom_label = QtWidgets.QLabel(Area_Calculator)
        self.bottom_label.setEnabled(False)
        self.bottom_label.setGeometry(QtCore.QRect(30, 100, 47, 16))
        self.bottom_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_label.setObjectName("bottom_label")
        self.label_info = QtWidgets.QLabel(Area_Calculator)
        self.label_info.setGeometry(QtCore.QRect(30, 140, 171, 31))
        self.label_info.setObjectName("label_info")
        self.calc = QtWidgets.QPushButton(Area_Calculator)
        self.calc.setEnabled(False)
        self.calc.setGeometry(QtCore.QRect(150, 180, 75, 23))
        self.calc.setObjectName("calc")

        self.retranslateUi(Area_Calculator)
        QtCore.QMetaObject.connectSlotsByName(Area_Calculator)

    def retranslateUi(self, Area_Calculator):
        _translate = QtCore.QCoreApplication.translate
        Area_Calculator.setWindowTitle(_translate("Area_Calculator", "Area calculator"))
        self.button_circle.setText(_translate("Area_Calculator", "Circle"))
        self.button_rectangle.setText(_translate("Area_Calculator", "Rectangle"))
        self.button_square.setText(_translate("Area_Calculator", "Square"))
        self.button_triangle.setText(_translate("Area_Calculator", "Triangle"))
        self.top_label.setText(_translate("Area_Calculator", "Select"))
        self.bottom_label.setText(_translate("Area_Calculator", "Shape"))
        self.label_info.setText(_translate("Area_Calculator", "Please select a shape."))
        self.calc.setText(_translate("Area_Calculator", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Area_Calculator = QtWidgets.QDialog()
    ui = Ui_Area_Calculator()
    ui.setupUi(Area_Calculator)
    Area_Calculator.show()
    sys.exit(app.exec_())
