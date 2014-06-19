import scrap_espace_fr
import scrap_espace_word
#import scrap_all_espace
import getkeyword
import export_to_xml
import create_table
import get_base_name
import my_mail
import sys,os
import time
reload(sys)
sys.setdefaultencoding("utf-8")



def Scrap(mail,export_arg,keywords,databases,number_base):

	if not os.path.exists("./temp/Base/Base_brevet_"+str(number_base)+".db"):
		create_table.create_base(number_base)
		print "create new"
	for i in databases : 
		if i=='f':
			print "googo"
			scrap_espace_fr.scrap_multi_keyword(keywords,"scrap",number_base)
		elif i =='w':
			scrap_espace_word.scrap_multi_keyword(keywords,"scrap",number_base)
		elif i=='a':
			scrap_all_espace.scrap_multi_keyword(keywords,data_all,"scrap",number_base)
	fileid=time.time()
        fileid=('%.*f' % (0, fileid))[:-1]
	export_to_xml.export(export_arg,fileid,number_base)
	my_mail.send_mail(mail,keywords,fileid,1)
	

def GetKeywordsFromGlobalDatabase(number_base) :
	return  getkeyword.get(number_base)
	
def GetListBases():
	return get_base_name.get()

def GetGlobalDatabase(export_arg,mail,number_base) :
	fileid=time.time()
	fileid=('%.*f' % (0, fileid))[:-1]
	export_to_xml.export(export_arg,fileid,number_base)
	#keywords=getkeyword.get()
	keywords=["all"]
	my_mail.send_mail(mail,keywords,fileid,2)

def GetNumber(keywords):
	result = 0
	for i in databases : 
		if i=='f':
			result += scrap_espace_fr.scrap_multi_keyword(keywords,"result",0)
		elif i =='w':
			result +=scrap_espace_word.scrap_multi_keyword(keywords,"result",0)
		elif i=='a':
			result +=scrap_all_espace.scrap_multi_keyword(keywords,data_all,"result",0)
	print result
	return result
mail = "benedict.hanser@gmail.com"
export = "k"
keywordss=["Alstom","Gec+Alsthom","Alstom+Transport","Alstom+Grid","Alstom+Thermal+Power","Alstom+Renewable+Power"]
databases = "w"
data_all=["f","wo","ep","lu","es"]
#GetNumber(keywordss)
#GetKeywordsFromGlobalDatabase("alstom")
#Scrap(mail,export,keywordss,databases,"alstom")
#GetGlobalDatabase(export,mail,"alstom")
