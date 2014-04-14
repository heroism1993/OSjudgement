import github_discover as discover
import github_collector as collector
from github_global import CYCLE_TIME
import time

host='imap.163.com'
user='gaochao1993@163.com'
passwd='1993425'

fro='heroism.1993@gmail.com'
mailbox=discover.login(host,user,passwd)
while (True):
    discover.search(mailbox,fro)
    time.sleep(CYCLE_TIME)
    
