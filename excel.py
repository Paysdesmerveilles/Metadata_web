# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:02:35 2016

@author: Standard
"""

import cgi 
html = open('excel.html', 'r')
print("Content-type: text/html; charset=utf-8\n")
print(html.read())