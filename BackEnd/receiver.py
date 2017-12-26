from BackEnd import data as DT
from BackEnd import protocol as PT
import _thread as thread
import threading
import socket
import base64

stopReceive = False


def startListen(nextfunc):
	global stopReceive
	stopReceive = False
	thread.start_new_thread(listen, (nextfunc, None))


def stopListen():
	global stopReceive
	print('ready to stop listen')
	stopReceive = True


def listen(nextfunc, sth=None):
	global stopReceive
	Data = DT.FrogDropData()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((Data.selfIP, 36500))
	print('listening at ' + Data.selfIP + ':36500')
	while not stopReceive:
		s.settimeout(5)
		try:
			s.listen(5)
			conn, addr = s.accept()
			conn.setblocking(1)
			recived = conn.recv(65535)
			recivedData = PT.loadFromString(recived)
			Data.fileURI = recivedData['URI']
			temp = Data.fileURI.replace('\\', '/')
			fileSplit = temp.split('/')
			Data.fileName = fileSplit[len(fileSplit) - 1]
			Data.fileSize = recivedData['Size']
			Data.reqName = recivedData['UserName']
			Data.reqIP = recivedData['Sender']
			resDic = {"Method": "REC", \
			          "Sender": Data.selfIP, \
			          "SenderPort": 36500, \
			          "Receiver": Data.reqIP, \
			          "ReceiverPort": recivedData['SenderPort'], \
			          "URI": recivedData['URI'], \
			          "UserName": Data.userName}
			resString = PT.getTrsString(resDic)
			conn.send(resString)
			conn.close()
			if nextfunc != None:
				nextfunc()
				return
		except:
			pass
			# print('recive time out')


def finishRecon(accept, nextfunc):
	Data = DT.FrogDropData()
	size = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect((Data.reqIP, 36501))
	reqDic = {"Method": "GET", \
	          "Sender": Data.selfIP, \
	          "SenderPort": 36501, \
	          "Receiver": Data.reqIP, \
	          "ReceiverPort": 36501, \
	          "URI": Data.fileURI, \
	          "StartPos": 0, \
	          "Size": 0}
	if not accept:
		s.send(PT.getTrsString(reqDic))
		data = s.recv(65535)
		s.close()
		if nextfunc != None:
			nextfunc()
		return
	nowPos = 0
	filed = open(Data.downloadDir + Data.fileName, 'wb')
	while nowPos <= Data.fileSize:
		reqDic['Size'] = size
		if size + nowPos > Data.fileSize:
			reqDic['Size'] = Data.fileSize - nowPos
		reqDic['StartPos'] = nowPos
		s.send(PT.getTrsString(reqDic))
		data = s.recv(65535)
		if nowPos == Data.fileSize:
			break
		resDic = PT.loadFromString(data)
		file = resDic['File']
		finaldata = base64.b64decode(file)
		filed.write(finaldata)
		nowPos += len(file)
		print(str(nowPos) + ' of ' + str(Data.fileSize) + ' received')
	# s.close()
	filed.close()
	if nextfunc != None:
		nextfunc()


def accept():
	finishRecon(True, None)


if __name__ == '__main__':
	Data = DT.FrogDropData()
	Data.initial()
	startListen(accept)
	Timer = threading.Timer(15, stopListen)
	Timer.start()
