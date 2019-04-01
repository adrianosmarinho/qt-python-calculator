#main file

import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_labels    = ["Clear", "(", ")", "%", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", ".", "=", "/"] #5rows x 4columns
        self.number_of_rows   = 5 #number of rows of the buttons grid
        self.number_of_colums = 4 #number of columns of the buttons grid

        self.expression_label = QtWidgets.QLabel("0")

        #initializingng the buttons
        self.button_grid = QtWidgets.QGridLayout()
        #TODO: Make the buttons a list of buttons
        for i in range(5):
            for j in range(4):
                index = (i*self.number_of_colums + j)
                current_button = QtWidgets.QPushButton(self.button_labels[index])
                current_button.clicked.connect(self.update_expression_label)
                self.button_grid.addWidget(current_button, i, j)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.expression_label)
        self.layout.addLayout(self.button_grid)
        self.setLayout(self.layout)

        #flags
        self.equals_was_pressed = False # controls when to clear the expression_label

    #updates the expression label, evaluates the expression if = is clicked
    def update_expression_label(self):

        if (self.equals_was_pressed == True):
            self.equals_was_pressed = False
            self.expression_label.setText("") # cleans the label after getting a result

        sender = self.sender()
        if (sender.text() == "="):
            result = eval(self.expression_label.text())
            self.expression_label.setText(str(result))

            #sets the flag to True
            self.equals_was_pressed = True

        elif (sender.text() == "."):
            self.expression_label.setText(self.expression_label.text() + sender.text())
        elif (sender.text() == "Clear"):
            self.expression_label.setText("")
        else:
            if (self.expression_label.text() == "0"):
                self.expression_label.setText(sender.text())
            else:
                self.expression_label.setText(self.expression_label.text() + sender.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Calculator()
    widget.setWindowTitle("Simple Calculator")
    widget.setWindowIcon(QtGui.QIcon("imgs/calculator.png"))
    widget.resize(640, 480)
    widget.show()

    sys.exit(app.exec_())