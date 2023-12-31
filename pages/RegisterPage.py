from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

from utils import *
from setUpDB import *


class RegisterPage(object):
    def showPopUp(self, text):
        dialog = QDialog()
        dialog.setWindowTitle("Уведомление")

        dialog.setStyleSheet("background-color: rgb(77, 77, 77);")

        label = QLabel(text)
        label.setStyleSheet("color: rgb(255, 255, 255);")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("OK")
        button.setStyleSheet("QPushButton {\n"
                             "    background-color:rgb(52, 52, 52);\n"
                             "    border-color: rgb(66, 66, 66);\n"
                             "    color: rgb(255, 255, 255);\n"
                             "    border-radius: 8px;    \n"
                             "    height: 30px; margin-top: 10px;"
                             "}\n"
                             "QPushButton:hover {\n"
                             "    background-color: rgba(255, 255, 255, 0.3);\n"
                             "    color: rgb(52, 52, 52);\n"
                             "}")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        dialog.setLayout(layout)

        button.clicked.connect(dialog.accept)

        dialog.exec_()

    def __init__(self):
        self.currentUser = None
        self.register_page_2 = QtWidgets.QWidget()
        self.register_page_2.setObjectName("register_page_2")
        self.register_page_2_back = QtWidgets.QLabel(self.register_page_2)
        self.register_page_2_back.setGeometry(QtCore.QRect(30, 30, 86, 23))
        self.register_page_2_back.setText("")
        self.register_page_2_back.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.register_page_2_back.setObjectName("register_page_2_back")
        self.register_page_2_frame = QtWidgets.QFrame(self.register_page_2)
        self.register_page_2_frame.setGeometry(QtCore.QRect(490, 290, 450, 359))
        self.register_page_2_frame.setMinimumSize(QtCore.QSize(450, 320))
        self.register_page_2_frame.setMaximumSize(QtCore.QSize(399, 16777215))
        self.register_page_2_frame.setStyleSheet("border: 1px solid rgb(91, 91, 91);\n"
                                                 "border-radius: 30px;")
        self.register_page_2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_page_2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_page_2_frame.setObjectName("register_page_2_frame")
        self.register_page_2_login = QtWidgets.QWidget(self.register_page_2_frame)
        self.register_page_2_login.setGeometry(QtCore.QRect(30, 40, 399, 101))
        self.register_page_2_login.setMinimumSize(QtCore.QSize(0, 101))
        self.register_page_2_login.setStyleSheet("border: none")
        self.register_page_2_login.setObjectName("register_page_2_login")
        self.register_page_2_login_header = QtWidgets.QLabel(self.register_page_2_login)
        self.register_page_2_login_header.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.register_page_2_login_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_2_login_header.setFont(font)
        self.register_page_2_login_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.register_page_2_login_header.setObjectName("register_page_2_login_header")
        self.register_page_2_login_lineedit = QtWidgets.QLineEdit(self.register_page_2_login)
        self.register_page_2_login_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.register_page_2_login_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_2_login_lineedit.setFont(font)
        self.register_page_2_login_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(91, 91, 91);\n"
                                                          "border-radius: 8px;\n"
                                                          "padding: 5px;")
        self.register_page_2_login_lineedit.setText("")
        self.register_page_2_login_lineedit.setObjectName("register_page_2_login_lineedit")
        self.register_page_2_psswrd = QtWidgets.QWidget(self.register_page_2_frame)
        self.register_page_2_psswrd.setGeometry(QtCore.QRect(30, 140, 399, 101))
        self.register_page_2_psswrd.setMinimumSize(QtCore.QSize(0, 101))
        self.register_page_2_psswrd.setStyleSheet("border: none")
        self.register_page_2_psswrd.setObjectName("register_page_2_psswrd")
        self.register_page_2_psswrd_label = QtWidgets.QLabel(self.register_page_2_psswrd)
        self.register_page_2_psswrd_label.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.register_page_2_psswrd_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_2_psswrd_label.setFont(font)
        self.register_page_2_psswrd_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.register_page_2_psswrd_label.setObjectName("register_page_2_psswrd_label")
        self.register_page_2_psswrd_lineedit = QtWidgets.QLineEdit(self.register_page_2_psswrd)
        self.register_page_2_psswrd_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.register_page_2_psswrd_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_2_psswrd_lineedit.setFont(font)
        self.register_page_2_psswrd_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                           "border-color: rgb(66, 66, 66);\n"
                                                           "background-color: rgb(91, 91, 91);\n"
                                                           "border-radius: 8px;\n"
                                                           "padding: 5px;")
        self.register_page_2_psswrd_lineedit.setText("")
        self.register_page_2_psswrd_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_page_2_psswrd_lineedit.setObjectName("register_page_2_psswrd_lineedit")
        self.register_page_2_btn = QtWidgets.QPushButton(self.register_page_2_frame)
        self.register_page_2_btn.setEnabled(True)
        self.register_page_2_btn.setGeometry(QtCore.QRect(30, 280, 390, 35))
        self.register_page_2_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.register_page_2_btn.setMaximumSize(QtCore.QSize(16777215, 10000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_2_btn.setFont(font)
        self.register_page_2_btn.setStyleSheet("QPushButton {\n"
                                               "    background-color:rgb(52, 52, 52);\n"
                                               "    border-color: rgb(66, 66, 66);\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    border-radius: 8px;    \n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: rgba(255, 255, 255, 0.3);\n"
                                               "    color: rgb(52, 52, 52);\n"
                                               "}")
        self.register_page_2_btn.setIconSize(QtCore.QSize(16, 16))
        self.register_page_2_btn.setObjectName("register_page_2_btn")
        self.register_page_2_hedaer = QtWidgets.QLabel(self.register_page_2)
        self.register_page_2_hedaer.setGeometry(QtCore.QRect(640, 280, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_2_hedaer.setFont(font)
        self.register_page_2_hedaer.setStyleSheet("border: none;\n"
                                                  "color: rgb(217, 217, 217)")
        self.register_page_2_hedaer.setAlignment(QtCore.Qt.AlignCenter)
        self.register_page_2_hedaer.setObjectName("register_page_2_hedaer")

        self.register_page_1 = QtWidgets.QWidget()
        self.register_page_1.setObjectName("register_page_1")
        self.register_page_1_frame = QtWidgets.QFrame(self.register_page_1)
        self.register_page_1_frame.setGeometry(QtCore.QRect(490, 190, 450, 619))
        self.register_page_1_back = QtWidgets.QLabel(self.register_page_1)
        self.register_page_1_back.setGeometry(QtCore.QRect(30, 30, 86, 23))
        self.register_page_1_back.setText("")
        self.register_page_1_back.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.register_page_1_back.setObjectName("register_page_1_back")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_page_1_frame.sizePolicy().hasHeightForWidth())
        self.register_page_1_frame.setSizePolicy(sizePolicy)
        self.register_page_1_frame.setMinimumSize(QtCore.QSize(450, 320))
        self.register_page_1_frame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.register_page_1_frame.setStyleSheet("border: 1px solid rgb(91, 91, 91);\n"
                                                 "border-radius: 30px;")
        self.register_page_1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_page_1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_page_1_frame.setObjectName("register_page_1_frame")
        self.register_page_1_surname = QtWidgets.QWidget(self.register_page_1_frame)
        self.register_page_1_surname.setGeometry(QtCore.QRect(30, 30, 399, 101))
        self.register_page_1_surname.setMinimumSize(QtCore.QSize(0, 101))
        self.register_page_1_surname.setStyleSheet("border: none")
        self.register_page_1_surname.setObjectName("register_page_1_surname")
        self.register_page_1_surname_label = QtWidgets.QLabel(self.register_page_1_surname)
        self.register_page_1_surname_label.setGeometry(QtCore.QRect(0, 30, 91, 17))
        self.register_page_1_surname_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_surname_label.setFont(font)
        self.register_page_1_surname_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.register_page_1_surname_label.setObjectName("register_page_1_surname_label")
        self.register_page_1_surname_lineedit = QtWidgets.QLineEdit(self.register_page_1_surname)
        self.register_page_1_surname_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.register_page_1_surname_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_surname_lineedit.setFont(font)
        self.register_page_1_surname_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                            "border-color: rgb(66, 66, 66);\n"
                                                            "background-color: rgb(91, 91, 91);\n"
                                                            "border-radius: 8px;\n"
                                                            "padding: 5px;")
        self.register_page_1_surname_lineedit.setText("")
        self.register_page_1_surname_lineedit.setObjectName("register_page_1_surname_lineedit")
        self.register_page_1_name = QtWidgets.QWidget(self.register_page_1_frame)
        self.register_page_1_name.setGeometry(QtCore.QRect(30, 130, 399, 101))
        self.register_page_1_name.setMinimumSize(QtCore.QSize(0, 101))
        self.register_page_1_name.setStyleSheet("border: none")
        self.register_page_1_name.setObjectName("register_page_1_name")
        self.register_page_1_name_label = QtWidgets.QLabel(self.register_page_1_name)
        self.register_page_1_name_label.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.register_page_1_name_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_name_label.setFont(font)
        self.register_page_1_name_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.register_page_1_name_label.setObjectName("register_page_1_name_label")
        self.register_page_1_name_lineeditr = QtWidgets.QLineEdit(self.register_page_1_name)
        self.register_page_1_name_lineeditr.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.register_page_1_name_lineeditr.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_name_lineeditr.setFont(font)
        self.register_page_1_name_lineeditr.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(91, 91, 91);\n"
                                                          "border-radius: 8px;\n"
                                                          "padding: 5px;")
        self.register_page_1_name_lineeditr.setText("")
        self.register_page_1_name_lineeditr.setObjectName("register_page_1_name_lineeditr")
        self.register_page_1_btn_w = QtWidgets.QWidget(self.register_page_1_frame)
        self.register_page_1_btn_w.setGeometry(QtCore.QRect(30, 500, 399, 91))
        self.register_page_1_btn_w.setMinimumSize(QtCore.QSize(0, 91))
        self.register_page_1_btn_w.setStyleSheet("border: none")
        self.register_page_1_btn_w.setObjectName("register_page_1_btn_w")
        self.register_page_1_btn_btn = QtWidgets.QPushButton(self.register_page_1_btn_w)
        self.register_page_1_btn_btn.setEnabled(True)
        self.register_page_1_btn_btn.setGeometry(QtCore.QRect(0, 30, 390, 35))
        self.register_page_1_btn_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.register_page_1_btn_btn.setMaximumSize(QtCore.QSize(16777215, 10000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_btn_btn.setFont(font)
        self.register_page_1_btn_btn.setStyleSheet("QPushButton {\n"
                                                   "    background-color:rgb(52, 52, 52);\n"
                                                   "    border-color: rgb(66, 66, 66);\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    border-radius: 8px;    \n"
                                                   "}\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: rgba(255, 255, 255, 0.3);\n"
                                                   "    color: rgb(52, 52, 52);\n"
                                                   "}")
        self.register_page_1_btn_btn.setIconSize(QtCore.QSize(16, 16))
        self.register_page_1_btn_btn.setAutoDefault(False)
        self.register_page_1_btn_btn.setDefault(False)
        self.register_page_1_btn_btn.setFlat(False)
        self.register_page_1_btn_btn.setObjectName("register_page_1_btn_btn")
        self.register_page_1_patronymic = QtWidgets.QWidget(self.register_page_1_frame)
        self.register_page_1_patronymic.setGeometry(QtCore.QRect(30, 230, 399, 101))
        self.register_page_1_patronymic.setMinimumSize(QtCore.QSize(0, 101))
        self.register_page_1_patronymic.setStyleSheet("border: none")
        self.register_page_1_patronymic.setObjectName("register_page_1_patronymic")
        self.register_page_1_patronymic_label = QtWidgets.QLabel(self.register_page_1_patronymic)
        self.register_page_1_patronymic_label.setGeometry(QtCore.QRect(0, 30, 91, 17))
        self.register_page_1_patronymic_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_patronymic_label.setFont(font)
        self.register_page_1_patronymic_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.register_page_1_patronymic_label.setObjectName("register_page_1_patronymic_label")
        self.register_page_1_patronymic_lineedit = QtWidgets.QLineEdit(self.register_page_1_patronymic)
        self.register_page_1_patronymic_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.register_page_1_patronymic_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_patronymic_lineedit.setFont(font)
        self.register_page_1_patronymic_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                               "border-color: rgb(66, 66, 66);\n"
                                                               "background-color: rgb(91, 91, 91);\n"
                                                               "border-radius: 8px;\n"
                                                               "padding: 5px;")
        self.register_page_1_patronymic_lineedit.setText("")
        self.register_page_1_patronymic_lineedit.setObjectName("register_page_1_patronymic_lineedit")
        self.register_page_1_number = QtWidgets.QWidget(self.register_page_1_frame)
        self.register_page_1_number.setGeometry(QtCore.QRect(30, 410, 399, 101))
        self.register_page_1_number.setMinimumSize(QtCore.QSize(0, 101))
        self.register_page_1_number.setStyleSheet("border: none")
        self.register_page_1_number.setObjectName("register_page_1_number")
        self.register_page_1_number_label = QtWidgets.QLabel(self.register_page_1_number)
        self.register_page_1_number_label.setGeometry(QtCore.QRect(0, 30, 231, 17))
        self.register_page_1_number_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_number_label.setFont(font)
        self.register_page_1_number_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.register_page_1_number_label.setObjectName("register_page_1_number_label")
        self.register_page_1_number_lineedit = QtWidgets.QLineEdit(self.register_page_1_number)
        self.register_page_1_number_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.register_page_1_number_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_number_lineedit.setFont(font)
        self.register_page_1_number_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                           "border-color: rgb(66, 66, 66);\n"
                                                           "background-color: rgb(91, 91, 91);\n"
                                                           "border-radius: 8px;\n"
                                                           "padding: 5px;")
        self.register_page_1_number_lineedit.setObjectName("register_page_1_number_lineedit")
        self.register_page_1_sex = QtWidgets.QWidget(self.register_page_1_frame)
        self.register_page_1_sex.setGeometry(QtCore.QRect(30, 340, 401, 80))
        self.register_page_1_sex.setStyleSheet("border: none")
        self.register_page_1_sex.setObjectName("register_page_1_sex")
        self.register_page_1_sex_female = QtWidgets.QRadioButton(self.register_page_1_sex)
        self.register_page_1_sex_female.setGeometry(QtCore.QRect(120, 50, 112, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_sex_female.setFont(font)
        self.register_page_1_sex_female.setStyleSheet("border: none;\n"
                                                      "color: rgb(217, 217, 217);")
        self.register_page_1_sex_female.setObjectName("register_page_1_sex_female")
        self.register_page_1_sex_label = QtWidgets.QLabel(self.register_page_1_sex)
        self.register_page_1_sex_label.setGeometry(QtCore.QRect(0, 20, 91, 17))
        self.register_page_1_sex_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_sex_label.setFont(font)
        self.register_page_1_sex_label.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                     "border: none\n"
                                                     "")
        self.register_page_1_sex_label.setObjectName("register_page_1_sex_label")
        self.register_page_1_sex_male = QtWidgets.QRadioButton(self.register_page_1_sex)
        self.register_page_1_sex_male.setGeometry(QtCore.QRect(0, 50, 116, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_sex_male.setFont(font)
        self.register_page_1_sex_male.setStyleSheet("border: none;\n"
                                                    "color: rgb(217, 217, 217);")
        self.register_page_1_sex_male.setObjectName("register_page_1_sex_male")
        self.register_page_1_sex.raise_()
        self.register_page_1_surname.raise_()
        self.register_page_1_name.raise_()
        self.register_page_1_btn_w.raise_()
        self.register_page_1_patronymic.raise_()
        self.register_page_1_number.raise_()
        self.register_page_1_header = QtWidgets.QLabel(self.register_page_1)
        self.register_page_1_header.setGeometry(QtCore.QRect(650, 180, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_page_1_header.setFont(font)
        self.register_page_1_header.setStyleSheet("border: none;\n"
                                                  "color: rgb(217, 217, 217)")
        self.register_page_1_header.setAlignment(QtCore.Qt.AlignCenter)
        self.register_page_1_header.setObjectName("register_page_1_header")

        self.register_page_2_btn.clicked.connect(self.registerUser)  # Кнопка регистрации на RegisterPage2

    def registerUser(self):
        print(len(Roles.select()))
        if len(Roles.select()) == 0:
            setUpRoles()
        if len(Users.select()) == 0:
            result = createEmployee(
                name=self.register_page_1_name_lineeditr.text(),
                surname=self.register_page_1_surname_lineedit.text(),
                patronymic=self.register_page_1_patronymic_lineedit.text(),
                username=self.register_page_2_login_lineedit.text(),
                password=self.register_page_2_psswrd_lineedit.text(),
                number=self.register_page_1_number_lineedit.text(),
                role="Директор"
            )
            self.currentUser = result.id
            if type(result) == type(Users()):
                setUpUnits()
                setUpManufacturers()
                setUpCategories()
                setUpStatuses()
                setUpCausesToReturn()
                setUpActions()
                setUpCausesToWriteOff()
                self.stackedWidget.setCurrentIndex(1)
        else:
            self.showPopUp(
                'Регистрацию в системе проходит только директор,\n если вы являетесь сотрудником, попросите у \nадминистратора данные для входа в ваш аккаунт')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.register_page_2_login_header.setText(_translate("MainWindow", "Логин"))
        self.register_page_2_login_lineedit.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.register_page_2_psswrd_label.setText(_translate("MainWindow", "Пароль"))
        self.register_page_2_psswrd_lineedit.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.register_page_2_btn.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.register_page_2_hedaer.setText(_translate("MainWindow", "Регистрация"))
        self.register_page_1_surname_label.setText(_translate("MainWindow", "Фамилия"))
        self.register_page_1_surname_lineedit.setPlaceholderText(_translate("MainWindow", "Введите фамилию"))
        self.register_page_1_name_label.setText(_translate("MainWindow", "Имя"))
        self.register_page_1_name_lineeditr.setPlaceholderText(_translate("MainWindow", "Введите имя"))
        self.register_page_1_btn_btn.setText(_translate("MainWindow", "Далее"))
        self.register_page_1_patronymic_label.setText(_translate("MainWindow", "Отчество"))
        self.register_page_1_patronymic_lineedit.setPlaceholderText(_translate("MainWindow", "Введите отчество"))
        self.register_page_1_number_label.setText(_translate("MainWindow", "Номер телефона"))
        self.register_page_1_number_lineedit.setText(_translate("MainWindow", "+7"))
        self.register_page_1_number_lineedit.setPlaceholderText(_translate("MainWindow", "Введите номер телефона"))
        self.register_page_1_sex_female.setText(_translate("MainWindow", "(Женщина)"))
        self.register_page_1_sex_label.setText(_translate("MainWindow", "Пол"))
        self.register_page_1_sex_male.setText(_translate("MainWindow", "(Мужчина)"))
        self.register_page_1_header.setText(_translate("MainWindow", "Регистрация"))
