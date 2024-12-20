from PyQt5 import (QtCore, QtGui, QtWidgets)
import random
import string

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setWindowTitle("Менеджер Паролів")
        icon = QtGui.QIcon("image.png")
        Form.setWindowIcon(icon)
        Form.setStyleSheet("""
                    QWidget {
                        background-color: #2c3e50;
                        font-family: 'Segoe UI';
                        font-size: 12pt;
                        color: #ecf0f1;
                    }
                    QPushButton {
                        background-color: #2980b9;
                        border: none;
                        border-radius: 10px;
                        padding: 10px 20px;
                        color: white;
                        font-weight: bold;
                        font-size: 12pt;
                        width: 300px;
                    }
                    QPushButton:hover {
                        background-color: #1c598a;
                    }
                    QRadioButton {
                        spacing: 10px;
                        color: #ecf0f1;
                        background: transparent;
                        font-size: 11pt;
                    }
                    QRadioButton::indicator {
                        border: 2px solid #95a5a6;
                        width: 15px;
                        height: 15px;
                        border-radius: 7px;
                        background: #34495e;
                    }
                    QRadioButton::indicator:checked {
                        background-color: #2980b9;
                        border: 2px solid #1c598a;
                    }
                    QGroupBox {
                        border: 2px solid #95a5a6;
                        border-radius: 10px;
                        margin-top: 15px;
                        background-color: #34495e;
                        padding: 10px;
                        color: #ecf0f1;
                    }
                    QGroupBox::title {
                        subcontrol-origin: margin;
                        subcontrol-position: top center;
                        padding: 5px;
                        font-size: 14pt;
                        font-weight: bold;
                        color: #ecf0f1;
                    }
                """)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 250, 150))
        self.groupBox.setTitle("Складність пароля")

        self.radioButton_easy = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_easy.setGeometry(QtCore.QRect(20, 30, 200, 20))
        self.radioButton_easy.setText("Легкий")

        self.radioButton_medium = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_medium.setGeometry(QtCore.QRect(20, 60, 200, 20))
        self.radioButton_medium.setText("Середній")

        self.radioButton_hard = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_hard.setGeometry(QtCore.QRect(20, 90, 200, 20))
        self.radioButton_hard.setText("Складний")

        self.radioButton_very_hard = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_very_hard.setGeometry(QtCore.QRect(20, 120, 200, 20))
        self.radioButton_very_hard.setText("Дуже складний")

        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 50, 250, 150))
        self.groupBox_2.setTitle("Довжина пароля")

        self.radioButton_short = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_short.setGeometry(QtCore.QRect(20, 30, 200, 20))
        self.radioButton_short.setText("Короткий")

        self.radioButton_medium_length = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_medium_length.setGeometry(QtCore.QRect(20, 60, 200, 20))
        self.radioButton_medium_length.setText("Середній")

        self.radioButton_long = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_long.setGeometry(QtCore.QRect(20, 90, 200, 20))
        self.radioButton_long.setText("Довгий")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 220, 120, 30))
        self.label.setText("Пароль:")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 220, 200, 30))

        self.pushButton_generate = QtWidgets.QPushButton(Form)
        self.pushButton_generate.setGeometry(QtCore.QRect(200, 270, 200, 40))
        self.pushButton_generate.setText("Згенерувати пароль")
        self.pushButton_generate.clicked.connect(self.generate_password)

        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(40, 330, 150, 40))
        self.pushButton_add.setText("Додати пароль")
        self.pushButton_add.clicked.connect(self.add_password)

        self.pushButton_check = QtWidgets.QPushButton(Form)
        self.pushButton_check.setGeometry(QtCore.QRect(220, 330, 150, 40))
        self.pushButton_check.setText("Переглянути паролі")
        self.pushButton_check.clicked.connect(self.view_passwords)

        self.pushButton_delete = QtWidgets.QPushButton(Form)
        self.pushButton_delete.setGeometry(QtCore.QRect(400, 330, 150, 40))
        self.pushButton_delete.setText("Видалити пароль")
        self.pushButton_delete.clicked.connect(self.delete_password)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 390, 510, 100))
        self.listWidget.setObjectName("listWidget")

    def generate_password(self):
        if self.radioButton_easy.isChecked():
            chars = string.ascii_lowercase
        elif self.radioButton_medium.isChecked():
            chars = string.ascii_letters
        elif self.radioButton_hard.isChecked():
            chars = string.ascii_letters + string.digits
        elif self.radioButton_very_hard.isChecked():
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_lowercase

        if self.radioButton_short.isChecked():
            length = 6
        elif self.radioButton_medium_length.isChecked():
            length = 10
        elif self.radioButton_long.isChecked():
            length = 16
        else:
            length = 8

        password = ''.join(random.choice(chars) for _ in range(length))
        self.lineEdit.setText(password)

    def add_password(self):
        password = self.lineEdit.text()
        if not password:
            self.show_message("Помилка", "Поле пароля порожнє!")
            return

        label, ok = QtWidgets.QInputDialog.getText(None, "Додати пароль", "Введіть назву для пароля:")
        if not ok or not label:
            return

        try:
            with open("passwords.txt", "r") as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            lines = []

        entry = f"{label}: {password}"
        if any(line.split(": ")[0] == label for line in lines):
            self.show_message("Інформація", "Така назва вже існує!")
        else:
            with open("passwords.txt", "a") as file:
                file.write(entry + "\n")
            self.show_message("Успіх", "Пароль успішно додано!")
            self.view_passwords()

    def view_passwords(self):
        self.listWidget.clear()
        try:
            with open("passwords.txt", "r") as file:
                passwords = file.read().splitlines()
            if passwords:
                self.listWidget.addItems(passwords)
            else:
                self.listWidget.addItem("Паролів немає.")
        except FileNotFoundError:
            self.listWidget.addItem("Файл паролів не знайдено.")

    def delete_password(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            self.show_message("Помилка", "Не вибрано жодного пароля!")
            return

        try:
            with open("passwords.txt", "r") as file:
                passwords = file.read().splitlines()

            for item in selected_items:
                passwords.remove(item.text())

            with open("passwords.txt", "w",) as file:
                file.write("\n".join(passwords) + "\n")

            self.show_message("Успіх", "Пароль(і), удалилися вдачно!")
            self.view_passwords()
        except FileNotFoundError:
            self.show_message("Помилка","Пароль не знайдено")


    def show_message(self,title,message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
