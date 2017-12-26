import sys
sys.path.insert(0, '..')
from BackEnd import data as DT
from BackEnd import protocol
# import thread
import threading
import socket

timer = ''
stop = False


def broadcast():
	global stop
	if stop:
		print('broadcast stopped')
		return
	else:
		pass
	# print("sent")
	data = DT.FrogDropData()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	port = data.broadcasterPort
	network = '<broadcast>'
	msg = '{"program":"FrogDrop","UserName":"' + data.userName + '"}'
	s.sendto(msg.encode(), (network, port))
	global timer
	timer = threading.Timer(10, broadcast)
	timer.start()


def startBroadcast():
	stop = False
	global timer
	timer = threading.Timer(0, broadcast)
	timer.start()


def stopBroadcast():
	global stop
	print('ready to stop')
	stop = True


if __name__ == '__main__':
	startBroadcast()
	stopTimer = threading.Timer(15, stopBroadcast)
	stopTimer.start()
