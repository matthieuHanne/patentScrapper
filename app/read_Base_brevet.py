import sqlite3
import os, sys

conn = sqlite3.connect('Base_brevet.db')
c = conn.cursor()

def show_brevet():
	try :
		    print "table des brevets"
		    c.execute('SELECT * FROM table_brevet where id=2550')
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)

def show_brevet_spe():
	try :
		    print "table des brevets"
		    #c.execute("SELECT * FROM table_inventeur WHERE name='MATSUOKA TATSUO'")
		    c.execute("SELECT * FROM table_inventeur ORDER by name DESC")
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)


def show_inventeur():
	try :
		    print "table des inventeur"
		    c.execute("SELECT * FROM table_inventeur where id_brevet = 2550")
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)

def show_demandeur():
	try :
		    print "table des demandeur"
		    c.execute("SELECT * FROM table_demandeur where NAME = 'LG ELECTRONICS INC'")
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)

def show_classification_int():
	try :
		    print "table des classification int"
		    c.execute('SELECT * FROM table_classification_int')
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)		    
				    

def show_classification_eur():
	try :
		    print "table des classification eur"
		    c.execute('SELECT * FROM table_classification_eur')
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)
				    
def show_doublon() :
	try :
		    print "doublon\n"
		  #  c.execute('SELECT COUNT(*) AS NBR_DOUBLES, NUM, NOM, PRENOM FROM  GROUP BY NUM,NOM,PRENOM HAVING COUNT(*) > 1')
		    c.execute('SELECT * FROM table_inventeur WHERE ID NOT IN  (SELECT MAX(ID) FROM table_inventeur GROUP BY name) ORDER BY name DESC')
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)
						    

def show_abrege_pour():
	
	try :
		    print "table d'abrege pour"
		    c.execute('SELECT * FROM table_abrege_pour')
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)
				    
				    

def show_keyword():
	try :
		    print "table des keyword"
		    c.execute('SELECT * FROM table_keyword')
		    a= c.fetchone()

		    while a:
			print a
			print '\n'
			a=c.fetchone()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)
				    
				    

def show_all():
	show_brevet()
	show_inventeur()
	show_demandeur()
	show_classification_int()
	show_abrege_pour()
	show_keyword()
	if conn :
		conn.close()



if len(sys.argv) > 2:
     #stripScriptFromHtml( sys.argv[1], sys.argv[2] )
	print "trop d'argument man"
else:
	if len(sys.argv) > 1:
		if sys.argv[1]=='t':
			show_all();
		elif sys.argv[1]=='b':
			show_inventeur()
		elif sys.argv[1]=='ci':
			show_classification_int()
		elif sys.argv[1]=='ce':
			show_classification_eur()
		elif sys.argv[1]=='k':
			show_keyword()
		elif sys.argv[1]=='sp':
			show_brevet_spe()
		elif sys.argv[1]=='a':
			show_abrege_pour()
		elif sys.argv[1]=='d':
			show_doublon()
       # stripscripts( sys.argv[1] )
	else:
 	       print "\nmarque un truc a chercher"
