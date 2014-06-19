import sqlite3


def create_base(base_number):

	try:
		conn = sqlite3.connect('temp/Base/Base_brevet_'+str(base_number)+'.db')
		c = conn.cursor()
		c.execute('''CREATE TABLE table_brevet(id INTEGER PRIMARY KEY ASC,signet text,date text, num_demande text,num_priorite text,contenu text , link text )''')

		c.execute('''CREATE TABLE table_inventeur(id INTEGER PRIMARY KEY ASC , name TEXT ,id_brevet INTEGER)''')
		c.execute('''CREATE TABLE table_demandeur(id INTEGER PRIMARY KEY ASC , name TEXT ,id_brevet INTEGER)''')
		c.execute('''CREATE TABLE table_classification_int(id INTEGER PRIMARY KEY ASC , name TEXT , id_brevet INTEGER)''')
		c.execute('''CREATE TABLE table_classification_eur(id INTEGER PRIMARY KEY ASC , name TEXT , id_brevet INTEGER)''')
		c.execute('''CREATE TABLE table_abrege_pour(id INTEGER PRIMARY KEY ASC , name TEXT , id_brevet INTEGER)''')
		c.execute('''CREATE TABLE table_keyword(id INTEGER PRIMARY KEY ASC , name TEXT , id_brevet INTEGER)''')


	except sqlite3.Error as e:
			       
		if conn:
			conn.rollback()
			print 'Error %s' % e    
			sys.exit(1)
			    
			    
	finally:
			    
		if conn:
			conn.close()	

