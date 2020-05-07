import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from music import *
from sign_in import *
import pymysql
user = ''
class musicPlayer(QWidget, playerUI):
	def __init__(self):
		super(musicPlayer,self).__init__()
		self.setupUi(self)
		self.signin_btn.clicked.connect(self.showSignIn)
		self.play_btn.clicked.connect(self.play)
	def showSignIn(self):
		if self.signin_btn.text() == 'Sign in':
			sign_in.show()
		else:
			self.signin_btn.setText('Sign in')
			global user
			user = ''
	def play(self):
		pass
class signIn(QWidget, signinUI):
	def __init__(self):
		super(signIn,self).__init__()
		self.setupUi(self)
		self.password.setEchoMode(QLineEdit.Password)
		self.sign_in.clicked.connect(self.checkAccount)
	def checkAccount(self):
		username = self.username.text()
		password = self.password.text()
		if username == '':
			QMessageBox.warning(self,'','user name cannot be null', QMessageBox.Ok)
		elif password == '':
			QMessageBox.warning(self, '', 'password cannot be null', QMessageBox.Ok)
		else:
			db = pymysql.connect("localhost", "root", "", "music")
			cursor = db.cursor()
			cursor.execute('SELECT password from accounts where username = %s', username)
			data = cursor.fetchone()
			if data[0] == password:
				global user
				user = username
				player.signin_btn.setText('Sign out')
				db.close()
				self.close()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	player = musicPlayer()
	sign_in = signIn()
	player.show()
	sys.exit(app.exec_())