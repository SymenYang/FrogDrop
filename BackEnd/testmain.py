import sys
sys.path.insert(0, '..')
from BackEnd import data, protocol, broadcaster, listener, sender, receiver
import os


def recon():
	ans = input('Do you want to receive ' + Data.fileName + ' sent from ' + Data.reqName + ' ?(y/n)')
	accept = False
	if ans == 'y':
		accept = True
	receiver.finishRecon(accept, restartListen)


def restartListen():
	receiver.startListen(recon)


def choose():
	print \
		('''
0. Send File
1. Check the receiver list
2. Change username
3. exit
''')
	ans = input('input the number: ')
	if ans == '0':
		return 0
	if ans == '1':
		return 1
	if ans == '2':
		return 2
	if ans == '3':
		return 3


def choosesend():
	count = 0
	IPList = []
	for item in Data.receiverList:
		print (str(count) + ' ' + Data.receiverList[item][0])
		IPList.append(item)
		count += 1
	ans = input('input the number you want to send to: ')
	num = int(ans)
	if num >= 0 and num < count:
		filename = input('input the file URI you want to send: ')
		if os.path.exists(filename):
			sender.startSend(IPList[num], filename, sender.sendFile)
		else:
			print("file doesn't exists")


def main():
	while True:
		ans = choose()
		if ans == 3:
			broadcaster.stopBroadcast()
			listener.stopListen()
			Data.save()
			print('exit')
			exit(0)
			break
		if ans == 2:
			newName = input('input new name: ')
			Data.setNewName(newName)
		if ans == 1:
			for item in Data.receiverList:
				print (Data.receiverList[item][0])
		if ans == 0:
			choosesend()


if __name__ == '__main__':
	Data = data.FrogDropData()
	Data.initial()
	broadcaster.startBroadcast()
	listener.startListen()
	receiver.startListen(recon)
	main()