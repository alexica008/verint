#!/usr/bin/python3

import requests

page1 = requests.get('http://10.0.0.11')
page2 = requests.get('http://10.0.0.11')
print (page1.text)
print ('############################')
print (page2.text)

if (("httpd_1" in page1.text and "httpd_2" in page2.text) or 
   ("httpd_1" in page2.text and "httpd_2" in page1.text)):
  print ("rr")
else:
  print ("fail")
