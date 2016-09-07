#!/usr/bin/python

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, text
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy import insert
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from datetime import datetime
from sqlalchemy import DateTime

import hashlib
import urllib
import urllib2
import os
import re
import datetime
import calendar
import time

from bs4 import BeautifulSoup

import smtplib
import pymysql

response = urllib.urlopen("http://it-ebooks.info/")

m = hashlib.md5()

soup = BeautifulSoup(response.read())
tag = soup.find_all("td", attrs={"class": "top"})
print str(tag)
m.update(str(tag))

engine = create_engine('mysql+pymysql://user:password@localhost/database_name')

check_duplicate = engine.execute("SELECT MAX(id) FROM %s " % 'itebooks')

for i in check_duplicate:
print i[0]
row = engine.execute("SELECT * FROM {} WHERE id = {}".format('itebooks', str(i[0])))

for i in row:
print i[1]
if m.hexdigest() != i[1]:
print "time to update"
engine.execute("INSERT INTO {} ({}) VALUES ('{}')".format('itebooks', 'checker', m.hexdigest()))
msg = 'it-ebooks has updated.'

server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('from@gmail.com','password')
server.sendmail('from@gmail.com','to@gmail.com',msg)
server.close()

else:
print "no need to update"
