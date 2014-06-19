# -*- coding: utf-8 -*- 
import smtplib
from urllib2 import Request, urlopen, URLError, HTTPError
import urllib2
import os.path
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(addr , keywords,number_file,type_request):
	#assert isinstance(send_to, list)
	#assert isinstance(files, list)
	files=["temp/temp_node_"+str(number_file)+".csv","temp/temp_edge_"+str(number_file)+".csv"]
	if type_request == 1:
		text = "Veuillez-trouvez ci-joint les fichiers les fichiers temp_node.csv et temp_edge.csv\n génrés par la recherche des mots clefs suivants:\n "
		for i in keywords : 
			if i!='\n':
				text+="\n\t-"+str(i)
	elif type_request == 2:
		text="Veuillez-trouvez ci-joint les fichiers les fichiers temp_node.csv et temp_edge.csv\n g "
	text +="\n\nLes fichiers sont des fichier csv directement importables depuis Gephi .Pour ce faire  :\n\n- Créez un nouveau projet\n- allez dans l\'onglet \" Data laboratory\"\n- Cliquez sur \"ImportSpreadSheet\"\n- Selectionnez le premier fichier cvs : temp_node_XX.csv ( attention , il faut commencer par importer le fichier de noeuds avant le fichier de liens )\n- Selectionnez \n\t- Separator : comma \n\t- As table : nodes table  \n\t- Charset : UTF-8- \n- Enfin cliquez sur \"next\" puis \"finish\"\n- Faire de meme pour le fichier de liens : temp_edge.csv ( attention à bien selectionner as table : edges table)"
	
	send_to=[addr]
	msg = MIMEMultipart()
	msg['From']='PR.crawler@gmail.com'
	msg['To'] = COMMASPACE.join(send_to)
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = "scrap de brevet fini"
	gmail_user = "PR.crawler@gmail.com"
	gmail_pwd = "banane60200"
	
	msg.attach( MIMEText(text))

	for f in files:
		print f
		part = MIMEBase('application', "octet-stream")
		part.set_payload( open(f,"rb").read() )
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
		msg.attach(part)
	try:
		print 0
		smtp = smtplib.SMTP("smtp.gmail.com",587)
		smtp.ehlo()
		print 1	
		smtp.starttls()
		print 2
		smtp.login(gmail_user, gmail_pwd)
		print 3
		smtp.sendmail(send_from, send_to, msg.as_string())
		smtp.close()
		print 'successfully sent the mail'
		os.remove('temp/temp_node_'+str(number_file)+'.csv')
		os.remove('temp/temp_edge_'+str(number_file)+'.csv')
	except:
		print "failed to send mail"

send_to=[""]
send_from="PR.crawler@gmail.com"






