#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time
import json
import shutil
from pget.down import Downloader

def LLloop ():
	LLqueue = open(os.path.dirname(__file__) + '/cgi-bin/LLprogress', "r+", encoding='utf-8')
	lines = LLqueue.read()
	item = lines.split('\n', 1)[0]
	if len(item) > 10:
		LL_item = json.loads(item)
		url = LL_item[0]
		filename = 'files'+LL_item[1]+'/'+os.path.basename(LL_item[0])
		chunk = int(LL_item[2])
		type = int(LL_item[3])
		print ('Start Downloading ['+url+']')
		if type == 1:
			downloader = Downloader(url, filename, chunk)
			downloader.start()
			downloader.wait_for_finish()
			
		if type == 2:
			LLcurl = 'curl -k ' + url + ' --output ' + filename
			os.system(LLcurl)
			
		datastring = '["' + url + '"' + ',' + '"' + filename + '"' + ',' + '"' + LL_item[2] + '"' + ',' + '"' + LL_item[3] + '"' + "]\n";

		if os.path.isfile(filename):
			LLqueue = open(os.path.dirname(__file__) + '/cgi-bin/LLresult', "a", encoding='utf-8')
			LLqueue.write(datastring)
			LLqueue.close()
		else:
			LLqueue = open(os.path.dirname(__file__) + '/cgi-bin/LLerrors', "a", encoding='utf-8')
			LLqueue.write(datastring)
			LLqueue.close()
		print ('Checking for next ...')

	else:
		print ('Waiting mode ...')
	LLqueue = open(os.path.dirname(__file__) + '/cgi-bin/LLqueue', "r+", encoding='utf-8')
	lines = LLqueue.read()
	new_item = lines.split('\n', 1)[0]
	if len(new_item) > 10:
		LLprogress = open(os.path.dirname(__file__) + '/cgi-bin/LLprogress', "w", encoding='utf-8')
		LLprogress.write(new_item+"\n")
		LLprogress.close()
		LLqueue.close()
		LLqueue_old = open(os.path.dirname(__file__) + '/cgi-bin/LLqueue', "r+", encoding='utf-8')
		LLqueue_old.readline()
		new_LLqueue = open(os.path.dirname(__file__) + '/cgi-bin/LLqueue', "w", encoding='utf-8')
		shutil.copyfileobj(LLqueue_old, new_LLqueue)
	else:
		LLprogress = open(os.path.dirname(__file__) + '/cgi-bin/LLprogress', "w", encoding='utf-8')
		LLprogress.write(''+"\n")
		LLprogress.close()
		print ('No new Item !')
	time.sleep(1)
		
while True:
	LLloop()
	time.sleep(1)