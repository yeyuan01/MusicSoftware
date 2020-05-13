# For self practice.
# Some code learned from https://github.com/CharlesPikachu/Tools/blob/master/MusicPlayer/MusicPlayer.py written By @CharlesPikachu
import sys
import os
from PyQt5.QtGui import *
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from music import *
from sign_in import *
from sign_up import *
import random
import pymysql
user = ''
class musicPlayer(QWidget, playerUI):
	def __init__(self):
		super(musicPlayer,self).__init__()
		self.setupUi(self)
		self.player = QMediaPlayer()
		self.is_pause = True
		self.is_switching = False
		self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
		self.cur_song = ''
		self.song_list = []
		self.timer = QTimer(self)
		self.timer.start(1000)
		self.timer.timeout.connect(self.playByMode)
		self.mode_btn.clicked.connect(self.changeMode)
		self.next_btn.clicked.connect(self.nextMusic)
		self.pre_btn.clicked.connect(self.preMusic)
		self.horizontalSlider.sliderMoved[int].connect(lambda: self.player.setPosition(self.horizontalSlider.value()))
		self.play_btn.clicked.connect(self.playMusic)
		self.music_list.itemDoubleClicked.connect(self.doubleClickPlay)
		self.cur_path = os.path.abspath(os.path.dirname(__file__))
		self.select_folder.clicked.connect(self.openDir)
		self.signin_btn.clicked.connect(self.showSignIn)

	def doubleClickPlay(self):
		self.horizontalSlider.setValue(0)
		self.is_switching = True
		self.setCurrentSong()
		self.playMusic()
		self.is_switching = False
	def changeMode(self):
		if self.mode_btn.text() == 'All Repeat':
			self.mode_btn.setText('Order')
		elif self.mode_btn.text() == 'Order':
			self.mode_btn.setText('Shuffle')
		elif self.mode_btn.text() == 'Shuffle':
			self.mode_btn.setText('Repeat Once')
		elif self.mode_btn.text() == 'Repeat Once':
			self.mode_btn.setText('All Repeat')
	def playByMode(self):
		if (not self.is_pause) and (not self.is_switching):
			self.horizontalSlider.setMinimum(0)
			self.horizontalSlider.setMaximum(self.player.duration())
			self.horizontalSlider.setValue(self.horizontalSlider.value() + 1000)
		self.label.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))
		self.label_2.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))
		if self.mode_btn.text() == 'All Repeat' and (not self.is_pause) and (not self.is_switching):
			if self.music_list.count() == 0:
				return
			if self.player.position() == self.player.duration():
				self.nextMusic()
		elif self.mode_btn.text() == 'Order' and (not self.is_pause) and (not self.is_switching):
			if self.music_list.count() == 0 or self.music_list.currentRow() == self.music_list.count():
				return
			if self.player.position() == self.player.duration():
				self.nextMusic()
		elif self.mode_btn.text() == 'Shuffle' and (not self.is_pause) and (not self.is_switching):
			if self.music_list.count() == 0:
				return
			if self.player.position() == self.player.duration():
				self.is_switching = True
				self.music_list.setCurrentRow(random.randint(0, self.music_list.count()-1))
				self.setCurrentSong()
				self.horizontalSlider.setValue(0)
				self.playMusic()
				self.is_switching = False
		elif self.mode_btn.text() == 'Repeat Once' and (not self.is_pause) and (not self.is_switching):
			if self.music_list.count() == 0:
				return
			if self.player.position() == self.player.duration():
				self.is_switching = True
				self.setCurrentSong()
				self.horizontalSlider.setValue(0)
				self.playMusic()
				self.is_switching = False
	def preMusic(self):
		self.horizontalSlider.setValue(0)
		if self.music_list.count() == 0:
			QMessageBox.warning(self, '', 'No music in list', QMessageBox.Ok)
			return
		if self.music_list.currentRow() == 0:
			self.music_list.setCurrentRow(self.music_list.count())
		else:
			self.music_list.setCurrentRow(self.music_list.currentRow() - 1)
		self.is_switching = True
		self.setCurrentSong()
		self.playMusic()
		self.is_switching = False
	def nextMusic(self):
		self.horizontalSlider.setValue(0)
		if self.music_list.count() == 0:
			QMessageBox.warning(self, '', 'No music in list', QMessageBox.Ok)
			return
		if self.music_list.currentRow() == self.music_list.count():
			self.music_list.setCurrentRow(0)
		else:
			self.music_list.setCurrentRow(self.music_list.currentRow() + 1)
		self.is_switching = True
		self.setCurrentSong()
		self.playMusic()
		self.is_switching = False

	def showSignIn(self):
		if self.signin_btn.text() == 'Sign in':
			sign_in.show()
		else:
			self.signin_btn.setText('Sign in')
			global user
			user = ''
	def openDir(self):
		self.cur_path = QFileDialog.getExistingDirectory(self,'select folder',self.cur_path)
		if self.cur_path:
			self.music_list.clear()
			for song in os.listdir(self.cur_path):
				if song.split('.')[-1] in self.song_formats:
					self.song_list.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])
					self.music_list.addItem(song)
			self.music_list.setCurrentRow(0)
			if self.song_list:
				self.cur_song = self.song_list[self.music_list.currentRow()][-1]
			self.setCurrentSong()
			self.label.setText('00:00')
			self.label_2.setText('00:00')
			self.horizontalSlider.setSliderPosition(0)
			self.is_pause = True
			self.play_btn.setText('Play')
	def playMusic(self):
		if self.music_list.count() == 0:
			QMessageBox.warning(self,'','No music in list', QMessageBox.Ok)
			return
		if not self.player.isAudioAvailable():
			self.setCurrentSong()
		if self.is_pause or self.is_switching:

			self.player.play()
			self.is_pause = False
			self.play_btn.setText('Pause')
			print("played")
		elif (not self.is_pause) and (not self.is_switching):

			self.player.pause()
			self.is_pause = True
			self.play_btn.setText('Play')
			print("paused")
	def setCurrentSong(self):
		self.cur_song = self.song_list[self.music_list.currentRow()][-1]
		self.CurrentSongName.setText(self.cur_song.split('/')[-1])
		self.player.setMedia(QMediaContent(QUrl(self.cur_song)))

class signUp(QWidget, signupUi):
	def __init__(self):
		super(signUp, self).__init__()
		self.setupUi(self)
		self.password1.setEchoMode(QLineEdit.Password)
		self.password2.setEchoMode(QLineEdit.Password)
		self.signup_btn.clicked.connect(self.checkCorrectness)
	def checkCorrectness(self):
		username = self.username.text()
		password1 = self.password1.text()
		password2 = self.password2.text()
		if username == '':
			QMessageBox.warning(self,'','user name cannot be null', QMessageBox.Ok)
		elif password1 == '' or password2 == '':
			QMessageBox.warning(self, '', 'password cannot be null', QMessageBox.Ok)
		elif password1 != password2:
			QMessageBox.warning(self, '', 'passwords must be equal', QMessageBox.Ok)
		else:
			db = pymysql.connect("localhost", "root", "", "music")
			cursor = db.cursor()
			cursor.execute('select username from accounts where username = %s', username)
			data = cursor.fetchone()
			if data:
				QMessageBox.warning(self, '', 'username already exist', QMessageBox.Ok)
				db.close()
				return
			else:
				cursor.execute('insert into accounts(username, password) value(%s, %s)', (username, password1))
				db.commit()
				db.close()
				QMessageBox.warning(self, '', 'account registered!', QMessageBox.Ok, self.close())

class signIn(QWidget, signinUI):
	def __init__(self):
		super(signIn,self).__init__()
		self.setupUi(self)
		self.password.setEchoMode(QLineEdit.Password)
		self.sign_in.clicked.connect(self.checkAccount)
		self.cancel.clicked.connect(self.close)
		self.sign_up.clicked.connect(self.show_signup)
	def show_signup(self):
		sign_up.show()
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
			if data and data[0] == password:
				global user
				user = username
				player.signin_btn.setText('Sign out')
				self.username.clear()
				self.password.clear()
				db.close()
				self.close()
			else:
				QMessageBox.warning(self, '', 'Wrong Password or Username', QMessageBox.Ok)
				db.close()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	player = musicPlayer()
	sign_up = signUp()
	sign_in = signIn()
	player.show()
	sys.exit(app.exec_())