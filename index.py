# -*- coding: utf-8 -*-

# Import modules for CGI handling 
import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

html = open('index3.html', 'r')
print(html.read())
  
title=form.getvalue("title")