# -*- coding: utf-8 -*- 
import smtplib
from urllib2 import Request, urlopen, URLError, HTTPError
import urllib2
import os.path
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(addr , keywords,number_file):
	#assert isinstance(send_to, list)
	#assert isinstance(files, list)
	files=["temp/temp_node_"+str(number_file)+".csv","temp/temp_edge_"+str(number_file)+".csv"]
	text = "Veuillez-trouvez ci-joint les fichiers les fichiers temp_node.csv et temp_edge.csv\n généré par la recherche des mots clefs suivants:\n "
	for i in keywords : 
		if i!='\n':
			text+="\n\t-"+str(i)
	text +="\n\nLes fichiers sont des fichier csv directement importable depuis Gephi .pour ce faire  :\n\n- créer un nouveau projet\n- aller dans l\'onglet \" Data laboratory\"\n- cliquer sur \"ImportSpreadSheet\"\n- selectionner le premier fichier cvs : temp_node.csv ( attention , il faut commencer par importer le fichier de noeud avant le fichier de lien )\n- Selectionner \n\t- separator : comma \n\t- as table : nodes table  \n\t- Charset : UTF-8- \n- Enfin cliquer sur \"next\" puis \"finish\"\n- Faire de meme pour le fichier de lien : temp_edge.csv ( attention a bien selectionner as table : edges table)"
	
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
	except:
		print "failed to send mail"

send_to=["benedict.hanser@gmail.com"]
send_from="PR.crawler@gmail.com"






