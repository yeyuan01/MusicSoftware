# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class signupUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 516)
        self.signup_btn = QtWidgets.QPushButton(Form)
        self.signup_btn.setGeometry(QtCore.QRect(309, 259, 93, 28))
        self.signup_btn.setObjectName("signup_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 150, 206, 94))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.layoutWidget)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.password1.setObjectName("password1")
        self.horizontalLayout_2.addWidget(self.password1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.password2.setObjectName("password2")
        self.horizontalLayout_3.addWidget(self.password2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.signup_btn.setText(_translate("Form", "sign up"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "Password"))
        self.password2.setToolTip(_translate("Form", "<html><head/><body><p>Please repeat your password</p></body></html>"))
