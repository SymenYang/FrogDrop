import json
import codecs
import socket
import os

class SingleClass(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(SingleClass, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance  

class FrogDropData(SingleClass) : 
    selfIP = "127.0.0.1"
    broadcasterPort = 3524
    downloadDir = ""
    fileURI = ""
    fileName = ""
    fileSize = 0
    receiverList = {} #((IP,userName):last receive time)
    userName = ""
    reqName = ""
    reqIP = ""

    fileBuffer = ""
    userNameFile = "userinfo.log"

    def initial(self):
        '''
        initial data from self.userNameFile and system info
        include selfIP,userName
        '''
        self.userName = socket.getfqdn(socket.gethostname())
        self.selfIP = socket.gethostbyname(self.userName)
        if not os.path.exists(self.userNameFile):
            userinfofd = codecs.open(self.userNameFile,'w','utf-8')
            userinfofd.write('{\n\t"userName" : "' + self.userName + '",\n}')
            userinfofd.close()
            return
        userinfofd = codecs.open(self.userNameFile,'r','utf-8')
        textdata = userinfofd.read()
        userinfoJson = json.loads(textdata)
        self.userName = userinfoJson["userName"]
        if userinfoJson.has_key('broadcasterPort'):
            self.broadcasterPort = userinfoJson["broadcasterPort"]
        userinfofd.close()

    def save(self):
        userinfofd = codecs.open(self.userNameFile,'w','utf-8')
        tempDic = {}
        tempDic['userName'] = self.userName
        tempDic['broadcasterPort'] = self.broadcasterPort
        userinfofd.write(json.dumps(tempDic))
        userinfofd.close()

data = FrogDropData()
data.initial()
data.save()
