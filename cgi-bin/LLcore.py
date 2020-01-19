#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import LLsession;

print ("Content-type: text/html"); print ()

if LLsession.login == True:
	f = open(os.path.dirname(__file__) + './LLcore', "r+", encoding='utf-8')
	page = f.read();
	print (page)
else:
	print (LLsession.erorr)
