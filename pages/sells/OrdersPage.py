from PyQt5 import QtCore, QtGui, QtWidgets


class OrdersPage(object):
    def __init__(self):
        self.orders = QtWidgets.QWidget()
        self.orders.setObjectName("orders")
        self.orders_stackedWidget = QtWidgets.QStackedWidget(self.orders)
        self.orders_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 911))
        self.orders_stackedWidget.setObjectName("orders_stackedWidget")
        self.orders_main = QtWidgets.QWidget()
        self.orders_main.setObjectName("orders_main")
        self.orders_main_table = QtWidgets.QTableWidget(self.orders_main)
        self.orders_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.orders_main_table.setObjectName("orders_main_table")
        self.orders_main_table.setColumnCount(4)
        self.orders_main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(3, item)
        self.orders_main_createBtn = QtWidgets.QLabel(self.orders_main)
        self.orders_main_createBtn.setGeometry(QtCore.QRect(1230, 50, 131, 20))
        self.orders_main_createBtn.setText("")
        self.orders_main_createBtn.setPixmap(QtGui.QPixmap("assets/new_order.png"))
        self.orders_main_createBtn.setObjectName("orders_main_createBtn")
        self.orders_main_search_lineEdit = QtWidgets.QLineEdit(self.orders_main)
        self.orders_main_search_lineEdit.setGeometry(QtCore.QRect(60, 40, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.orders_main_search_lineEdit.setFont(font)
        self.orders_main_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                       "font: 25 10pt \"Ubuntu\";\n"
                                                       "padding: 5px;\n"
                                                       "padding-right: 35px;\n"
                                                       "border-radius: 8px;\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "background-color: rgb(52, 52, 52);")
        self.orders_main_search_lineEdit.setText("")
        self.orders_main_search_lineEdit.setObjectName("orders_main_search_lineEdit")
        self.orders_main_search_img = QtWidgets.QLabel(self.orders_main)
        self.orders_main_search_img.setGeometry(QtCore.QRect(430, 50, 18, 18))
        self.orders_main_search_img.setStyleSheet("background: none")
        self.orders_main_search_img.setText("")
        self.orders_main_search_img.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.orders_main_search_img.setObjectName("orders_main_search_img")
        self.orders_stackedWidget.addWidget(self.orders_main)
        self.orders_create = QtWidgets.QWidget()
        self.orders_create.setObjectName("orders_create")
        self.orders_create_header = QtWidgets.QLabel(self.orders_create)
        self.orders_create_header.setGeometry(QtCore.QRect(170, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orders_create_header.setFont(font)
        self.orders_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.orders_create_header.setObjectName("orders_create_header")
        self.orders_create_back_btn = QtWidgets.QLabel(self.orders_create)
        self.orders_create_back_btn.setGeometry(QtCore.QRect(60, 50, 91, 22))
        self.orders_create_back_btn.setText("")
        self.orders_create_back_btn.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.orders_create_back_btn.setObjectName("orders_create_back_btn")
        self.orders_create_login_widget = QtWidgets.QWidget(self.orders_create)
        self.orders_create_login_widget.setGeometry(QtCore.QRect(60, 100, 800, 101))
        self.orders_create_login_widget.setMinimumSize(QtCore.QSize(0, 101))
        self.orders_create_login_widget.setStyleSheet("border: none")
        self.orders_create_login_widget.setObjectName("orders_create_login_widget")
        self.orders_create_login_label = QtWidgets.QLabel(self.orders_create_login_widget)
        self.orders_create_login_label.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.orders_create_login_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_login_label.setFont(font)
        self.orders_create_login_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.orders_create_login_label.setObjectName("orders_create_login_label")
        self.orders_create_login_lineEdit = QtWidgets.QLineEdit(self.orders_create_login_widget)
        self.orders_create_login_lineEdit.setGeometry(QtCore.QRect(0, 60, 791, 35))
        self.orders_create_login_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_login_lineEdit.setFont(font)
        self.orders_create_login_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                        "border-color: rgb(66, 66, 66);\n"
                                                        "background-color: rgb(91, 91, 91);\n"
                                                        "border-radius: 8px;\n"
                                                        "padding: 5px;")
        self.orders_create_login_lineEdit.setText("")
        self.orders_create_login_lineEdit.setObjectName("orders_create_login_lineEdit")
        self.orders_create_status_widget = QtWidgets.QWidget(self.orders_create)
        self.orders_create_status_widget.setGeometry(QtCore.QRect(870, 120, 491, 80))
        self.orders_create_status_widget.setObjectName("orders_create_status_widget")
        self.orders_create_status_header = QtWidgets.QLabel(self.orders_create_status_widget)
        self.orders_create_status_header.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.orders_create_status_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_status_header.setFont(font)
        self.orders_create_status_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.orders_create_status_header.setObjectName("orders_create_status_header")
        self.orders_create_status_combobox = QtWidgets.QComboBox(self.orders_create_status_widget)
        self.orders_create_status_combobox.setGeometry(QtCore.QRect(0, 40, 491, 35))
        self.orders_create_status_combobox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "border-radius: 8px;")
        self.orders_create_status_combobox.setObjectName("orders_create_status_combobox")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_scrollArea = QtWidgets.QScrollArea(self.orders_create)
        self.orders_create_scrollArea.setGeometry(QtCore.QRect(60, 260, 1300, 611))
        self.orders_create_scrollArea.setStyleSheet("QScrollArea {\n"
                                                    "    border: none;\n"
                                                    "}")
        self.orders_create_scrollArea.setWidgetResizable(True)
        self.orders_create_scrollArea.setObjectName("orders_create_scrollArea")
        self.orders_create_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.orders_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, 800))
        self.orders_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 800))
        self.orders_create_scrollAreaWidgetContents.setObjectName("orders_create_scrollAreaWidgetContents")
        self.orders_create_item1 = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_item1.setGeometry(QtCore.QRect(0, 10, 1300, 35))
        self.orders_create_item1.setMinimumSize(QtCore.QSize(0, 0))
        self.orders_create_item1.setObjectName("orders_create_item1")
        self.orders_create_item1_name = QtWidgets.QLineEdit(self.orders_create_item1)
        self.orders_create_item1_name.setEnabled(False)
        self.orders_create_item1_name.setGeometry(QtCore.QRect(0, 0, 630, 35))
        self.orders_create_item1_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_item1_name.setFont(font)
        self.orders_create_item1_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                    "border-color: rgb(66, 66, 66);\n"
                                                    "background-color:rgb(71, 71, 71);\n"
                                                    "border-radius: 8px;\n"
                                                    "padding: 5px;")
        self.orders_create_item1_name.setText("")
        self.orders_create_item1_name.setObjectName("orders_create_item1_name")
        self.orders_create_item1_manufac = QtWidgets.QLineEdit(self.orders_create_item1)
        self.orders_create_item1_manufac.setEnabled(False)
        self.orders_create_item1_manufac.setGeometry(QtCore.QRect(640, 0, 351, 35))
        self.orders_create_item1_manufac.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_item1_manufac.setFont(font)
        self.orders_create_item1_manufac.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "background-color: rgb(71, 71, 71);\n"
                                                       "border-radius: 8px;\n"
                                                       "padding: 5px;")
        self.orders_create_item1_manufac.setText("")
        self.orders_create_item1_manufac.setObjectName("orders_create_item1_manufac")
        self.orders_create_item1_insys = QtWidgets.QLineEdit(self.orders_create_item1)
        self.orders_create_item1_insys.setEnabled(False)
        self.orders_create_item1_insys.setGeometry(QtCore.QRect(1000, 0, 110, 35))
        self.orders_create_item1_insys.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_item1_insys.setFont(font)
        self.orders_create_item1_insys.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                     "border-color: rgb(66, 66, 66);\n"
                                                     "background-color: rgb(71, 71, 71);\n"
                                                     "border-radius: 8px;\n"
                                                     "padding: 5px;")
        self.orders_create_item1_insys.setText("")
        self.orders_create_item1_insys.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_item1_insys.setObjectName("orders_create_item1_insys")
        self.orders_create_item1_inorder = QtWidgets.QSpinBox(self.orders_create_item1)
        self.orders_create_item1_inorder.setGeometry(QtCore.QRect(1120, 0, 110, 35))
        self.orders_create_item1_inorder.setStyleSheet("\n"
                                                       "background-color:rgb(91, 91, 91);\n"
                                                       "color: rgb(217, 217, 217);\n"
                                                       "border-color: rgb(66, 66, 66);")
        self.orders_create_item1_inorder.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_item1_inorder.setObjectName("orders_create_item1_inorder")
        self.orders_create_item1_close = QtWidgets.QLabel(self.orders_create_item1)
        self.orders_create_item1_close.setGeometry(QtCore.QRect(1240, 0, 35, 35))
        self.orders_create_item1_close.setStyleSheet("QLabel:hover {\n"
                                                     "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                     "    color: rgb(52, 52, 52);\n"
                                                     "}")
        self.orders_create_item1_close.setText("")
        self.orders_create_item1_close.setPixmap(QtGui.QPixmap("assets/X.png"))
        self.orders_create_item1_close.setObjectName("orders_create_item1_close")
        self.orders_create_newItem = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_newItem.setGeometry(QtCore.QRect(0, 60, 1281, 35))
        self.orders_create_newItem.setObjectName("orders_create_newItem")
        self.orders_create_newItem_ok = QtWidgets.QPushButton(self.orders_create_newItem)
        self.orders_create_newItem_ok.setGeometry(QtCore.QRect(1170, 0, 101, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_newItem_ok.setFont(font)
        self.orders_create_newItem_ok.setStyleSheet("QPushButton {\n"
                                                    "    background-color: rgb(91, 91, 91);\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    border: 1px solid rgb(66, 66, 66);\n"
                                                    "}\n"
                                                    "QPushButton:hover {\n"
                                                    "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                    "    color: rgb(52, 52, 52);\n"
                                                    "}\n"
                                                    "")
        self.orders_create_newItem_ok.setObjectName("orders_create_newItem_ok")
        self.orders_create_newItem_name = QtWidgets.QLineEdit(self.orders_create_newItem)
        self.orders_create_newItem_name.setGeometry(QtCore.QRect(0, 0, 1041, 35))
        self.orders_create_newItem_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_newItem_name.setFont(font)
        self.orders_create_newItem_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                      "border-color: rgb(66, 66, 66);\n"
                                                      "background-color: rgb(91, 91, 91);\n"
                                                      "border-radius: 6px;\n"
                                                      "padding: 5px;")
        self.orders_create_newItem_name.setText("")
        self.orders_create_newItem_name.setObjectName("orders_create_newItem_name")
        self.orders_create_newItem_amount = QtWidgets.QSpinBox(self.orders_create_newItem)
        self.orders_create_newItem_amount.setGeometry(QtCore.QRect(1050, 0, 110, 35))
        self.orders_create_newItem_amount.setStyleSheet("\n"
                                                        "background-color:rgb(91, 91, 91);\n"
                                                        "color: rgb(217, 217, 217);\n"
                                                        "border-color: rgb(66, 66, 66);")
        self.orders_create_newItem_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_newItem_amount.setObjectName("orders_create_newItem_amount")
        self.orders_create_scrollArea.setWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_table_name = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_name.setGeometry(QtCore.QRect(60, 240, 67, 17))
        self.orders_create_table_name.setObjectName("orders_create_table_name")
        self.orders_create_table_manufac = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_manufac.setGeometry(QtCore.QRect(700, 240, 141, 17))
        self.orders_create_table_manufac.setObjectName("orders_create_table_manufac")
        self.orders_create_table_insys = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_insys.setGeometry(QtCore.QRect(1060, 240, 111, 17))
        self.orders_create_table_insys.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_table_insys.setObjectName("orders_create_table_insys")
        self.orders_create_inorder = QtWidgets.QLabel(self.orders_create)
        self.orders_create_inorder.setGeometry(QtCore.QRect(1180, 240, 111, 17))
        self.orders_create_inorder.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_inorder.setObjectName("orders_create_inorder")
        self.orders_create_saveBtn = QtWidgets.QPushButton(self.orders_create)
        self.orders_create_saveBtn.setGeometry(QtCore.QRect(1000, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_saveBtn.setFont(font)
        self.orders_create_saveBtn.setStyleSheet("QPushButton {\n"
                                                 "    background-color: rgb(91, 91, 91);\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    border-radius: 8px;\n"
                                                 "    border: 1px solid rgb(66, 66, 66);\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                 "    color: rgb(52, 52, 52);\n"
                                                 "}\n"
                                                 "")
        self.orders_create_saveBtn.setObjectName("orders_create_saveBtn")
        self.orders_create_deleteImg = QtWidgets.QLabel(self.orders_create)
        self.orders_create_deleteImg.setGeometry(QtCore.QRect(1320, 40, 35, 35))
        self.orders_create_deleteImg.setStyleSheet("QLabel:hover {\n"
                                                   "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                   "    color: rgb(52, 52, 52);\n"
                                                   "}")
        self.orders_create_deleteImg.setText("")
        self.orders_create_deleteImg.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.orders_create_deleteImg.setObjectName("orders_create_deleteImg")
        self.orders_create_closeBtn = QtWidgets.QPushButton(self.orders_create)
        self.orders_create_closeBtn.setGeometry(QtCore.QRect(1160, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_closeBtn.setFont(font)
        self.orders_create_closeBtn.setStyleSheet("QPushButton {\n"
                                                  "    background-color: rgb(66, 66, 66);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    border-radius: 8px;\n"
                                                  "    border: 1px solid rgb(52, 52, 52);\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                  "    color: rgb(52, 52, 52);\n"
                                                  "}\n"
                                                  "")
        self.orders_create_closeBtn.setObjectName("orders_create_closeBtn")
        self.orders_stackedWidget.addWidget(self.orders_create)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        item = self.orders_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код заказа"))
        item = self.orders_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.orders_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Адрес"))
        item = self.orders_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата и время"))
        self.orders_main_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.orders_create_header.setText(_translate("MainWindow", "Заказ 123123"))
        self.orders_create_login_label.setText(_translate("MainWindow", "Адрес"))
        self.orders_create_login_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите адрес"))
        self.orders_create_status_header.setText(_translate("MainWindow", "Статус"))
        self.orders_create_status_combobox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.orders_create_status_combobox.setItemText(0, _translate("MainWindow", "Создан"))
        self.orders_create_status_combobox.setItemText(1, _translate("MainWindow", "Принят"))
        self.orders_create_status_combobox.setItemText(2, _translate("MainWindow", "Собирается"))
        self.orders_create_status_combobox.setItemText(3, _translate("MainWindow", "Отправлен"))
        self.orders_create_status_combobox.setItemText(4, _translate("MainWindow", "Принят на складе"))
        self.orders_create_status_combobox.setItemText(5, _translate("MainWindow", "Передан курьеру"))
        self.orders_create_status_combobox.setItemText(6, _translate("MainWindow", "Завершен"))
        self.orders_create_item1_name.setPlaceholderText(
            _translate("MainWindow", "Молоко ультра пастеризованное 900 мл"))
        self.orders_create_item1_manufac.setPlaceholderText(_translate("MainWindow", "ООО Простоквашено"))
        self.orders_create_item1_insys.setPlaceholderText(_translate("MainWindow", "0"))
        self.orders_create_newItem_ok.setText(_translate("MainWindow", "OK"))
        self.orders_create_newItem_name.setPlaceholderText(_translate("MainWindow", "Введите название..."))
        self.orders_create_table_name.setText(_translate("MainWindow", "Товар"))
        self.orders_create_table_manufac.setText(_translate("MainWindow", "Производитель"))
        self.orders_create_table_insys.setText(_translate("MainWindow", "В системе"))
        self.orders_create_inorder.setText(_translate("MainWindow", "В заказе"))
        self.orders_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.orders_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))