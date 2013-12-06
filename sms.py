#sms.py
#Michael Van Veen
#11/26/05
#Library for receiving mail from cell phone
import imaplib

mailserver = "mail.phr4g.net"
logindata = ["sms+phr4g.net", "passwenthere"]
cellnumber = "7609949051@vtext.com"
Mail = imaplib.IMAP4(mailserver)

def login():
	'''Login to IMAP server, only needs to be called once
	'''
	Mail.login(logindata[0], logindata[1])
	Mail.select()

def logout():
	'''Log out of IMAP server, only needs to be called once
Once logged out, unable to use any other commands
	'''
	Mail.logout()

def getmessage(message):
	'''Get any messages in mailbox from cellphone
	'''
	typ, data = Mail.search(None, '(FROM ' + cellnumber + ')')
	for num in data[0].split():
	    typ, data = Mail.fetch(num, '(BODY[TEXT])')
	    temp = (data[0][1].replace('\n', "").replace('\r', ""))
	    message.append(temp)

def delete():
	'''Delete any messages in mailbox from cellphone
	'''
	typ, data = Mail.search(None, '(FROM ' + cellnumber + ')')
	for num in data[0].split():
		Mail.store(num, '+FLAGS', '\\Deleted')
	Mail.expunge()

def getmail(message):
	login()
	getmessage(message)
	delete()
	logout()
