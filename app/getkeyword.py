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
	while item:
		keywords+=[""+item[1]+""]
		item=cur.fetchone()
	return keywords

get()
