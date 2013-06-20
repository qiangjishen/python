# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup

import urllib
import urllib2



url = 'http://ip.xpcha.com/'
values = {'q':'218.241.97.42'}

data = urllib.urlencode(values)



req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = BeautifulSoup(response.read())


readall = the_page.find_all('p')
    

print '======================================='

print readall[0].get_text()
print readall[1].get_text()

print '======================================='



import sys, socket
try:
    result =socket.getaddrinfo('www.cnnic.cn', None, 0, socket.SOCK_STREAM)
    counter =0;
    for item in result:
        print"%-2d: %s"%(counter, item[4][0])
        counter +=1
except:
    print r'解析失败'
    
    
    








