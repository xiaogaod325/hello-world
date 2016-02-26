__author__ = "xiaogaod325"
import re
import urllib2
class  DOWNLOAD_MOBI:
	def openweb(self,url):
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		pattern = re.compile('href=(.*?)>',re.S)
		print response.read()
		items = re.findall(pattern,response.read())
		for item in items:
            		print item
	def downLoad(self,attachmentUrl,attachmentName):
		attachment=urllib2.urlopen(attachmentUrl)
		localfile=open(DIR+attachmentName,'wb')
		localfile.write(attachment.read())
		localfile.close()

URL='http://www.hi-pda.com/forum/attachment.php?aid=MjQxNTIwN3wzNGU3MWZiNHwxNDU2MDY0MDUyfDNjZWZBczJjVGlnL2NLN1R3bklsTEYxM3JwZFJJUWQ2enRkYk1jMTM3em0yTGMw'
#URL='http://www.baidu.com'
URL='http://www.hi-pda.com/forum/viewthread.php?tid=1811170&extra=page%3D1'
NAME='reborn.mobi'
DIR='/opt/nfs/scull/'

downloadmobi=DOWNLOAD_MOBI()
#downloadmobi.downLoad(URL,NAME)
downloadmobi.openweb(URL)
	
