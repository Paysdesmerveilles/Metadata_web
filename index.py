# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:29:52 2016

@author: Standard
"""
# Import modules for CGI handling
print("Content-type: text/html; charset=utf-8\n")
HTML = open('index3.html', 'r')
print(HTML.read())

