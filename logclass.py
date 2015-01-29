import re

# A Class that takes a string and returns a Common Log interpretation of the data
class LogFile:
	"""
	>>> LogFile("123.23.4.567").remotehost
	'123.23.4.567'
	>>> LogFile('[28/May/2014:18:12:26 +0000]').date
	'28/May/2014:18:12:26 +0000'
	>>> test = LogFile('127.0.0.1 user-identifier frank_the_man [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326')
	>>> test.remotehost
	'127.0.0.1'
	>>> test.logname
	'user-identifier'
	>>> test.username
	'frank_the_man'
	>>> test.date
	'10/Oct/2000:13:55:36 -0700'
	>>> test.request
	'GET /apache_pb.gif HTTP/1.0'
	>>> test.status
	'200'
	>>> test.statustype
	'succesful'
	>>> test.bytes
	'2326'
	"""
	def __init__(self, string):
		self.string = string

	@property
	def remotehost(self):
		remotehost = re.search('\d+\.\d+\.\d+\.\d+', self.string)
		if remotehost != None:
			remotehost = remotehost.group()
		return remotehost

#NOTE: Currently cannot deal with abnormal logname and usernames- such as "user-i\dentifier"
	@property
	def logname(self):
		logname = re.search('\d+\.\d+\.\d+\.\d+\s([\w-]+)\s', self.string)
		if logname != None:
			logname = logname.group(1)
		return logname

	@property
	def username(self):
		if self.logname:
			username = re.search(self.logname + '\s([\w-]+)\s', self.string)
		else:
			username = re.search('\s([\w-]+)\s', self.string)
		if username != None:
			username = username.group(1)
			if username == self.status:
				username = None
		return username


	@property
	def date(self):
		date = re.search('\[([\w\W]+)\]',self.string)
		if date != None:
			date = date.group(1)
		return date
	
	@property
	def request(self):
		request = re.search('\"([\w\W]+)\"', self.string)
		if request != None:
			request = request.group(1)
		return request

	@property
	def status(self):
		statustypeD = {'2':'succesful', '3':'redirection', '4':'client error', '5':'server error'}
		status = re.search('\s([2345])(\w\w)\s', self.string)
		if status != None:
			statusind = status.group(1)
			self.statustype = statustypeD[statusind]
			status = statusind + status.group(2)
		return status

	@property
	def bytes(self):
		bytes = re.search('(\d+)$', self.string)
		if bytes != None:
			bytes = bytes.group(1)
		return bytes



