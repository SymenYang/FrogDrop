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


class FrogDropData(SingleClass):
	selfIP = "127.0.0.1"
	broadcasterPort = 3524
	downloadDir = "../received/"
	if not os.path.isdir(downloadDir):
		os.mkdir(downloadDir)
	fileURI = ""
	fileName = ""
	fileSize = 0
	sentSize = 0
	receiverList = {}  # (IP: (userName,last receive time)
	userName = ""
	reqName = ""
	reqIP = ""

	fileBuffer = ""
	if not os.path.isdir('../log/'):
		os.mkdir('../log/')
	userNameFile = "../log/userinfo.log"

	def get_host_ip(self):
		ip = ""
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('1.1.1.1', 80))
			ip = s.getsockname()[0]
		finally:
			s.close()
		return ip

	def initial(self):
		'''
		initial data from self.userNameFile and system info
		include selfIP,userName
		'''
		self.userName = socket.getfqdn(socket.gethostname())
		self.selfIP = socket.gethostbyname(self.userName)
		if not os.path.exists(self.userNameFile):
			userinfofd = codecs.open(self.userNameFile, 'w', 'utf-8')
			userinfofd.write('{\n\t"userName" : "' + self.userName + '",\n}')
			userinfofd.close()
			return
		userinfofd = codecs.open(self.userNameFile, 'r', 'utf-8')
		textdata = userinfofd.read()
		userinfoJson = json.loads(textdata)
		self.userName = userinfoJson["userName"]
		if userinfoJson.get('broadcasterPort') != None:
			self.broadcasterPort = userinfoJson["broadcasterPort"]
		userinfofd.close()

	def save(self):
		userinfofd = codecs.open(self.userNameFile, 'w', 'utf-8')
		tempDic = {}
		tempDic['userName'] = self.userName
		tempDic['broadcasterPort'] = self.broadcasterPort
		userinfofd.write(json.dumps(tempDic))
		userinfofd.close()

	def setNewName(self, newname):
		self.userName = newname


if __name__ == '__main__':
	data = FrogDropData()
	data.initial()
	data.save()
