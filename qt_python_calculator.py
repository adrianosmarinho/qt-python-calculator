#main file

import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello            = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.button_labels    = ["Clear", "(", ")", "%", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", ".", "=", "/"] #5rows x 4columns
        self.number_of_rows   = 5 #number of rows of the buttons grid
        self.number_of_colums = 4 #number of columns of the buttons grid

        self.expression_label = QtWidgets.QLabel("0")
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

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
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))
        

    #updates the expression label, evaluates the expression if = is clicked
    def update_expression_label(self):
        sender = self.sender()
        #self.statusBar().showMessage(sender.text() + ' was pressed')
        self.text.setText(sender.text() + ' was pressed')
        if (sender.text() == "="):
            result = eval(self.expression_label.text())
            self.expression_label.setText(str(result))
        elif (sender.text() == "."):
            #TODO: Implement floating point numbers
            print("TODO: Im goning to treat float numbers properly")
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
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())