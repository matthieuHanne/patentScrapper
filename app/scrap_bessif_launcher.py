import scrap_espace_fr
import scrap_espace_word
#import scrap_all_espace
import export_to_xml
import my_mail
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")



def Scrap(mail,export_arg,keywords,databases):
	for i in databases : 
		if i=='f':
			print "googo"
			scrap_espace_fr.scrap_multi_keyword(keywords,"scrap")
		elif i =='w':
			scrap_espace_word.scrap_multi_keyword(keywords,"scrap")
		elif i=='a':
			scrap_all_espace.scrap_multi_keyword(keywords,data_all,"scrap")
	fileid=time.time()
        fileid=('%.*f' % (0, fileid))[:-1]
	export_to_xml.export(export_arg,fileid)
	my_mail.send_mail(mail,keywords,fileid)

def GetKeywordsFromGlobalDatabase() :
	return getkeyword.get()
	

def GetGlobalDatabase(export_arg,mail) :
	fileid=time.time()
	fileid=('%.*f' % (0, fileid))[:-1]
	export_to_xml.export(export_arg,fileid)
	#keywords=getkeyword.get()
	keywords=["all"]
	my_mail.send_mail(mail,keywords,fileid)

def GetNumber(keywords):
	result = 0
	for i in databases : 
		if i=='f':
			result += scrap_espace_fr.scrap_multi_keyword(keywords,"result")
		elif i =='w':
			result +=scrap_espace_word.scrap_multi_keyword(keywords,"result")
		elif i=='a':
			result +=scrap_all_espace.scrap_multi_keyword(keywords,data_all,"result")
	print result
	return result
mail = "benedict.hanser@gmail.com"
export = "ik"
keywordss=["tactile+touchscreen+multitouch","ecran+tactile+projection","tactile+screen+table+projection","screen+multitouch+table"]
databases = "fw"
data_all=["f","wo","ep","lu","es"]
#Scrap(mail,export,keywords,databases)
#GetGlobalDatabase(export,mail)
