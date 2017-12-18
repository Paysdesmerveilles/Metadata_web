#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import B2d_XML2


##############################################################
########## GET THE VALUE FROM THE HTML FORM  ################
#############################################################

form = cgi.FieldStorage()
data = {a:form.getvalue(a) for a in form.keys()}

##############################################################
########## TRANSFORM VALUE INTO XML METADATA  ################
#############################################################

B2d_XML2.xml(data)

##############################################################
################ DISPLAY RESULTS  ##########################
#############################################################
print("Content-type: text/html")
print("""
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
            <li class="active" href='index3.py'><a href='index3.py'>Metadata implementation tool</a></li>
            <li><a href="upload.html">Uploading metadata</a></li>
			<li><a href="excel.html">Excel tools</a></li>
			<li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
    </nav>


        <h1><center>Succeed!! Please find your created metadata below </center></h1>""")
print('<form method="post" action="webapp1.py?datatype=%s">'  % data['datatype'])
print("""   
        <fieldset>
""")
print('<h4><b>Title </b>: %s </h4>'%data['title'].encode('ascii', 'xmlcharrefreplace'))
print('<h4><b>Short Title </b><input type="text" name="ID_title" value="%s" readonly></h4>'%data['ID_title'])
print("""
    </fieldset>
    <fieldset>
	<p>
	<h2> XML</h2>
	</p>
 <h3>Click on the image logo to download the XML:</h3>""")
print(' <a href="File/XML_temp.xml" download="%s.xml"><center>' % data['ID_title'].encode('ascii', 'xmlcharrefreplace'))
print("""<img src="File/XML.jpg" width="104"/></center>
</a>
<p><b>Note:</b> The download attribute is not supported in Edge version 12, IE, Safari or Opera version 12 (and earlier).</p>
</fieldset>""")

print("""<fieldset>
<center><button class="btn btn-primary">Validate</button></center>
</p>
</fieldset>
</form>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>""")
