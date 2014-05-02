#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import os, sys
#import psycopg2
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

photoname = 1


g=open("temp/log_espace_fr.log",'wb') 


def scrap_url(url,numberbrevet,type_file,keyword):
        foundbalise = 0
        error=0
        foundtitle = 0
        download_ok=0 
       
        while not download_ok or error>3:

                print "download page.. :"+str(url)
                try : 
                        req = urllib2.Request(url)
                        u = urllib2.urlopen(req)
                        meta = u.info() 
                        print "..done\n"
                        download_ok=1
                except urllib2.HTTPError, e:
                        error+=1
                        print "error"
                except urllib2.URLError, e:
                        error+=1
                        print "error"
                print "try number "+str(error)+"/3"
                if error>3:
                        g.write("could\'nt download :\n "+url)
                        break

  
	
		    
	if download_ok :
	
		if type_file == 1:
			#fichier temporaire : page de resultat de recherche
			f = open("temp/temp", 'wb')	
			buffer = u.read()
			f.write(buffer)
			f.close()
			return 1
		elif type_file == 2:
			#fichier de brevet
			u.read(500)
			signet = ""
			while not foundtitle :
				temp=u.read(1)
				if temp =='&':
					test="nbsp;-"
					if u.read(len(test))==test:
						foundtitle = 1	
						u.read(37)
						foundendtitle = 0 
						listsignet=[]
						while not foundendtitle :
							test="   "
							temp = u.read(len(test))
							if temp==test:
								foundendtitle = 1;
							else :
								listsignet+=temp
			founddate=0
			print "found title\n"
			while not founddate :
				temp = u.read(1)
				if temp==':' :
					u.read(46)
			 		date=u.read(10)
					founddate=1
			foundinventeur=0
			print "found date\n"
			cmpt=0
			while not foundinventeur :
				temp = u.read(1)
				if temp==':' :
					test="none\">"
					temp = u.read(len(test))
					if temp==test:
						while not foundinventeur :
							temp=u.read(1)
							if temp=='(':
								foundinventeur=1
				elif temp=='<' :
					cmpt+=1
					if cmpt==10:
						break
			listinventeur=[]
			foundendinventeur=0
			if cmpt!=10:
				while not foundendinventeur :
							test=')'
							temp = u.read(len(test))
							if temp==test:
								foundendinventeur = 1;
							else :
								listinventeur+=temp
			else:
				 listinventeur="NULL"
			founddemandeur=0
		
		
			print "found inventeur\n"
			cmpt=0
			while not founddemandeur :
				temp = u.read(1)
				if temp==':' :
					test="none\">"
					temp = u.read(len(test))
					if temp==test:
						while not founddemandeur :
							temp=u.read(1)
							if temp=='(':
								founddemandeur=1
				elif temp=='<' :
					cmpt+=1
					if cmpt==10:
						break				
		
		 	
				
		
			listdemandeur=[]
			foundenddemandeur=0
			if cmpt!=10 :
				while not foundenddemandeur :
						test=')'
						temp = u.read(len(test))
						if temp==test:
							foundenddemandeur = 1;
						else :
							listdemandeur+=temp
			else :
				listdemandeur="NULL"	
			listclassification_int=[]
			founddemandeur=0
			foundfirst=0
			cmpt=0
			cmpt2=0
			print "found demandeur\n"
			while not founddemandeur :
					temp = u.read(1)
					if temp=='<' :
						test="i>"
						temp = u.read(len(test))
						if foundfirst :
							cmpt2+=1
							if cmpt2==4:
								founddemandeur=1
								print "exit"
						
						if temp==test:
							u.read(3)
							foundfirst=0
							while not foundfirst :
								temp=u.read(1)
								if temp=='<':
									foundfirst=1
									cmpt2=0
									cmpt=0	
	
								else: 
									listclassification_int+=temp
					
						else :
							cmpt+=1
							if cmpt>13 :
								founddemandeur=1
					
						 
					
					
			print" found classification int\n"	
			print listclassification_int					
			founddemandeur=0
			foundfirst=0
			cmpt2=0
			cmpt=0
			listclassification_eur=[]
			while not founddemandeur :
					temp = u.read(1)
					if temp=='<' :
						test="i>"
						temp = u.read(len(test))
						if foundfirst :
							cmpt2+=1
							if cmpt2==3:
								founddemandeur=1
								print "exit"
						
						if temp==test:
							u.read(3)
							foundfirst=0
							while not foundfirst :
								temp=u.read(1)
								if temp=='<':
									foundfirst=1
									cmpt2=0
									cmpt=0	
	
								else: 
									listclassification_eur+=temp
					
						else :
							cmpt+=1
							if cmpt>8 :
								founddemandeur=1
					
						 
					
					
			print" found classification eur\n"
			print listclassification_eur
			founddemandeur=0
			cmpt2=0
			cmpt=0
			numdemande=""
			while not founddemandeur :
					temp = u.read(1)
					if temp==':' :
						u.read(32)
						while not founddemandeur :
							temp=u.read(1)
							if temp=='&':
								founddemandeur=1
						
							else: 
								numdemande+=temp
			print" found numdemande \n"	
			print numdemande
			founddemandeur=0
			numpriorite=""				
			while not founddemandeur :
					temp = u.read(1)
					if temp==':' :
						u.read(64)
						while not founddemandeur :
							temp='e'
							temp=u.read(1)
							if ord(temp)==10:
								founddemandeur=1
						
							else: 
								numpriorite+=temp
			
			print" found numpriorite \n"	
			print numpriorite	
			founddemandeur=0
			abregepour=""
			cmpt=0
			while not founddemandeur :
					temp = u.read(1)
					if temp=='A' :
						test="br"
						temp = u.read(len(test))
						if temp==test:
							u.read(47)
							while not founddemandeur :
								temp=u.read(1)
								if ord(temp)==10:
									cmpt+=1	
									if cmpt==3:
										founddemandeur=1
								elif temp==' ':
									pass
								elif temp=='&':
									u.read(6)
						
								else: 
									abregepour+=temp
			print" found abrege pour\n"	
			founddemandeur=0
			listcontenu=[]
			while not founddemandeur :
					temp = u.read(1)
					if temp=='<' :
						test="p>"
						temp = u.read(len(test))
						if temp==test:
							while not founddemandeur :
								temp=u.read(1)
								if temp=='<':
									founddemandeur=1
								
								else: 
									listcontenu+=temp
			print" found contenu\n"	
			for i in listsignet :
				if ord(i)==10 :
					break			
				elif ord(i)==39:
					signet+=" "
				elif ord(i)==243:
					signet+='o'
				elif i=='\'':
					pass
				elif i=='\"':
					pass
				elif i==',':
					signet+=" "
			
				else :
					signet+=i
			inventeur =""
			inventeurs=[]	
			new_inventeur=1
			for i in listinventeur :
			
				if   i=='\'':
					new_inventeur = 0
					pass
				elif ord(i)==39:
					new_inventeur = 0
					signet+=" "
				elif i==',':
					new_inventeur = 0
					pass	
				elif i==';' :
					inventeurs+=[inventeur]
					inventeur=""
					new_inventeur = 1
				elif i==' ' and new_inventeur :
					new_inventeur=0
					pass	
				else :
					inventeur+=i
			inventeurs+=[inventeur]	

			demandeur=""
			demandeurs=[]
			new=1
			for i in listdemandeur :
				
				if new and i==' ':
					new=0
					pass
				else:
					new=0
					if   i=='\'':
						demandeur+=" "
					elif i==',':
						pass	
					elif ord(i)==39:
						signet+=" "
					elif i==';' :
						demandeurs+=[demandeur]
						demandeur=""
						new=1
					
					else :
						demandeur+=i
			
			demandeurs+=[demandeur]
			classification_int=""
			classification_ints=[]
			new=1
			for i in listclassification_int :
				if new and i==' ':
					new=0
					pass
				else :
		
					if   i=='\'':
						pass
					elif i==',':
						pass	
					elif i==';' :
						classification_ints+=[classification_int]
						classification_int=""
						new=1
					else :
						classification_int+=i
			classification_ints+=[classification_int]
			
			contenu=""
			for i in listcontenu :
			
				if   i=='\'':
					contenu+=" "
				elif i==',':
					pass
				elif ord(i)==39:
					signet+=" "
				elif i==';' :
					contenu+=" "	
				else :
					contenu+=i

			classification_eur=""
			classification_eurs=[]
			new=1
			for i in listclassification_eur :
				if new and i==' ':
					new=0
					pass
				else :
					if   i=='\'':
						pass
					elif i==',':
						pass	
					elif i==';' :
						classification_eurs+=[classification_eur]
						classification_eur=""	
						new=1
					else :
						classification_eur+=i
			classification_eurs+=[classification_eur]
			
			print "contenu du titre: \n"
			print signet					
			print "inventeur :\n"
			for i in inventeurs :
				print i
			print "demandeurs :\n"
			for i in demandeurs :
				print i	
			print "classification inters :\n"
			for i in classification_ints :
				print i		
			print "classification eurs :\n"	
			for i in classification_eurs :
				print i	
			print "numdemande :\n"
			print numdemande			
			print "numpriorite :\n"
			print numpriorite	
			print "abregepour :\n"
			print abregepour	
			print "contenu :\n"
			print contenu	

			# cas 1 nouveau brevet
			# cas 2 brevet deja vu mais keyword different
			# cas 3 brevet deja vu et meme keyword
			try:	
				
				conn = sqlite3.connect('temp/Base_brevet.db')
				c = conn.cursor()
		
				request1 = "SELECT id from table_brevet WHERE signet='"+signet+"'"
				c.execute(request1)
				a= c.fetchone()
				if a :
					print "id brevet : "+ str(a[0])
					request1 = "SELECT * from table_keyword WHERE id_brevet='"+str(a[0])+"' AND name='"+keyword+"'"
					c.execute(request1)
					b= c.fetchone()
					print b
					if b :
						print "already in the database"
					else :
						request2 = "INSERT INTO table_keyword(NAME,ID_BREVET) VALUES('"+keyword+"','"+str(a[0])+"')"
						c.execute(request2)
			
				else : 	
					request1 = "INSERT INTO table_brevet(SIGNET,DATE ,NUM_DEMANDE,NUM_PRIORITE,CONTENU,LINK) VALUES ('"+signet+"','"+date+"','"+numdemande+"','"+numpriorite+"','"+contenu+"','"+url+"')"
		
					c.execute(request1)
					brevet_id=c.lastrowid
					for i in inventeurs :
						request2 = "INSERT INTO table_inventeur(NAME,ID_BREVET) VALUES ('"+i+"','"+str(brevet_id)+"')"
						if i and i!=' ':
							c.execute(request2)
					for i in inventeurs :
						request2 = "INSERT INTO table_demandeur(NAME,ID_BREVET) VALUES ('"+i+"','"+str(brevet_id)+"')"
						if i and i!=' ':
							c.execute(request2)

					for i in classification_ints :
						request2 = "INSERT INTO table_classification_int(NAME,ID_BREVET) VALUES ('"+i+"','"+str(brevet_id)+"')"
						if i and i!=' ':
							c.execute(request2)
					for i in classification_eurs :
						request2 = "INSERT INTO table_classification_eur(NAME,ID_BREVET) VALUES ('"+i+"','"+str(brevet_id)+"')"
						if i and i!=' ':
							c.execute(request2)
			
				    	request2 = "INSERT INTO table_abrege_pour(NAME,ID_BREVET) VALUES('"+abregepour+"','"+str(brevet_id)+"')"
					if abregepour and abregepour!=' ':
						c.execute(request2)
					request2 = "INSERT INTO table_keyword(NAME,ID_BREVET) VALUES('"+keyword+"','"+str(brevet_id)+"')"
					c.execute(request2)
			
			    
			    # Insert a row of data
			#    c.execute(request)
		    
			    # Save (commit) the changes
				conn.commit()
			    
			    # We can also close the connection if we are done with it.
			    # Just be sure any changes have been committed or they will be lost.
				conn.close()  
			
			    
			except sqlite3.Error as e:
			       
			    if conn:
				conn.rollback()
			    print 'Error %s' % e    
			    sys.exit(1)
			    
			    
			finally:
			    
			    if conn:
				conn.close()	


    		elif type_file == 3:

			temp = u.read()
			number = temp.split('<div class=\"primary\">')[1].split('<p>')[1].split('r')[0][114:-1]
			
			while number[0]==' ':
				number=number[1:]
			
			try:
				number = int(number)
			except ValueError :
				number = 1000
			 			
			return number
				
		



def parcour_page(url,numberbrevet,keyword):
	photoname=0
	download_ok=0	
	download_ok=scrap_url(url,numberbrevet,1,keyword)
	if download_ok :	
		f = open("temp/temp", 'rb')
		i=1
		wk=""
		brevet=0
		newpage=0
		just_balise = 0 
		addr=""
		cmpt_newpage=0
		while True:

			temp = f.read(i)
			if not temp:
				break
			just_balise=0
			if temp=='<':
				just_balise=1
			if temp=='>':
				if brevet :
					addr+='\n'
					brevet=0
					newpage=0
			if just_balise and not brevet and not newpage :
				wk=str(f.read(12))
				if wk=="a href=\"/pub":
					brevet = 1
					numberbrevet+=1
					print '\n'+"numberbrevet="+str(numberbrevet)
					#print temp
				if wk=="a id=\"nextPa":
					newpage=1
					f.read(37)
			if brevet and not just_balise :

				if temp=='\"':
			
				
					addr="http://fr.espacenet.com/pub"+addr
					print addr
					scrap_url(str(addr),numberbrevet,2,keyword)
					addr=""
					brevet=0
			
				else :
					if temp=='&':
						f.read(4)
					addr+=temp	
			if newpage and not just_balise :

				if temp=='\"':
			
					print "go to nextpage"
					addr="http://fr.espacenet.com/"+addr
					print addr
					cmpt_newpage+=1
					if cmpt_newpage==2:
						parcour_page(str(addr),numberbrevet,keyword)
					addr=""
					newpage=0
				else :
					addr+=temp
				
	return numberbrevet


def recherche (keyword,type_recherche) :
	numberbrevet = 0 
	print "let's go"
	if type_recherche == "scrap":
		parcour_page("http://fr.espacenet.com/searchResults?&ST=singleline&compact=false&query="+keyword+"&locale=fr_FR&DB=fr.espacenet.com",numberbrevet ,keyword)
		return 0
	elif type_recherche == "result":
		return scrap_url("http://fr.espacenet.com/searchResults?&ST=singleline&compact=false&query="+keyword+"&locale=fr_FR&DB=fr.espacenet.com",numberbrevet,3,keyword)	
			
	print "scrap done"
	


#def scrap_multi_keyword():
#	keyword_file = open('keyword.txt')
#	for word in keyword_file :
#		print "\n\n"+word
#		recherche(str(word[0:-1]))

#scrap_multi_keyword()

def scrap_multi_keyword(keywords,type_recherche):
	result = 0 	
	for word in keywords :
		result+=recherche(word,type_recherche)
	return result
			
#if len(sys.argv) > 2:
     #stripScriptFromHtml( sys.argv[1], sys.argv[2] )
#	print "trop d'argument man"
#else:
#	if len(sys.argv) > 1:
#		recherche(str(sys.argv[1]))
#       # stripscripts( sys.argv[1] )
#	else:
# 	       print "\nmarque un truc a chercher"





	


