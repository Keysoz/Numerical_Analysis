import sys

from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QMessageBox, QWidget
)
from PyQt5.QtCore import (
    Qt, pyqtSlot, QPoint
)
from PyQt5.QtGui import (
    QMouseEvent, QPixmap, QIcon
)
from MainWindow import Ui_MainWindow
from textViewer import Ui_Form
from guess import Ui_guess
import numpy as np
import math

# from sympy  import *

fu = []


def gu(fu):
    poly = np.poly1d(fu)
    return poly


def f(x):
    poly = gu(fu)
    cul = poly(x)
    return cul


def g(x):
    return 1 / math.sqrt(1 + x)


def der(fu):
    poly = np.poly1d(fu)
    poly = poly.deriv()
    return poly


def gi(x):
    poly = der(fu)
    cul = poly(x)
    # print(cul )
    return cul


def bisection(xl, xu, e):
    step = 1
    my_write_file = open('methods/bisection.txt', 'a')
    my_write_file.write(
        '\n\n** BISECTION METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    condition = True
    old = 0
    xr = 0
    first_iteration = True
    first_iteration1 = True
    while condition:
        old = xr
        xr = (xl + xu) / 2

        if first_iteration:
            l = 0
            my_write_file = open('methods/bisection.txt', 'a')
            my_write_file.write((
                    'Iteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | '
                    'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
                        step, xl, f(xl), xu, f(xu), xr, f(xr), l)))
            my_write_file.close()

            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('methods/bisection.txt', 'a')
            my_write_file.write((
                    '\nIteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | xr = %0.6f | f(xr) = '
                    '%0.6f | error =%.2f\n' % (
                        step, xl, f(xl), xu, f(xu), xr, f(xr), l)))
            my_write_file.close()

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        step = step + 1
        if first_iteration1:
            condition = True
            first_iteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
    my_write_file = open('methods/bisection.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f=' % xr)
    my_write_file.close()


def false_position(xl, xu, e):
    step = 1
    my_write_file = open('methods/false_position.txt', 'a')
    my_write_file.write(
        '\n\n** FALSE POSITION METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    condition = True
    old = 0
    xr = 0
    first_iteration = True
    first_iteration1 = True
    while condition:
        old = xr
        xr = xu - ((xl - xu) * f(xu) / (f(xl) - f(xu)))

        if first_iteration:
            l = 0
            my_write_file = open('methods/false_position.txt', 'a')
            my_write_file.write((
                    'Iteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | '
                    'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
                        step, xl, f(xl), xu, f(xu), xr, f(xr), l)))
            my_write_file.close()

            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('methods/false_position.txt', 'a')
            my_write_file.write((
                    '\nIteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | xr = %0.6f | f(xr) = '
                    '%0.6f | error =%.2f\n' % (
                        step, xl, f(xl), xu, f(xu), xr, f(xr), l)))
            my_write_file.close()

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        step = step + 1
        if first_iteration1:
            condition = True
            first_iteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
    my_write_file = open('methods/false_position.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f=' % xr)
    my_write_file.close()


# def fixed_point(xl, e):
#     step = 1
#     my_write_file = open('methods/fixed_point.txt', 'a')
#     my_write_file.write('\n\n** Fixed Point METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
#     my_write_file.close()
#     condition = True
#     old = 0
#     xr = 0
#     first_iteration = True
#     first_iteration1 = True
#     while condition:
#         old = xr
#         xr = g(xl)
#
#         if first_iteration:
#             l = 0
#             my_write_file = open('methods/fixed_point.txt', 'a')
#             my_write_file.write((
#                     'Iteration %d | xl = %0.6f | f(xl) = %0.6f | '
#                     'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
#                         step, xl, f(xl),  xr, f(xr), l)))
#             my_write_file.close()
#
#             first_iteration = False
#         else:
#             l = abs((xr - old) / xr) * 100
#             my_write_file = open('methods/fixed_point.txt', 'a')
#             my_write_file.write((
#                     'Iteration %d | xl = %0.6f | f(xl) = %0.6f | '
#                     'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
#                         step, xl, f(xl), xr, f(xr), l)))
#             my_write_file.close()
#
#         xl = xr
#         step = step + 1
#         condition = abs(f(xr)) > e
#     my_write_file = open('methods/fixed_point.txt', 'a')
#     my_write_file.write('\nRequired Root is : %0.8f=' % xr)
#     my_write_file.close()
# def newtonRaphson(xl, e):
#     my_write_file = open('methods/newton.txt', 'a')
#     my_write_file.write(
#         '\n\n** Newton METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
#     my_write_file.close()
#     step = 1
#     flag = 1
#     old=0
#     xr=0
#     fristIteration = True
#     condition = True
#     while condition:
#         old = xr
#         if gi(xl) == 0:
#             print('Divide by zero error!')
#             break
#         xr = xl - (f(xl) / gi(xl))
#         if fristIteration == True:
#             l=0
#             my_write_file = open('methods/false_position.txt', 'a')
#             my_write_file.write((
#                     'Iteration %d | xl = %0.6f | f(xl) = %0.6f | gi(xl)= %0.6f |
#                     'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
#                         step, xl, f(xl),  gi(xl), xr, f(xr), l)))
#             my_write_file.close()
#         else:
#             l = abs((xr - old) / xr) * 100
#             my_write_file = open('methods/false_position.txt', 'a')
#             my_write_file.write((
#                     'Iteration %d | xl = %0.6f | f(xl) = %0.6f | gi(xl)= %0.6f |
# #                     'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
# #                         step, xl, f(xl),  gi(xl), xr, f(xr), l)))
#             my_write_file.close()
#         condition = abs(((xr - old) / xr) * 100) >= e
#         xl = xr
#         step = step + 1
#     if condition == False:
#         my_write_file = open('methods/false_position.txt', 'a')
#         my_write_file.write('\nRequired Root is : %0.8f=' % xr)
#         my_write_file.close()
#     else:
#         my_write_file = open('methods/false_position.txt', 'a')
#         my_write_file.write('\nNot Convergent.')
#         my_write_file.close()
# def secant(x0, x1, e):
#     step = 1
#     my_write_file = open('methods/bisection.txt', 'a')
#     my_write_file.write('\n\n** BISECTION METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
#     my_write_file.close()
#     condition = True
#     old = 0
#     xr = 0
#     first_iteration = True
#     first_iteration1 = True
#     while condition:
#         old = xr
#         xr = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
#
#         if first_iteration:
#             l = 0
#             my_write_file = open('methods/bisection.txt', 'a')
#             my_write_file.write((
#                     'Iteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | '
#                     'xr = %0.6f | f(xr) = %0.6f | error =%.2f\n' % (
#                         step, x0, f(x0), x1, f(x1), xr, f(xr), l)))
#             my_write_file.close()
#
#             first_iteration = False
#         else:
#             l = abs((xr - old) / xr) * 100
#             my_write_file = open('methods/bisection.txt', 'a')
#             my_write_file.write((
#                     '\nIteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | xr = %0.6f | f(xr) = '
#                     '%0.6f | error =%.2f\n' % (
#                         step, x0, f(x0), x1, f(x1), xr, f(xr), l)))
#             my_write_file.close()
#
#         x0 = x1
#         x1 = xr
#         step = step + 1
#         if first_iteration1:
#             condition = True
#             first_iteration1 = False
#         else:
#             condition = abs(((xr - old) / xr) * 100) >= e
#     my_write_file = open('methods/bisection.txt', 'a')
#     my_write_file.write('\nRequired Root is : %0.8f=' % xr)
#     my_write_file.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = None
        self.poly = None
        self._tracking = None
        self._startPos = None
        self._endPos = None
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.pow_list.setCurrentIndex(0)
        self.viewer = Viewer()
        self.viewer_false = Viewer_false()
        self.guess_el = guess_eli()
        self.default_val()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = True
            self._startPos = None
            self._endPos = False

    @pyqtSlot()
    def on_exit_btn_clicked(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowIcon(QIcon(r"imgs\question.png"))
        msgbox.setIconPixmap(QPixmap(r"imgs\question (1).png"))
        msgbox.setWindowTitle("E X I T !!!")
        msgbox.setText("Are you sure to E X I T ?")
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = msgbox.exec()
        if reply == QMessageBox.Yes:
            self.close()
        else:
            return

    def pow_custom_bisec(self):
        self.x9_widget.setHidden(False)
        self.x8_widget.setHidden(False)
        self.x7_widget.setHidden(False)
        self.x6_widget.setHidden(False)
        self.x5_widget.setHidden(False)
        self.x4_widget.setHidden(False)
        self.x3_widget.setHidden(False)
        self.x2_widget.setHidden(False)
        self.x1_widget.setHidden(False)

    def pow_custom_pos(self):
        self.x9_widget_2.setHidden(False)
        self.x8_widget_2.setHidden(False)
        self.x7_widget_2.setHidden(False)
        self.x6_widget_2.setHidden(False)
        self.x5_widget_2.setHidden(False)
        self.x4_widget_2.setHidden(False)
        self.x3_widget_2.setHidden(False)
        self.x2_widget_2.setHidden(False)
        self.x1_widget_2.setHidden(False)

    @pyqtSlot()
    def on_sub_btn_clicked(self):
        self.pow_custom_bisec()
        index = self.pow_list.currentText()
        if index == "8":
            self.x9_widget.setHidden(True)
        elif index == "7":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
        elif index == "6":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
        elif index == "5":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
        elif index == "4":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
        elif index == "3":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x4_widget.setHidden(True)
        elif index == "2":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x4_widget.setHidden(True)
            self.x3_widget.setHidden(True)
        elif index == "1":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x4_widget.setHidden(True)
            self.x3_widget.setHidden(True)
            self.x2_widget.setHidden(True)

    @pyqtSlot()
    def on_sub_btn_2_clicked(self):
        self.pow_custom_pos()
        index = self.pow_list_2.currentText()
        if index == "8":
            self.x9_widget_2.setHidden(True)
        elif index == "7":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
        elif index == "6":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
            self.x7_widget_2.setHidden(True)
        elif index == "5":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
            self.x7_widget_2.setHidden(True)
            self.x6_widget_2.setHidden(True)
        elif index == "4":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
            self.x7_widget_2.setHidden(True)
            self.x6_widget_2.setHidden(True)
            self.x5_widget_2.setHidden(True)
        elif index == "3":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
            self.x7_widget_2.setHidden(True)
            self.x6_widget_2.setHidden(True)
            self.x5_widget_2.setHidden(True)
            self.x4_widget_2.setHidden(True)
        elif index == "2":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
            self.x7_widget_2.setHidden(True)
            self.x6_widget_2.setHidden(True)
            self.x5_widget_2.setHidden(True)
            self.x4_widget_2.setHidden(True)
            self.x3_widget_2.setHidden(True)
        elif index == "1":
            self.x9_widget_2.setHidden(True)
            self.x8_widget_2.setHidden(True)
            self.x7_widget_2.setHidden(True)
            self.x6_widget_2.setHidden(True)
            self.x5_widget_2.setHidden(True)
            self.x4_widget_2.setHidden(True)
            self.x3_widget_2.setHidden(True)
            self.x2_widget_2.setHidden(True)

    def default_val(self):
        self.x0_edit.setText("0")
        self.x1_edit.setText("0")
        self.x2_edit.setText("0")
        self.x3_edit.setText("0")
        self.x4_edit.setText("0")
        self.x5_edit.setText("0")
        self.x6_edit.setText("0")
        self.x7_edit.setText("0")
        self.x8_edit.setText("0")
        self.x9_edit.setText("0")
        self.xl_edit.setText("0")
        self.xu_edit.setText("0")
        self.error_edit.setText("0")

    def message_error(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowIcon(QIcon(r"imgs\question.png"))
        msgbox.setIconPixmap(QPixmap(r"imgs\question (1).png"))
        msgbox.setWindowTitle("E R R O R!!!")
        msgbox.setText("Enter A Valid Values.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        reply = msgbox.exec()
        if reply == QMessageBox.Ok:
            return reply

    def on_calc_btn_clicked(self):
        power = int(self.pow_list.currentText())
        x0, x1, x2 = float(self.x0_edit.text()), float(self.x1_edit.text()), float(self.x2_edit.text())
        x3, x4, x5 = float(self.x3_edit.text()), float(self.x4_edit.text()), float(self.x5_edit.text())
        x6, x7, x8 = float(self.x6_edit.text()), float(self.x7_edit.text()), float(self.x8_edit.text())
        x9 = float(self.x9_edit.text())
        xl = float(self.xl_edit.text())
        xu = float(self.xu_edit.text())
        err = float(self.error_edit.text())
        my_list = [x9, x8, x7, x6, x5, x4, x3, x2, x1, x0]
        count = 10 - (power + 1)
        for num in range(count, 10):
            fu.append(my_list[num])
        if self.index == 0:
            if (f(xl) * f(xu)) < 0.0:
                my_write_file = open('methods/bisection.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                bisection(xl, xu, err)
                my_write_file = open('methods/bisection.txt', 'a')
                my_write_file.write(str(power))
                my_write_file.close()
                self.viewer.showing('methods/bisection.txt')
            else:
                self.message_error()
                print(xl, xu)

        elif self.index == 1:
            if (f(xl) * f(xu)) < 0.0:
                my_write_file = open('methods/false_position.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                false_position(xl, xu, err)
                my_write_file = open('methods/false_position.txt', 'a')
                my_write_file.write(str(power))
                my_write_file.close()
                self.viewer.showing('methods/false_position.txt')
            else:
                self.message_error()

        elif self.index == 2:
            pass

        elif self.index == 3:
            if not True:
                self.message_error()
            else:
                my_write_file = open('methods/newton.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                # new(xl, err)
                self.viewer.showing('methods/newton.txt')


        elif self.index == 4:
            pass

    # def on_guess_calc_clicked(self):
    #     x_0_0 = self.edit_00.text()
    #     x_0_1 = self.edit_01.text()
    #     x_0_2 = self.edit_02.text()
    #     x_0_3 = self.edit_03.text()
    #     x_1_0 = self.edit_10.text()
    #     x_1_1 = self.edit_11.text()
    #     x_1_2 = self.edit_12.text()
    #     x_1_3 = self.edit_13.text()
    #     x_2_0 = self.edit_20.text()
    #     x_2_1 = self.edit_21.text()
    #     x_2_2 = self.edit_22.text()
    #     x_2_3 = self.edit_23.text()
    #     x_3_0 = self.edit_30.text()
    #     x_3_1 = self.edit_31.text()
    #     x_3_2 = self.edit_32.text()
    #     x_3_3 = self.edit_33.text()
    #     self.guess_el.showing()

    def on_submit_btn_clicked(self):
        self.index = self.algo_box.currentIndex()
        if self.index == 0:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("Bisection Method")
        elif self.index == 1:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("False Position Method")
        elif self.index == 2:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("Fixed Point Method")
        elif self.index == 3:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("Newton Method")
        elif self.index == 4:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("Secant Method")
        else:
            self.stackedWidget.setCurrentIndex(2)


def main_window():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


class Viewer(QWidget):
    def __init__(self):
        super(Viewer, self).__init__()
        self.viewer = Ui_Form()
        self.viewer.setupUi(self)

    def showing(self, file):
        my_read_file = open(file, 'r')
        self.viewer.textBrowser.setPlainText(str(my_read_file.read()))
        self.show()
        my_read_file.close()


class Viewer_false(QWidget):
    def __init__(self):
        super(Viewer_false, self).__init__()
        self.viewer = Ui_Form()
        self.viewer.setupUi(self)

    def showing(self):
        my_read_file = open('methods/false_position.txt', 'r')
        self.viewer.textBrowser.setPlainText(str(my_read_file.read()))
        self.show()
        my_read_file.close()


class guess_eli(QWidget):
    def __init__(self):
        super(guess_eli, self).__init__()
        self.guess = Ui_guess()
        self.guess.setupUi(self)

    def showing(self):
        my_read_file_1 = open('methods/guess_1.txt', 'r')
        self.guess.matrix_editor.setPlainText(str(my_read_file_1.read()))
        my_read_file_2 = open('methods/guess_2.txt', 'r')
        self.guess.res_editor.setPlainText(str(my_read_file_2.read()))
        self.show()
        my_read_file_1.close()
        my_read_file_2.close()


if __name__ == "__main__":
    main_window()