import data as DT
import broadcaster as BC
import protocol
import socket
import thread
import json
import threading
import time

listenStop = False
def listen():
    global listenStop
    listenStop = False
#    BC.stopBroadcast()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    PORT = 3524
    s.bind(('',PORT))
    print('Listening for broadcast at ', s.getsockname())
    universalData = DT.FrogDropData()
    universalData.receiverList.clear()
    while not listenStop:
        print('once')
        s.settimeout(5.0)
        try:
            data, address = s.recvfrom(65535)
            print('Server received from {}:{}'.format(address, data.decode('utf-8')))
            tempDic = json.loads(data.decode('utf-8'))
            IPaddr = address[0]
            nowtime = time.time()
            userName = tempDic['UserName']
            universalData.receiverList[(IPaddr,userName)] = nowtime
        except:
            print('time out')
        nowtime = time.time()
        poplist = []
        for key in universalData.receiverList:
            if (nowtime - universalData.receiverList[key]) >= 15:
                print (key)
                poplist.append(key)
        for key in poplist:
            universalData.receiverList.pop(key)

def startListen():
    thread.start_new_thread(listen,())

def stopListen():
    global listenStop
    print('ready to stop listen')
    listenStop = True

if __name__ == '__main__':
    startListen()
    timer = threading.Timer(30,stopListen)
    timer.start()