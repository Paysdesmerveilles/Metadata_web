# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:29:52 2016

@author: Standard
"""

import cgi 
html = open('upload.html', 'r')
print("Content-type: text/html; charset=utf-8")
print(html.read())

