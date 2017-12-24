import data as DT
import protocol as PT
import thread
import threading
import socket

def listen(nextfunc):
    Data = DT.FrogDropData()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((Data.selfIP,36500))
    s.listen(5)
    print('listening at ' + Data.selfIP + ':36500')
    conn,addr = s.accept()
    recived = conn.recv(65535)
    recivedData = PT.loadFromString(recived)
    Data.fileURI = recivedData['URI']
    fileSplit = Data.fileURI.split('/')
    Data.fileName = fileSplit[len(fileSplit) - 1]
    Data.fileSize = recivedData['Size']
    Data.reqName = recivedData['UserName']
    Data.reqIP = recivedData['Sender']
    resDic = {"Method" : "REC",\
              "Sender" : Data.selfIP,\
              "SenderPort" : 36500,\
              "Receiver" : Data.reqIP,\
              "ReceiverPort" : recivedData['SenderPort'],\
              "URI" : recivedData['URI'],\
              "UserName" : Data.userName}
    resString = PT.getTrsString(resDic)
    conn.send(resString)
    if nextfunc != None:
        nextfunc()

def finishRecon(accept,nextfunc):
    Data = DT.FrogDropData()
    times = Data.fileSize / 32768 + 1
    size = 32768
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((Data.reqIP,36501))
    reqDic = {"Method" : "GET",\
              "Sender" : Data.selfIP,\
              "SenderPort" : 36501,\
              "Receiver" : Data.reqIP,\
              "ReceiverPort" : 36501,\
              "URI" : Data.fileURI,\
              "StartPos" : 0,\
              "Size" : 0}
    if not accept:
        s.send(PT.getTrsString(reqDic))
        data = s.recv(65535)
        s.close()
        return
    nowPos = 0
    filed = open(Data.downloadDir + Data.fileName,'w')
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
        filed.write(file)
        nowPos += len(file)
    s.close()
    filed.close()
    if nextfunc != None:
        nextfunc()

def accept():
    finishRecon(True,None)

if __name__ == '__main__':
    Data = DT.FrogDropData()
    Data.initial()
    listen(accept)