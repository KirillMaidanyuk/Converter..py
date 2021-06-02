import sys
from cmath import isfinite
from math import copysign, fabs, floor, modf

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator, QDoubleValidator
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtWidgets, QtCore


class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"Converter")
        MainWindow.resize(800, 631)
        self.setWindowTitle("Converter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 60, 801, 101))
        font = QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 150, 651, 61))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_2.setFont(font1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(570, 170, 73, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 210, 791, 81))
        self.comboBox_2 = QComboBox(self.centralwidget)
        list = [str(i) for i in range(1, 33)]
        self.comboBox_2.addItems(list)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(570, 240, 73, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 350, 161, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 360, 221, 31))
        self.lineEdit.setMaxLength(33)
        self.translate = QPushButton(self.centralwidget)
        self.translate.setObjectName(u"translate")
        self.translate.setGeometry(QRect(560, 360, 171, 31))
        self.translate.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 430, 161, 31))
        self.label_5.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 430, 221, 31))
        self.lineEdit_2.setReadOnly(True)
        self.spravka = QPushButton(self.centralwidget)
        self.spravka.setObjectName(u"spravka")
        self.spravka.setGeometry(QRect(740, 10, 51, 41))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.spravka.setFont(font3)
        self.print_solution = QPushButton(self.centralwidget)
        self.print_solution.setObjectName(u"print_solution")
        self.print_solution.setGeometry(QRect(560, 430, 171, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.lineEdit.setValidator(QDoubleValidator(0.99, 99.99, 12))
        QMetaObject.connectSlotsByName(MainWindow)
        self.translate.clicked.connect(self.translat)
        self.print_solution.clicked.connect(self.new_window)
        self.spravka.clicked.connect(self.sprav)
        self.solution = ''


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Converter", u"Converter", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u0434\u0440\u043e\u0431\u043d\u044b\u0445 \u0447\u0438\u0441\u0435\u043b \u0438\u0437 10\u0441\u0441 \u0432 2\u0441\u0441 (\u0438 \u043d\u0430\u043e\u0431\u043e\u0440\u043e\u0442):",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0441 \u0432 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0447\u0438\u0441\u043b\u043e:",
                                                        None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2 cc", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"10 cc", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"*\u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430 \u0432 2\u0441\u0441 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c \n"
                                                        " (\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0446\u0438\u0444\u0440 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439)",
                                                        None))

        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e: ",
                                                        None))
        self.translate.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.spravka.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.print_solution.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0445\u043e\u0434 \u0440\u0435\u0448\u0435\u043d\u0438\u044f",
                                                               None))


    def translat(self):
        ss = self.comboBox.currentText()
        n = self.lineEdit.text()
        if ',' in n:
            n = n.replace(',', '.')
        n = float(n)
        k = int(self.comboBox_2.currentText())
        if ss == '2 cc':
            self.float_to_bin(n, k)
        else:
            self.bin_to_float(n)

    def new_window(self):
        if len(self.solution) == 0:
            messageBox = QMessageBox.critical(self, self.tr("Ошибка!"),
                                                 self.tr("Вы не ввели число!"),
                                                 QMessageBox.Ok)
        else:
            messageBox = QMessageBox.information(self, self.tr("Результат"),
                                          self.tr(self.solution),
                                          QMessageBox.Ok)

    def sprav(self):
        messageBox = QMessageBox.information(self, self.tr("Справка"),
                                             self.tr("Разработчики: Майданюк Кирилл, Кулагина Лина, группа ПИ-19б \n\n"
                                                     "\n\nПочта тех.поддержки: converter@gmail.com"),
                                             QMessageBox.Ok)


    def bin_to_float(self, f):
        s = str(f)
        chars = set('23456789')
        if any((c in chars) for c in s):
            messageBox = QMessageBox.critical(self, self.tr("Ошибка!"),
                                              self.tr("Двоичное число может содержать только 0 или 1! "),
                                              QMessageBox.Ok)
            return
        if f < 0:
            flag_minus = 1
            f = f * (-1)
        else:
            flag_minus = 0
        bin_f, int_bin = modf(f)
        s_int = str(int_bin)
        l1 = len(str(int(int_bin)))
        l = l1
        sum = 0
        s1 = 'Переводим целую часть в 10сс: \n'
        for i in range(l1):                     # перевод целой части в 10сс
            sum += int(s_int[i]) * 2**(l-1)
            s1 += str(int(s_int[i])) + ' * 2^' + str(l - 1) + ' + '
            l -= 1
        s1 = s1[:-3]
        s1 += ' = '
        l = l1
        for i in range(l1):
            s1 += str(int(s_int[i]) * 2**(l-1)) + ' + '
            l -= 1
        s1 = s1[:-3]
        s1 += ' = ' + str(sum) + '\n'

        s = str(f)
        l = s.split('.')
        s_float = l[1]
        l2 = len(s_float)
        sum2 = 0
        s1 += 'Перевод дробной части: ' + '\n'
        for i in range(l2):                    # перевод дробной части в 10сс
            sum2 += int(s_float[i]) * 2 ** (-(i+1))
            s1 += str(int(s_float[i])) + ' * 2^' + str(-i-1) + ' + '
        s1 = s1[:-3]
        s1 += ' = '
        for i in range(l2):
            s1 += str(int(s_float[i]) * 2 ** (-(i+1))) + ' + '
        s1 = s1[:-3]
        s1 += ' = ' + str(sum2)

        res = sum + sum2
        s1 += '\nСкладываем целую и дробную часть: ' + str(sum) + ' + ' + str(sum2) + ' = '
        if flag_minus == 1:
            res = res * (-1)
        s1 += str(res)
        s1 += '\nРезультат: ' + str(f) + '₂= ' + str(res) + '₁₀'

        self.solution = s1
        self.lineEdit_2.setText(str(res))


    def float_to_bin(self, f, k):
        if f < 0:
            flag_minus = 1
            f = f * (-1)
        else:
            flag_minus = 0
        float_f, int_f = modf(f)
        res = ''
        s = 'Переводим целую часть в 2сс: \n'
        while int_f > 0:                      # перевод целой части числа в 2сс
            res = str(int(int_f % 2)) + res
            s += str(int_f) + ' : 2 = '
            s += str(int_f / 2) + '  ('+ str(int(int_f % 2)) + ')' + ' \n'
            int_f = int_f // 2
        res_1 = ''
        f_f = float_f
        s += "\nПереводим дробную часть в 2сс: \n"
        for i in range(k):                   # перевод дробной части числа в 2сс
            s += str(round(f_f, 1)) + ' * 2 = '
            f1 = f_f * 2
            f_f, f_i = modf(f_f * 2)
            res_1 += str(int(f_i))
            s += str(round(f1, 2)) + '  (' + str(int(f_i)) + ')' + '\n'

        s += '\nСкладываем целую и дробную часть: ' + str(res) + ' + 0.' + str(res_1) + ' = '
        number = res + '.' + res_1
        if flag_minus == 1:
            number = '-' + number
        s += str(number) + '\n'
        s += 'Результат: ' + str(f) + '₁₀= ' + number + '₂'
        self.solution = s
        self.lineEdit_2.setText(number)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())








