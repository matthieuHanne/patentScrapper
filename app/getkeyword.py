#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Document 

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def get():
		
	conn = sqlite3.connect("temp/Base_brevet.db")
	cur = conn.cursor()
	current_n_id=0
	current_e_id=0


	request1 = "SELECT * from table_keyword ORDER BY NAME"
	cur.execute(request1)
	item =cur.fetchone()
	keywords=[]
	old_keyword=str(item[1])
	while item:
		new_keyword=str(item[1])
		if old_keyword!=new_keyword :
			keywords+=[""+new_keyword+""]
			old_keyword=new_keyword
		item=cur.fetchone()
	return keywords




