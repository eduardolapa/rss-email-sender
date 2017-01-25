#!/usr/bin/python2
#encoding: utf-8
import feedparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys

def envia_mail(log, email):
	fromaddr = 'emailfrom@email.com.br'
	toaddrs  = email
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Subject'
	msg['From'] = fromaddr
	msg['To'] = email
	part1 = MIMEText(log, 'html')
	msg.attach(part1)
	username = 'emailfrom@email.com.br'
	password = 'pass'
	try:
		server = smtplib.SMTP('smtp.email.com.br:587')
	except:
		return
	server.ehlo()
	server.starttls()
	try:
		server.login(username, password)
	except:
		return
	try:
		server.sendmail(fromaddr, email, msg.as_string())
	except:
		return
	server.quit()

def dir_exe():
	return os.path.dirname(sys.argv[0])

data_old = []
d = feedparser.parse('http://url.com/feed')
email_arq = open(dir_exe() + '/emails.txt', 'r')
email_lista = email_arq.read().split(';')
try:
    if not d.entries[0].published in data_old:
	    data_old.append(d.entries[0].published)
		assunto = d.entries[0].title.encode('utf-8') +' '+ d.entries[0].description.encode('utf-8') + d.entries[0].link.encode('utf-8')
		for email in email_lista:
			envia_mail(assunto, email)
except: 
		pass



