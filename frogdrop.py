from UI.send_ui import Ui_SendDialog
from UI.frogdrop_ui import Ui_FrogDrop
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from BackEnd import broadcaster, data, listener, sender, receiver
import sys, time, os

sys.path.insert(0, '..')


class FrogDrop(QtWidgets.QMainWindow, Ui_FrogDrop):
	__received_signal = QtCore.pyqtSignal()

	def __init__(self):
		super(FrogDrop, self).__init__()
		broadcaster.startBroadcast()
		listener.startListen()
		receiver.startListen(self.recv_alert)

		self.setupUi(self)
		self.RefreshBtn.clicked.connect(self.refresh)
		self.ChooseBtn.clicked.connect(self.choose)
		self.EditBtn.clicked.connect(self.rename)
		self.__received_signal.connect(self.show_Message_Box)

		self.LogoPic.setPixmap(QtGui.QPixmap('../images/logo_tmp.jpg'))
		self.LogoPic.setScaledContents(True)
		self.HeadPic.setPixmap(QtGui.QPixmap('../images/pika.jpg'))
		self.HeadPic.setScaledContents(True)

		self.refresh()

	def dropping(self):
		while True:
			time.sleep(5)
			self.refresh()

	def refresh(self):
		self.HostIP.setText(fd_data.selfIP)
		self.NameLabel.setText(fd_data.userName)

		self.RecTable.clear()
		self.RecTable.setColumnCount(2)
		self.RecTable.setRowCount(len(fd_data.receiverList))
		self.RecTable.horizontalHeader().setStretchLastSection(True)
		self.RecTable.setHorizontalHeaderLabels(['IP', 'Nickname'])
		self.RecTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		table_item = QtWidgets.QTableWidgetItem

		for idx, ip in enumerate(fd_data.receiverList):
			self.RecTable.setItem(idx, 0, table_item(ip))
			self.RecTable.setItem(idx, 1, table_item(fd_data.receiverList[ip][0]))

	def rename(self):
		value, ok = QtWidgets.QInputDialog.getText(self, "Edit Nickname", "You want to be seen as...",
		                                           QtWidgets.QLineEdit.Normal, fd_data.userName)
		if ok:
			fd_data.setNewName(value)
			self.refresh()

	def choose(self):
		try:
			cur_row = self.RecTable.currentRow()
			ip = self.RecTable.item(cur_row, 0).text()
			print(ip)
		except:
			QMessageBox.warning(self, 'WARNING', 'You are sending to a ghost:)', QMessageBox.Ok)
			return

		send_dg = SendDialog(ip)
		send_dg.show()
		send_dg.exec_()

	def recv_alert(self):
		if fd_data.reqIP == fd_data.selfIP:
			print('ha')
			ok = True
			receiver.finishRecon(ok, self.restart_listen)
		else:
			print('here')
			self.__received_signal.emit()
			# ok = QMessageBox.question(self, 'New Request',
			#                          'Do you want to receive %s from %s?' % (fd_data.fileName, fd_data.reqName),
			#                          QMessageBox.Yes | QMessageBox.No)

	def show_Message_Box(self):
		ok = (QMessageBox.Yes == QMessageBox.question(self, 'New Request', 'Do you want to receive %s from %s?' % (
		fd_data.fileName, fd_data.reqName), QMessageBox.Yes | QMessageBox.No))
		receiver.finishRecon(ok, self.restart_listen)

	def restart_listen(self):
		receiver.startListen(self.recv_alert)


class SendDialog(QtWidgets.QDialog, Ui_SendDialog):
	def __init__(self, ip):
		super(SendDialog, self).__init__()

		self.setupUi(self)
		self.SelectBtn.clicked.connect(self.select_file)
		self.SendBtn.clicked.connect(self.send_multithread)
		self.ip = ip
		self.name = fd_data.receiverList[ip][0]
		self.file = None
		self.ProgBar.setValue(0)

	def select_file(self):
		path = QtWidgets.QFileDialog.getOpenFileName(self,
		                                             'Select file',
		                                             '',
		                                             'All Files (*)')[0]
		if path != None:
			self.file = path
			if not os.path.exists(self.file):
				QMessageBox.warning(self, 'WARNING', 'You just selected nothing:(')
				return
		print(path)
		self.SendLog.setText('Selected ' + self.file.split('/')[-1])

	def send(self):
		'''
		single thread
		'''
		self.SelectBtn.setEnabled(False)
		self.SendBtn.setEnabled(False)

		msg = 'Waiting for response...'
		self.SendLog.setText(msg)

		# if sender.acceptFlag is sender.SD_NO:
		# 	self.SendLog.setText('He/She said no:(')
		# 	time.sleep(5)
		# 	self.SendBtn.setEnabled(True)
		# 	return

		msg = 'Sending %s to %s...' % (self.file.split('/')[-1], self.name)
		self.SendLog.setText(msg)

		sender.startSend(self.ip, self.file, sender.sendFile)

		sender.stopFlag = False
		sender.acceptFlag = sender.SD_WAIT

		self.SendLog.setText('File sent.')
		self.SendBtn.setEnabled(True)
		self.SelectBtn.setEnabled(True)

	def send_multithread(self):
		self.SendBtn.setEnabled(False)
		self.SelectBtn.setEnabled(False)
		msg = 'Waiting for response...'
		self.SendLog.setText(msg)

		# TODO: wait util yes

		msg = 'Sending %s to %s...' % (self.file.split('/')[-1], self.name)
		self.SendLog.setText(msg)

		self.worker = SendThread(self.ip, self.file)
		self.worker.trigger.connect(self.send_complete)
		self.worker.start()

	def send_complete(self, flag):
		self.SendBtn.setEnabled(True)
		self.SelectBtn.setEnabled(True)
		if flag:
			self.SendLog.setText('File sent.')
		else:
			self.SendLog.setText('Sending abort.')


#TODO
class WaitThread(QtCore.QThread):
	trigger = QtCore.pyqtSignal(bool)
	def __init__(self):
		super(WaitThread, self).__init__()

	def run(self):
		pass


class SendThread(QtCore.QThread):
	trigger = QtCore.pyqtSignal(bool)

	def __init__(self, ip, file):
		super(SendThread, self).__init__()
		self.ip = ip
		self.file = file

	def run(self):
		try:
			sender.startSend(self.ip, self.file, sender.sendFile)
			self.trigger.emit(True)
		except:
			self.trigger.emit(False)


fd_data = data.FrogDropData()
fd_data.initial()

app = QtWidgets.QApplication(sys.argv)
frogdrop = FrogDrop()

frogdrop.show()
app.exec_()
me = os.getpid()
os.kill(me, 9)