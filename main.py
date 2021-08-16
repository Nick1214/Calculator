import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_plus_minus.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_plus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equals.clicked.connect(self.equals_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_divide.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)

        self.pushButton_clear.clicked.connect(self.clear_label)

    def digit_pressed(self):
        button = self.sender()
        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked()  # !!!!!!
             or self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked()) and (
                not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), ".15g")
            self.userIsTypingSecondNumber = True
        if ("." in self.label.text()) and (button.text() == "."):
            self.label.setText(self.label.text())
        else:
            if (("." in self.label.text()) and (button.text() == "0")):
                newLabel = format(self.label.text() + button.text(), ".15")
            else:
                newLabel = format(float(self.label.text() + button.text()), '.15g')
        self.label.setText(newLabel)

    def decimal_pressed(self):
        self.label.setText(self.label.text() + self.pushButton_decimal.text())

    def unary_operation_pressed(self):
        button = self.sender()
        labelNumber = float(self.label.text())
        if button.text() == "+/-":
            labelNumber = labelNumber * -1
        else:  # If button.text() == "%"
            labelNumber = labelNumber * 0.01
        newLabel = format(labelNumber, ".15g")
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()
        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def equals_pressed(self):
        secondNum = float(self.label.text())
        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)
        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)
        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)
        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_label(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.label.setText("0")


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()