#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import cgi
import json
import LLsession

print ("Content-type: text/html"); print ()
formdata = cgi.FieldStorage()

if "act" in formdata:
	LL_action = formdata["act"].value

	if LL_action == 'login':
		if LLsession.login == True:
			print (1)
		else:
			print (LLsession.erorr)
	else:
		if LLsession.login == True:
			
			if LL_action == 'addQueue':
				if "url" in formdata:
					url = formdata["url"].value
					if "path" in formdata:
						path = '/' + formdata["path"].value + '/'
					else:
						path = '/'
					if "conc" in formdata:
						conc = formdata["conc"].value
					else:
						conc = 2
					if "type" in formdata:
						type = formdata["type"].value
					else:
						type = 1
					datastring = '["' + url + '"' + ',' + '"' + path + '"' + ',' + '"' + conc + '"' + ',' + '"' + type + '"' + "]\n";
					LLqueue = open(os.path.dirname(__file__) + './LLqueue', "a", encoding='utf-8')
					LLqueue.write(datastring)
					LLqueue.close()
					print (1)
				else:
					print ('Please Input URL !')
					
					
			if LL_action == 'delQueue':
				formdata = cgi.FieldStorage()
				if "tu" in formdata:
					tu = formdata["tu"].value
					LLqueue = open(os.path.dirname(__file__) + './LLqueue', "r+", encoding='utf-8')
					lines = LLqueue.readlines()
					datastring = ''
					count = 0
					for item in lines:
						itemJson = json.loads(item)
						if itemJson[0] != tu:
							datastring = datastring + item
						else:
							count += 1
					LLqueue.close()
					LLqueue = open(os.path.dirname(__file__) + './LLqueue', "w", encoding='utf-8')
					LLqueue.write(datastring)
					LLqueue.close()
					print(count)
				else:
					print('No Target Link')

					
			if LL_action == 'list':
				if "list" in formdata:
					LL_list_type = formdata["list"].value
					LLlist = open(os.path.dirname(__file__) + './LL'+LL_list_type, "r+", encoding='utf-8')
					lines = LLlist.read().replace('\n', ',')
					offset = len(lines) - 1
					lines = lines[:offset]
					print("[")
					print(lines)
					print("]")
					LLlist.close()
		else:
			print (LLsession.erorr)
else:
	print ('No Action !')
