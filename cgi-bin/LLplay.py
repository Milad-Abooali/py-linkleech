#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import shutil

LLqueue = open(os.path.dirname(__file__) + './LLqueue', "r+", encoding='utf-8')
lines = LLqueue.read()
item = lines.split('\n', 1)[0]
LLprogress = open(os.path.dirname(__file__) + './LLprogress', "w", encoding='utf-8')
LLprogress.write(item+"\n")
LLprogress.close()
LLqueue.close()
LLqueue_old = open(os.path.dirname(__file__) + './LLqueue', "r+", encoding='utf-8')
LLqueue_old.readline()
new_LLqueue = open(os.path.dirname(__file__) + './LLqueue', "w", encoding='utf-8')
shutil.copyfileobj(LLqueue_old, new_LLqueue)