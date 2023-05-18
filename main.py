import sys
import numpy as np
import math
from sympy import *
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
from methods import (
    gaussElimination, gaussGordan, cramerRule,
    gaussEliminationPartial, luDecomposition,
    luDecompositionPartial
)

fu = []


def gu():
    poly_gu = np.poly1d(fu)
    return poly_gu


def f(x):
    poly_f = gu()
    cul = poly_f(x)
    return cul


def g(x):
    return 1 / math.sqrt(1 + x)


def der():
    poly_der = np.poly1d(fu)
    poly_der = poly_der.deriv()
    return poly_der


def gi(x):
    poly_gi = der()
    cul = poly_gi(x)
    return cul


def bisection(xl, xu, e):
    step = 1
    my_write_file = open('files/bisection.txt', 'a')
    my_write_file.write(
        '\n\n** BISECTION METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    condition = True
    xr = 0
    first_iteration = True
    first_iteration1 = True
    while condition:
        old = xr
        xr = (xl + xu) / 2

        if first_iteration:
            l = 0
            my_write_file = open('files/bisection.txt', 'a')
            my_write_file.write((
                'Iteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | '
                'xr = %0.6f | f(xr) = %0.6f | error =%.2f' % (
                    step, xl, f(xl), xu, f(xu), xr, f(xr), l)) + "%\n")
            my_write_file.close()

            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('files/bisection.txt', 'a')
            my_write_file.write((
                '\nIteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | xr = %0.6f | f(xr) = '
                '%0.6f | error =%.2f' % (
                    step, xl, f(xl), xu, f(xu), xr, f(xr), l)) + "%\n")
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
    my_write_file = open('files/bisection.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f' % xr)
    my_write_file.close()


def false_position(xl, xu, e):
    step = 1
    my_write_file = open('files/false_position.txt', 'a')
    my_write_file.write(
        '\n\n** FALSE POSITION METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    condition = True
    xr = 0
    first_iteration = True
    while condition:
        old = xr
        xr = xu - ((xl - xu) * f(xu) / (f(xl) - f(xu)))

        if first_iteration:
            l = 0
            my_write_file = open('files/false_position.txt', 'a')
            my_write_file.write((
                'Iteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | '
                'xr = %0.6f | f(xr) = %0.6f | error =%.2f' % (
                    step, xl, f(xl), xu, f(xu), xr, f(xr), l)) + "%\n")
            my_write_file.close()

            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('files/false_position.txt', 'a')
            my_write_file.write((
                '\nIteration %d | xl = %0.6f | f(xl) = %0.6f | xu = %0.6f | f(xu) = %0.6f | '
                'xr = %0.6f | f(xr) = %0.6f | error =%.2f' % (
                    step, xl, f(xl), xu, f(xu), xr, f(xr), l)) + "%\n")
            my_write_file.close()
        condition = abs(((xr - old) / xr) * 100) >= e
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        step = step + 1
    my_write_file = open('files/false_position.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f' % xr)
    my_write_file.close()


def fixed_point(xl, e):
    xr = 0
    my_write_file = open('files/fixed_point.txt', 'a')
    my_write_file.write(
        '\n\n** FIXED POINT METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    step = 1
    condition = True
    first_iteration = True
    first_iteration1 = True
    while condition:
        old = xr
        xr = g(xl)
        if first_iteration:
            l = 0
            my_write_file = open('files/fixed_point.txt', 'a')
            my_write_file.write((
                'Iteration-%d | xr = %0.6f | f(xr) = %0.6f  | error %0.6f' % (
                    step, xr, f(xr), l)) + "%\n")
            my_write_file.close()

            first_iteration = False
        else:
            l = abs(xr-old)/xr*100
            my_write_file = open('files/fixed_point.txt', 'a')
            my_write_file.write((
                'Iteration-%d | xr = %0.6f | f(xr) = %0.6f  | error %0.6f' % (
                    step, xr, f(xr), l)) + "%\n")
            my_write_file.close()
        xl = xr
        step = step + 1
        if first_iteration1:
            condition = True
            first_iteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e

    my_write_file = open('files/fixed_point.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f' % xr)
    my_write_file.close()


def newton_raphson(xl, e):
    my_write_file = open('files/newton.txt', 'a')
    my_write_file.write(
        '\n\n** NEWTON METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    step = 1
    xr = 0
    first_iteration = True
    condition = True
    while condition:
        old = xr
        if gi(xl) == 0:
            my_write_file = open('files/newton.txt', 'a')
            my_write_file.write('Divide by zero error!')
            my_write_file.close()
            break
        xr = xl - (f(xl) / gi(xl))
        if first_iteration:
            l = 0
            my_write_file = open('files/newton.txt', 'a')
            my_write_file.write((
                'Iteration %d | xl = %0.6f | f(xl) = %0.6f | f`(xl)= %0.6f | x1 = %0.6f | f(x1) = %0.6f'
                ' error =%.2f' % (
                    step, xl, f(xl), gi(xl), xr, f(xr), l)) + "%\n")
            my_write_file.close()
            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('files/newton.txt', 'a')
            my_write_file.write((
                'Iteration %d | xl = %0.6f | f(xl) = %0.6f | f`(xl)= %0.6f | x1 = %0.6f | f(x1) = %0.6f'
                ' error =%.2f' % (
                    step, xl, f(xl), gi(xl), xr, f(xr), l)) + "%\n")
            my_write_file.close()
        condition = abs(((xr - old) / xr) * 100) >= e
        xl = xr
        step = step + 1
    if not condition:
        my_write_file = open('files/newton.txt', 'a')
        my_write_file.write('\nRequired Root is : %0.8f' % xr)
        my_write_file.close()
    else:
        my_write_file = open('files/newton.txt', 'a')
        my_write_file.write('\nNot Convergent.')
        my_write_file.close()


def secant(x0, x1, e):
    my_write_file = open('files/secant.txt', 'a')
    my_write_file.write(
        '\n\n** SECANT METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    step = 1
    condition = True
    xr = 0
    first_iteration = True
    first_iteration1 = True
    while condition:
        old = xr
        xr = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))

        if first_iteration:
            l = 0
            my_write_file = open('files/secant.txt', 'a')
            my_write_file.write((
                'Iteration %d | x0 = %0.6f | f(x0) = %0.6f | x1 = %0.6f | f(x1) = %0.6f | '
                'xr = %0.6f | f(xr) = %0.6f | error =%.2f' % (
                    step, x0, f(x0), x1, f(x1), xr, f(xr), l)) + "%\n")
            my_write_file.close()

            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('files/secant.txt', 'a')
            my_write_file.write((
                'Iteration %d | x0 = %0.6f | f(x0) = %0.6f | x1 = %0.6f | f(x1) = %0.6f | '
                'xr = %0.6f | f(xr) = %0.6f | error =%.2f' % (
                    step, x0, f(x0), x1, f(x1), xr, f(xr), l)) + "%\n")
            my_write_file.close()

        x0 = x1
        x1 = xr
        step = step + 1
        if first_iteration1:
            condition = True
            first_iteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
    my_write_file = open('files/secant.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f' % xr)
    my_write_file.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon("imgs/loggo_1.png"))
        self.setWindowIconText("Numerical Analysis")
        self.setWindowTitle("Numerical Analysis Calculator")
        self.index = None
        self._tracking = None
        self._startPos = None
        self._endPos = None
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.pow_list.setCurrentIndex(0)
        self.default_val()
        self.tab_order()
        self.viewer = Viewer()
        self.guess_el = GuessEli()
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

    def pow_custom_bisection(self):
        self.x9_widget.setHidden(False)
        self.x8_widget.setHidden(False)
        self.x7_widget.setHidden(False)
        self.x6_widget.setHidden(False)
        self.x5_widget.setHidden(False)
        self.x4_widget.setHidden(False)
        self.x3_widget.setHidden(False)
        self.x2_widget.setHidden(False)
        self.x1_widget.setHidden(False)

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
        msgbox.setMinimumSize(600, 400)
        msgbox.setWindowIcon(QIcon(r"imgs\question.png"))
        msgbox.setIconPixmap(QPixmap(r"imgs\question (1).png"))
        msgbox.setWindowTitle("E R R O R!!!")
        msgbox.setText("The Method Has No Solution")
        msgbox.setStandardButtons(QMessageBox.Ok)
        reply = msgbox.exec()
        if reply == QMessageBox.Ok:
            msgbox.close()

    def empty_error(self):
        msgbox_2 = QMessageBox(self)
        msgbox_2.setMinimumSize(600, 400)
        msgbox_2.setWindowIcon(QIcon(r"imgs\question.png"))
        msgbox_2.setIconPixmap(QPixmap(r"imgs\question (1).png"))
        msgbox_2.setWindowTitle("E R R O R!!!")
        msgbox_2.setText("Enter All Values!")
        msgbox_2.setStandardButtons(QMessageBox.Ok)
        reply = msgbox_2.exec()
        if reply == QMessageBox.Ok:
            msgbox_2.close()
    def no_value(self):
        if self.x0_edit.text() == "" or self.x1_edit.text() == "" or self.x2_edit.text() == "" or self.x3_edit.text() == "" \
                or self.x4_edit.text() == "" or self.x5_edit.text() == "" or self.x6_edit.text() == "" or self.x7_edit.text() == "" \
                or self.x8_edit.text() == "" or self.x9_edit.text() == "" or self.xl_edit.text() == "" or self.xu_edit.text() == "" \
                or self.error_edit.text() == "":
            return True
        else:
            return False

    def empty_gauss(self):
        if self.edit_00.text() == "" or self.edit_01.text() == "" or self.edit_02.text() == "" or self.edit_03.text() == "" \
                or self.edit_10.text() == "" or self.edit_11.text() == "" or self.edit_12.text() == "" or self.edit_13.text() == "" \
                or self.edit_20.text() == "" or self.edit_21.text() == "" or self.edit_22.text() == "" or self.edit_23.text() == "":
            return True
        else:
            return False

    def clear_val(self):
        self.x9_edit.clear()
        self.x8_edit.clear()
        self.x7_edit.clear()
        self.x6_edit.clear()
        self.x5_edit.clear()
        self.x4_edit.clear()
        self.x3_edit.clear()
        self.x2_edit.clear()
        self.x1_edit.clear()
        self.x0_edit.clear()
        self.xl_edit.clear()
        self.xu_edit.clear()
        self.error_edit.clear()

    def reset_boxes(self):
        self.edit_00.clear()
        self.edit_01.clear()
        self.edit_02.clear()
        self.edit_03.clear()
        self.edit_10.clear()
        self.edit_11.clear()
        self.edit_12.clear()
        self.edit_13.clear()
        self.edit_20.clear()
        self.edit_21.clear()
        self.edit_22.clear()
        self.edit_23.clear()

    def tab_order(self):
        self.setTabOrder(self.x9_edit, self.x8_edit)
        self.setTabOrder(self.x8_edit, self.x7_edit)
        self.setTabOrder(self.x7_edit, self.x6_edit)
        self.setTabOrder(self.x6_edit, self.x5_edit)
        self.setTabOrder(self.x5_edit, self.x4_edit)
        self.setTabOrder(self.x4_edit, self.x3_edit)
        self.setTabOrder(self.x3_edit, self.x2_edit)
        self.setTabOrder(self.x2_edit, self.x1_edit)
        self.setTabOrder(self.x1_edit, self.x0_edit)
        self.setTabOrder(self.x0_edit, self.xl_edit)
        self.setTabOrder(self.xl_edit, self.xu_edit)
        self.setTabOrder(self.xu_edit, self.error_edit)
        self.setTabOrder(self.edit_00, self.edit_01)
        self.setTabOrder(self.edit_01, self.edit_02)
        self.setTabOrder(self.edit_02, self.edit_03)
        self.setTabOrder(self.edit_03, self.edit_10)
        self.setTabOrder(self.edit_10, self.edit_11)
        self.setTabOrder(self.edit_11, self.edit_12)
        self.setTabOrder(self.edit_12, self.edit_13)
        self.setTabOrder(self.edit_13, self.edit_20)
        self.setTabOrder(self.edit_20, self.edit_21)
        self.setTabOrder(self.edit_21, self.edit_22)
        self.setTabOrder(self.edit_22, self.edit_23)

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

    def on_sub_btn_clicked(self):
        self.pow_custom_bisection()
        index = self.pow_list.currentText()
        if index == "8":
            self.x9_widget.setHidden(True)
            self.x9_edit.setText('0')
        elif index == "7":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
        elif index == "6":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
            self.x7_edit.setText('0')
        elif index == "5":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
            self.x7_edit.setText('0')
            self.x6_edit.setText('0')
        elif index == "4":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
            self.x7_edit.setText('0')
            self.x6_edit.setText('0')
            self.x5_edit.setText('0')
        elif index == "3":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x4_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
            self.x7_edit.setText('0')
            self.x6_edit.setText('0')
            self.x5_edit.setText('0')
            self.x4_edit.setText('0')
        elif index == "2":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x4_widget.setHidden(True)
            self.x3_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
            self.x7_edit.setText('0')
            self.x6_edit.setText('0')
            self.x5_edit.setText('0')
            self.x4_edit.setText('0')
            self.x3_edit.setText('0')
        elif index == "1":
            self.x9_widget.setHidden(True)
            self.x8_widget.setHidden(True)
            self.x7_widget.setHidden(True)
            self.x6_widget.setHidden(True)
            self.x5_widget.setHidden(True)
            self.x4_widget.setHidden(True)
            self.x3_widget.setHidden(True)
            self.x2_widget.setHidden(True)
            self.x9_edit.setText('0')
            self.x8_edit.setText('0')
            self.x7_edit.setText('0')
            self.x6_edit.setText('0')
            self.x5_edit.setText('0')
            self.x4_edit.setText('0')
            self.x3_edit.setText('0')
            self.x2_edit.setText('0')

    def on_back_btn_clicked(self):
        self.clear_val()
        self.stackedWidget.setCurrentIndex(0)

    def on_back_btn_2_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_calc_btn_clicked(self):
        global fu
        check = self.no_value()
        if check:
            self.empty_error()
            return
        else:
            power = int(self.pow_list.currentText())
            x0, x1, x2 = float(self.x0_edit.text()), float(
                self.x1_edit.text()), float(self.x2_edit.text())
            x3, x4, x5 = float(self.x3_edit.text()), float(
                self.x4_edit.text()), float(self.x5_edit.text())
            x6, x7, x8 = float(self.x6_edit.text()), float(
                self.x7_edit.text()), float(self.x8_edit.text())
            x9 = float(self.x9_edit.text())
            xl = float(self.xl_edit.text())
            xu = float(self.xu_edit.text())
            err = float(self.error_edit.text())
            if power == 9:
                fu = [x9, x8, x7, x6, x5, x4, x3, x2, x1, x0]
            elif power == 8:
                fu = [x8, x7, x6, x5, x4, x3, x2, x1, x0]
            elif power == 7:
                fu = [x7, x6, x5, x4, x3, x2, x1, x0]
            elif power == 6:
                fu = [x6, x5, x4, x3, x2, x1, x0]
            elif power == 5:
                fu = [x5, x4, x3, x2, x1, x0]
            elif power == 4:
                fu = [x4, x3, x2, x1, x0]
            elif power == 3:
                fu = [x3, x2, x1, x0]
            elif power == 2:
                fu = [x2, x1, x0]
            else:
                fu = [x1, x0]
            if self.index == 0:
                my_write_file = open('files/bisection.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                if (f(xl) * f(xu)) < 0.0:
                    bisection(xl, xu, err)
                    self.viewer.showing('files/bisection.txt')
                else:
                    self.message_error()
                    return
                my_write_file = open('files/bisection.txt', 'w')
                my_write_file.write("")
                my_write_file.close()

            elif self.index == 1:
                my_write_file = open('files/false_position.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                if f(xl) * f(xu) < 0.0:
                    false_position(xl, xu, err)
                    self.viewer.showing('files/false_position.txt')
                else:
                    self.message_error()
                    return
                my_write_file = open('files/false_position.txt', 'w')
                my_write_file.write("")
                my_write_file.close()
            elif self.index == 2:
                my_write_file = open('files/fixed_point.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                fixed_point(xl, err)
                self.viewer.showing('files/fixed_point.txt')
                my_write_file = open('files/fixed_point.txt', 'w')
                my_write_file.write("")
                my_write_file.close()

            elif self.index == 3:
                my_write_file = open('files/newton.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                newton_raphson(xl, err)
                self.viewer.showing('files/newton.txt')
                my_write_file = open('files/newton.txt', 'w')
                my_write_file.write("")
                my_write_file.close()

            elif self.index == 4:
                my_write_file = open('files/secant.txt', 'w')
                my_write_file.write(str(np.poly1d(fu)))
                my_write_file.close()
                secant(xl, xu, err)
                self.viewer.showing('files/secant.txt')
                my_write_file = open('files/secant.txt', 'w')
                my_write_file.write("")
                my_write_file.close()

    def on_guess_calc_clicked(self):
        check = self.empty_gauss()
        if check:
            self.empty_error()
        else:
            x00, x01, x02, x03 = float(self.edit_00.text()), float(
                self.edit_01.text()), float(self.edit_02.text()), float(self.edit_03.text())
            x10, x11, x12, x13 = float(self.edit_10.text()), float(
                self.edit_11.text()), float(self.edit_12.text()), float(self.edit_13.text())
            x20, x21, x22, x23 = float(self.edit_20.text()), float(
                self.edit_21.text()), float(self.edit_22.text()), float(self.edit_23.text())
            my_list_2 = [[x00, x01, x02, x03],
                         [x10, x11, x12, x13],
                         [x20, x21, x22, x23]]
            if self.index == 5:
                gaussElimination.gauss_elimination(my_list_2)
                self.guess_el.showing('files/guess_1.txt', 'files/guess_2.txt')
            elif self.index == 6:
                gaussEliminationPartial.gauss_partial(my_list_2)
                self.guess_el.cramer_showing(
                    'files/gauss_partial_1.txt', 'files/gauss_partial_2.txt', 'files/gauss_partial_3.txt')
            elif self.index == 7:
                gaussGordan.gauss_gordan(my_list_2)
                self.guess_el.showing(
                    'files/gordan_1.txt', 'files/gordan_2.txt')
            elif self.index == 8:
                luDecomposition.lu_method(my_list_2)
                self.guess_el.cramer_showing(
                    'files/lu_1.txt', 'files/lu_2.txt', 'files/lu_3.txt')
            elif self.index == 9:
                luDecompositionPartial.lu_partial(my_list_2)
                self.guess_el.cramer_showing(
                    'files/lu_p_1.txt', 'files/lu_p_2.txt', 'files/lu_p_3.txt')
            elif self.index == 10:
                cramerRule.cramer(my_list_2)
                self.guess_el.cramer_showing(
                    'files/cramer_1.txt', 'files/cramer_2.txt', 'files/cramer_3.txt')

    def on_submit_btn_clicked(self):
        self.pow_list.setCurrentIndex(0)
        self.clear_val()
        self.reset_boxes()
        self.pow_custom_bisection()
        self.index = self.algo_box.currentIndex()
        self.xu_widget.setHidden(False)
        if self.index == 0:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("Bisection Method")
        elif self.index == 1:
            self.stackedWidget.setCurrentIndex(1)
            self.title_lbl.setText("False Position Method")
        elif self.index == 2:
            self.stackedWidget.setCurrentIndex(1)
            self.xu_widget.setHidden(True)
            self.xu_edit.setText('0')
            self.xl_lbl.setText("Enter The Number OF (x_0) Variable")
            self.title_lbl.setText("Fixed Point Method")
        elif self.index == 3:
            self.stackedWidget.setCurrentIndex(1)
            self.xu_widget.setHidden(True)
            self.xu_edit.setText('0')
            self.xl_lbl.setText("Enter The Number OF (x_0) Variable")
            self.title_lbl.setText("Newton Method")
        elif self.index == 4:
            self.stackedWidget.setCurrentIndex(1)
            self.xl_lbl.setText("Enter The Number OF (x_1) Variable")
            self.xu_lbl_2.setText("Enter The Number OF (x_0) Variable")
            self.title_lbl.setText("Secant Method")
        else:
            self.stackedWidget.setCurrentIndex(2)
            self.guess_el.hide_icons()
            if self.index == 5:
                self.label_2.setText("\tGauss Elimination")
                self.guess_el.guess_condition_4()
                self.guess_el.guess_condition_5()
            elif self.index == 6:
                self.label_2.setText(" Gauss Elimination With P")
                self.guess_el.guess_condition_1()
                self.guess_el.guess_condition_2()
                self.guess_el.guess_condition_3()
                self.guess_el.guess_condition_4()
                self.guess_el.guess_condition_5()
            elif self.index == 8:
                self.label_2.setText("\tLU Decomposition")
                self.guess_el.guess_condition_3()
                self.guess_el.guess_condition_2()
                self.guess_el.guess_condition_1()
            elif self.index == 9:
                self.label_2.setText(" LU Decomposition With P")
                self.guess_el.lu_condition_2()
                self.guess_el.lu_condition_1()
                self.guess_el.guess_condition_1()
                self.guess_el.guess_condition_2()
                self.guess_el.guess_condition_3()
                self.guess_el.guess_condition_4()
                self.guess_el.guess_condition_5()
            elif self.index == 10:
                self.label_2.setText("\tCramer's Rule")
                self.guess_el.guess_condition_3()
            else:
                self.label_2.setText("\tGauss Gordan")
                self.guess_el.hide_icons()


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
        self.setWindowIcon(QIcon("imgs/loggo_1.png"))
        self.setWindowIconText("Results Page")
        self.setWindowTitle("Results Page")

    def showing(self, file):
        my_read_file = open(file, 'r')
        self.viewer.textBrowser.setPlainText(str(my_read_file.read()))
        self.show()
        my_read_file.close()


class GuessEli(QWidget):
    def __init__(self):
        super(GuessEli, self).__init__()
        self.guess = Ui_guess()
        self.guess.setupUi(self)
        self.hide_icons()
        self.setWindowIcon(QIcon("imgs/loggo_1.png"))
        self.setWindowIconText("Results Page")
        self.setWindowTitle("Results Page")

    def showing(self, file1, file2):
        my_read_file_1 = open(file1, 'r')
        self.guess.l_editor.setPlainText(str(my_read_file_1.read()))
        my_read_file_2 = open(file2, 'r')
        self.guess.res_editor.setPlainText(str(my_read_file_2.read()))
        self.show()
        my_read_file_1.close()
        my_read_file_2.close()

    def cramer_showing(self, file1, file2, file3):
        my_read_file_1 = open(file1, 'r')
        self.guess.l_editor.setPlainText(str(my_read_file_1.read()))
        my_read_file_2 = open(file2, 'r')
        self.guess.r_editor.setPlainText(str(my_read_file_2.read()))
        my_read_file_3 = open(file3, 'r')
        self.guess.res_editor.setPlainText(str(my_read_file_3.read()))
        self.show()
        my_read_file_1.close()
        my_read_file_2.close()
        my_read_file_3.close()

    def hide_icons(self):
        self.guess.lb_lbl_2.setHidden(True)
        self.guess.rb_lbl_2.setHidden(True)
        self.guess.lt_lbl_2.setHidden(True)
        self.guess.rt_lbl_2.setHidden(True)
        self.guess.r_editor.setHidden(True)
        self.guess.lb_lbl.setHidden(True)
        self.guess.rb_lbl.setHidden(True)

    def lu_condition_1(self):
        self.guess.lb_lbl_2.setHidden(False)

    def lu_condition_2(self):
        self.guess.rb_lbl_2.setHidden(False)

    def guess_condition_1(self):
        self.guess.lt_lbl_2.setHidden(False)

    def guess_condition_2(self):
        self.guess.rt_lbl_2.setHidden(False)

    def guess_condition_3(self):
        self.guess.r_editor.setHidden(False)

    def guess_condition_4(self):
        self.guess.lb_lbl.setHidden(False)

    def guess_condition_5(self):
        self.guess.rb_lbl.setHidden(False)


if __name__ == "__main__":
    try:
        main_window()
    except RuntimeError:
        print("Some RunTime Errors have been happened!!!")
