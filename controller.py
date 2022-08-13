from PyQt5.QtWidgets import*
from area import *
from view import Ui_Area_Calculator



class Controller(QMainWindow, Ui_Area_Calculator):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__shape = 5
        self.__second = False
        self.button_circle.clicked.connect(self.circle_click)
        self.button_square.clicked.connect(self.square_click)
        self.button_rectangle.clicked.connect(self.rectangle_click)
        self.button_triangle.clicked.connect(self.triangle_click)
       
       
    def calculate(self):
        match self.__shape:
            case 0:
                self.label_info.setText("circle") 
            case 1:
                self.label_info.setText("square")
            case 2:
                self.label_info.setText("rectangle")
            case 3:
                self.label_info.setText("triangle")


    def circle_click(self):
        self.__shape = 0
        self.top_label.setEnabled(True)
        self.top_label.setText("Radius")
        self.input1.setEnabled(True)
        self.input2.setEnabled(False)
        self.bottom_label.setText("")
        self.label_info.setText("Enter Radius")
        self.calc.setEnabled(True)
        self.calc.clicked.connect(self.calculate)
        
    def square_click(self):
        self.__shape = 1
        self.top_label.setEnabled(True)
        self.top_label.setText("Length")
        self.input1.setEnabled(True)
        self.input2.setEnabled(False)
        self.bottom_label.setText("")
        self.label_info.setText("Enter Length")
        self.calc.setEnabled(True)
        self.calc.clicked.connect(self.calculate)
           
    def rectangle_click(self):
        self.__shape = 2
        self.top_label.setEnabled(True)
        self.top_label.setText("Length")
        self.bottom_label.setEnabled(True)
        self.bottom_label.setText("Width")
        self.input1.setEnabled(True)
        self.input2.setEnabled(True)
        self.label_info.setText("Enter Length & width")
        self.calc.setEnabled(True)
        self.calc.clicked.connect(self.calculate)
       
    def triangle_click(self): 
        self.__shape = 3
        self.top_label.setEnabled(True)
        self.top_label.setText("Height")
        self.bottom_label.setEnabled(True)
        self.bottom_label.setText("Base")
        self.input1.setEnabled(True)
        self.input2.setEnabled(True)
        self.label_info.setText("Enter Height & Base")
        self.calc.setEnabled(True)
        self.calc.clicked.connect(self.calculate)