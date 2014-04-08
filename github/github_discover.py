import imaplib
import email
import string,re

host='imap.163.com'
user='gaochao1993@163.com'
passwd='1993425'


def emailbody(message):
    for part in message.walk():
        if not part.is_multipart():
            charset=part.get_charset()
            contenttype=part.get_content_type()
            return part.get_payload(decode=True)



def getlink(message):
    for msg in message.split('\n'):
        temp=msg.split()
        if(temp[0]=='git' and temp[1]=='pull'):
            return temp[2]

mailbox=imaplib.IMAP4_SSL(host)
try:
    try:
        mailbox.login(user,passwd)
    except Exception ,e:
        print 'login error: %s' % e
    
    mailbox.select('INBOX')
    typ,data=mailbox.search(None,'UNSEEN')
    print data
    print '\n\n\n\n'
    pattern = re.compile(r'^[^<]*<heroism.1993@gmail.com>$')
    
    for num in string.split(data[0]):
        print num
        print '\n\n\n\n\n'
        try:
            typ,msg=mailbox.fetch(num,'(RFC822)')
            mailmsg=email.message_from_string(msg[0][1])
            if(pattern.match(mailmsg['FROM'])):
                print getlink(emailbody(mailmsg))
                
        except Exception, e:
            print 'fetch error: %s' % e

except Exception , e:
    print 'imap error: %s' %e
