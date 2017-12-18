#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:07:41 2017

@author: alice
"""
import cgi, cgitb
import os
import shutil
from pprint import pprint
cgitb.enable()
##############################################################
##################### HTML NAV ############################
#############################################################
nav="""
    <html lang="en">
     <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
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
                <li class="active" href='index3.py'><a href="index3.py">Metadata implementation tool</a></li>
    			<li  ><a href="upload.html">Uploading metadata</a></li>
    			<li  href='excel.html'><a href="excel.html">Excel tools</a></li>
    			<li ><a href="about.html">About</a></li>
                <li><a href="contact.html">Contact</a></li>
              </ul>
            </div>
          </div>
        </nav>"""
end= """        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    
      </body>
    </html>
    
    """        
##############################################################
##################### PROCESSING############################
#############################################################
form = cgi.FieldStorage()
if 'filetoimport' not in form:
    print('Content-Type: text/html; charset=UTF-8')
    print(nav)
    print("""
<h1>ERROR: The file has not been uploaded</h1>
<html>
<head>
  <input type="button" class="btn btn-primary" value="Go back!" onclick="history.back()">
  </input>
</head>
<body>""")
    print(end)
else:
    ID_title = form.getvalue('ID_title')
    filefield = form['filetoimport']
    if not isinstance(filefield, list):
        filefield = [filefield]
    
    mypath = 'File/Data/%s' %ID_title
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    # Test if the file was uploaded
    for fileitem in filefield:
        if fileitem.filename:
        # strip leading path from file name to avoid
        # directory traversal attacks
            fn = os.path.basename(fileitem.filename)
            filePath = mypath + '/' + fn
            open(filePath, 'wb').write(fileitem.file.read())
            message = 'The file "' + fn + '" was uploaded successfully'
        else:
            message = 'No file was uploaded'
    
    shutil.copyfile('File/XML_temp.xml', 'File/Data/%s/XML_temp.xml' %ID_title)
    shutil.make_archive(mypath, 'zip', mypath)
    shutil.rmtree(mypath)
    
    print("Content-type: text/html; charset=utf-8\n")
    print(nav)
    print("""
            <h1><center>The data and metadata have been successfully uploaded</center></h1>
        <fieldset>
    	<p>
    	<h2> Zip file containing the data and XML metadata that have been uploaded on the server</h2>
    	</p>
     <h3>Click on the image logo to download the zip file:</h3>
     <a href="%s.zip" download="%s.zip"><center>""" %(mypath, mypath))
    print("""
      <img src="File/zip.png" width="104" height="142"/></center>
    </a>
    <p><b>Note:</b> The download attribute is not supported in Edge version 12, IE, Safari or Opera version 12 (and earlier).</p>
    </form>    
    """)
    print(end)
