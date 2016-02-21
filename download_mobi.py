__author__ = "xiaogaod325"
import urllib2
class  DOWNLOAD_MOBI:
	def downLoad(self,attachmentUrl,attachmentName):
		attachment=urllib2.urlopen(attachmentUrl)
		localfile=open(DIR+attachmentName,'wb')
		localfile.write(attachment.read())
		localfile.close()

URL='http://www.hi-pda.com/forum/attachment.php?aid=MjQxNTIwN3wzNGU3MWZiNHwxNDU2MDY0MDUyfDNjZWZBczJjVGlnL2NLN1R3bklsTEYxM3JwZFJJUWQ2enRkYk1jMTM3em0yTGMw'
#URL='http://www.baidu.com'
NAME='reborn.mobi'
DIR='/opt/nfs/scull/'

downloadmobi=DOWNLOAD_MOBI()
downloadmobi.downLoad(URL,NAME)
		
