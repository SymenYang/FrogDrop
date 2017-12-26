from BackEnd import data as DT
from BackEnd import protocol as PT
from BackEnd import broadcaster as BC
from BackEnd import listener as LT
from BackEnd import sender as SD
from BackEnd import receiver as RC
import os


def recon():
	ans = input('Do you want to receive ' + Data.fileName + ' sended from ' + Data.reqName + ' ?(y/n)')
	accept = False
	if ans == 'y':
		accept = True
	RC.finishRecon(accept, restartListen)


def restartListen():
	RC.startListen(recon)


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
		print (str(count) + ' ' + item[1])
		IPList.append(item[0])
		count += 1
	ans = input('input the number you want to send to: ')
	num = int(ans)
	if num >= 0 and num < count:
		filename = input('input the file URI you want to send: ')
		if os.path.exists(filename):
			SD.startSend(IPList[num], filename, SD.sendFile)
		else:
			print("file doesn't exists")


def main():
	Data = DT.FrogDropData()
	Data.initial()
	BC.startBroadcast()
	LT.startListen()
	RC.startListen(recon)
	while True:
		ans = choose()
		if ans == 3:
			BC.stopBroadcast()
			LT.stopListen()
			Data.save()
			print('exit')
			exit(0)
			break
		if ans == 2:
			newName = input('input new name: ')
			Data.userName = newName
		if ans == 1:
			for item in Data.receiverList:
				print (item[1])
		if ans == 0:
			choosesend()


if __name__ == '__main__':
	main()