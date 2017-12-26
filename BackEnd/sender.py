import sys
sys.path.insert(0, '..')
from BackEnd import data as DT
from BackEnd import protocol as PT
# import thread
import threading
import socket
import base64


def startSend(IPaddr, fileURI, nextfunc):
	Data = DT.FrogDropData()
	Data.reqIP = IPaddr
	Data.fileURI = fileURI
	fd = open(fileURI, 'rb')
	statrbuffer = fd.read()
	Data.fileBuffer = base64.b64encode(statrbuffer).decode('utf-8')
	Data.fileSize = len(Data.fileBuffer)
	reqDic = {'Method': 'PUT', \
	          'Sender': Data.selfIP, \
	          'SenderPort': 36500, \
	          'Receiver': Data.reqIP, \
	          'ReceiverPort': 36500, \
	          'URI': Data.fileURI, \
	          'UserName': Data.userName, \
	          'Size': Data.fileSize}
	print(reqDic)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect((Data.reqIP, 36500))
	s.send(PT.getTrsString(reqDic).encode())
	data = s.recv(65535)
	resDic = PT.loadFromString(data)
	if nextfunc != None:
		nextfunc()


def sendFile(nextfunc=None):
	Data = DT.FrogDropData()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((Data.selfIP, 36501))
	s.listen(5)
	conn = ''
	addr = ''
	while True:
		conn, addr = s.accept()
		if addr[0] == Data.reqIP:
			break
	stopFlag = False
	while not stopFlag:
		received = conn.recv(65535).decode('utf-8')
		print('')
		print('received', type(received), received)
		print('')
		recDic = PT.loadFromString(received)
		if 'error' in recDic:
			print('protocol error')
			break
		if recDic['URI'] != Data.fileURI:
			print('URI not match')
			break
		if recDic['Size'] == 0:
			print('Finished')
			break
		resDic = {'Method': 'TRS', \
		          'Sender': Data.selfIP, \
		          'SenderPort': 36501, \
		          'Receiver': Data.reqIP, \
		          'ReceiverPort': 36501, \
		          'URI': Data.fileURI, \
		          'Size': recDic['Size']}
		resDic['File'] = Data.fileBuffer[recDic['StartPos']:recDic['StartPos'] + recDic['Size']]
		conn.send(PT.getTrsString(resDic))
		sent = recDic['StartPos'] + recDic['Size']
		print (str(sent) + ' of ' + str(Data.fileSize) + ' sent')
	conn.close()
	if nextfunc != None:
		nextfunc()


if __name__ == '__main__':
	Data = DT.FrogDropData()
	Data.initial()
	startSend('10.221.123.249', '../test.log', sendFile)
