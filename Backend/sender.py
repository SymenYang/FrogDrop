import data as DT
import protocol as PT
import thread
import threading
import socket
<<<<<<< HEAD
import base64
=======
>>>>>>> 4872dface877726e14b5620c4e233b8c91f59a09

def startSend(IPaddr,fileURI,nextfunc):
    Data = DT.FrogDropData()
    Data.reqIP = IPaddr
    Data.fileURI = fileURI
<<<<<<< HEAD
    fd = open(fileURI,'rb')
    statrbuffer = fd.read()
    Data.fileBuffer = base64.b64encode(statrbuffer).decode('utf-8')
=======
    fd = open(fileURI,'r')
    Data.fileBuffer = fd.read()
>>>>>>> 4872dface877726e14b5620c4e233b8c91f59a09
    Data.fileSize = len(Data.fileBuffer)
    reqDic = {'Method' : 'PUT',\
              'Sender' : Data.selfIP,\
              'SenderPort' : 36500,\
              'Receiver' : Data.reqIP,\
              'ReceiverPort' : 36500,\
              'URI' : Data.fileURI,\
              'UserName' : Data.userName,\
              'Size' : Data.fileSize}
<<<<<<< HEAD
    print(reqDic)
=======
    
>>>>>>> 4872dface877726e14b5620c4e233b8c91f59a09
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((Data.reqIP,36500))
    s.send(PT.getTrsString(reqDic))
    data = s.recv(65535)
    resDic = PT.loadFromString(data)
    if nextfunc != None:
        nextfunc()

def sendFile(nextfunc = None):
    Data = DT.FrogDropData()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((Data.selfIP,36501))
    s.listen(5)
    conn = ''
    addr = ''
    while True:
        conn,addr = s.accept()
        if addr[0] == Data.reqIP:
            break
    stopFlag = False
    while not stopFlag:
        received = conn.recv(65535)
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
        resDic = {'Method' : 'TRS',\
                  'Sender' : Data.selfIP,\
                  'SenderPort' : 36501,\
                  'Receiver' : Data.reqIP,\
                  'ReceiverPort' : 36501,\
                  'URI' : Data.fileURI,\
                  'Size' : recDic['Size']}
        resDic['File'] = Data.fileBuffer[recDic['StartPos']:recDic['StartPos'] + recDic['Size']]
        conn.send(PT.getTrsString(resDic))
<<<<<<< HEAD
        sended = recDic['StartPos'] + recDic['Size']
        print (str(sended) + ' of ' + str(Data.fileSize) + ' sended')
=======
>>>>>>> 4872dface877726e14b5620c4e233b8c91f59a09
    conn.close()
    if nextfunc != None:
        nextfunc()

if __name__ == '__main__':
    Data = DT.FrogDropData()
    Data.initial()
<<<<<<< HEAD
    startSend('10.221.123.249','../test.log',sendFile)
=======
    startSend('10.221.123.249','test.log',sendFile)
>>>>>>> 4872dface877726e14b5620c4e233b8c91f59a09
