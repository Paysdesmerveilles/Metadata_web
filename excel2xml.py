#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Thu Nov 24 11:39:51 2016

@author: Alice FREMAND
"""
import cgi, cgitb
import os
import shutil
from collections import defaultdict
from datetime import datetime
import xlrd
import csv
import B2d_XML2_excel

##############################################################
########## GET THE CSV FILE FROM THE HTML FORM  ##############
#############################################################
#
form = cgi.FieldStorage()
fileitem = form['path']

# Test if the file was uploaded
if fileitem.filename:
# strip leading path from file name to avoid
# directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('File/tmp/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
else:
    message = 'No file was uploaded'
#print("""
#   <p>%s</p>
#""" % (message,))

filePath = 'File/tmp/'+fn
mypath = 'File/tmp/XML'
if not os.path.isdir(mypath):
    os.makedirs(mypath)


##############################################################
############# STUDY OF THE CSV FILE  #######################
#############################################################

#Opening the csv file
data = defaultdict(list)
with open(filePath, errors = 'ignore') as f:
    metadata_file = csv.DictReader(f, delimiter=';')#io.BytesIO(filePath),'r')
    for row in metadata_file:
        for (x, v) in row.items():
           data[x].append(v)
            
##############################################################
############# Definition of variables  #######################
#############################################################

for i in range(0, len(data['ID_title'])):
    if isinstance(data['format1'][i], str):
        data['format1'][i] = data['format1'][i].split('- ')
    if isinstance(data['subject_study'][i], str):
        data['subject_study'][i] = data['subject_study'][i].split('- ')
    if isinstance(data['project_phase'][i], str):
        data['project_phase'][i] = data['project_phase'][i].split('- ')
    if isinstance(data['location'][i], str):
        data['location'][i] = data['location'][i].split('- ')
        data['location'][i].append('Upper Rhine Graben')
        data['location'][i].append('Alsace')
        data['location'][i].append('France')
    else:
        data['location'][i] = [str(data['location'][i])]
    if isinstance(data['variables'][i], str):
        data['variables'][i] = data['variables'][i].split('- ')

################################################################
############ TRANSFORMING THE LINES INTO XML METADATA ##########
###############################################################
for i in range(0, len(data['ID_title'])):
    B2d_XML2_excel.xml(data, i)
shutil.make_archive('File/tmp/XML', 'zip', 'File/tmp/XML')
shutil.rmtree('File/tmp/XML')

##############################################################
####################### HTML  ###############################
#############################################################
print("Content-type: text/html")
print("""
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Metadata implementation</title>
		<link href="css/bootstrap-combined.min.css" rel="stylesheet">
		<link rel="stylesheet" type="text/css" media="screen"
		 href="css/bootstrap-datetimepicker.min.css">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript"
		 src="js/jquery.min.js">
		</script> 
		<script type="text/javascript"
		 src="js/bootstrap.min.js">
		</script>
		<script type="text/javascript"
		 src="js/bootstrap-datetimepicker.min.js">
		</script>	
  </head>

  <body>

	<div class="container">
    <nav class="navbar navbar-default navbar-fixed-top">
	<div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
			<span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="welcome.html">Centre de Donn&eacutees de G&eacuteothermie Profonde</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li href='index3.html'><a href='index3.html'>Metadata implementation tool</a></li>
            <li><a href="upload.html">Uploading metadata</a></li>
			<li class="active" ><a href="excel.html">Excel tools</a></li>
			<li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


        <h1><center>The XML files have been created</center></h1>
    <form method="post" action="webapp1.py">
    <fieldset>
	<p>
	<h2> Zip file containing the created XML metadata </h2>
	</p>
 <h3>Click on the image logo to download the zip file:</h3>
 <a href="File/tmp/XML.zip" download="XML.zip"><center>
  <img src="File/zip.png" width="104" height="142"/></center>
</a>
<p><b>Note:</b> The download attribute is not supported in Edge version 12, IE, Safari or Opera version 12 (and earlier).</p>


</form>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>

""")
f.close()

