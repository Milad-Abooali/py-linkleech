#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import cgi

def clearfy (val):
	offset = len(val) - 1
	return val[:offset]
f = open(os.path.dirname(__file__) + '/../admin.pass', "r+", encoding='utf-8')
username_s = f.readline(); password_s = f.readline(); f.close()

formdata = cgi.FieldStorage()
if "f" in formdata:
	if "u" in formdata:
		username_r = formdata["u"].value
		if "p" in formdata:
			password_r = formdata["p"].value
			if username_r == clearfy(val=username_s) :
				if password_r == password_s :
					login = True; erorr = False
				else:
					login = False; erorr = 'Password Is Wrong'
			else:
				login = False; erorr = 'Please Login !'
		else:
			login = False; erorr = 'Password Not Definded'
	else:
		login = False; erorr = 'Username Not Definded'
else:
	handler = {}
	if 'HTTP_COOKIE' in os.environ: 
		cookies = os.environ['HTTP_COOKIE']
		cookies = cookies.split('; ')
		for cookie in cookies:
			cookie = cookie.split('=')
			handler[cookie[0]] = cookie[1]
		if "u" in handler:
			username_r = handler['u']
			if "p" in handler:
				password_r = handler['p']
				if username_r == clearfy(val=username_s) :
					if password_r == password_s :
						login = True; erorr = False
					else:
						login = False; erorr = 'Password Is Wrong'
				else:
					login = False; erorr = 'Please Login !'
			else:
				login = False; erorr = 'Password Not Definded'
		else:
			login = False; erorr = 'Username Not Definded'