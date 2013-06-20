#! /usr/bin/env python

import urllib2
import webbrowser

proxy_support = urllib2.ProxyHandler({'https':'http://127.0.0.1:8087'})
opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen('https://www.facebook.com').read()

print content.decode("GBK");
 
