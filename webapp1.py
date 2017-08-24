#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import cgitb; cgitb.enable()  # for troubleshooting

form = cgi.FieldStorage()
datatype=form.getvalue('datatype')

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
            <li class="active" href='index3.html'><a href='index3.html'>Metadata implementation tool</a></li>
            <li><a href="upload.html">Uploading metadata</a></li>
			<li><a href="excel.html">Excel tools</a></li>
			<li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
    </nav>
	</div>
	<div class="container">
		<div class="page-header">""")
if datatype=="Services":
    print("""
        <h1><center>XML Metadata upload succeeded!</center></h1>
	</div>
	</div>
<form method="post" action="data1.py" enctype="multipart/form-data" >

    <fieldset>
	<p>
	<h2> Give the URL of the services</h2>
	</p>
	<div class="form-group row">
		<label for="url" class="col-xs-2 col-form-label">URL *</label>
		<div class="col-xs-9">
			<input class="form-control" type="text" name="title" required>
		</div>
	</div>
	  <p>
   </div>
  <center><button type="submit" class="btn btn-primary">Submit</button></center>
</p>
</form>
    </fieldset>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>""")
    
else:
    print("""
        <h1><center>XML Metadata upload succeeded !</center></h1>
	</div>
	</div>
    <h2><center>Uploading data</center></h2>
<form method="post" action="data.py" enctype="multipart/form-data" >

    <fieldset>
	<p>
	<h2> Uploading Data</h2>
	</p>
   	<div class="row">
<label class="custom-file col-xs-3">Uploading data</label>
  <input type="file" id="file" name="path" class="custom-file-input" required>
  <span class="custom-file-control col-xs-3"></span>
  <center><button type="submit" value="upload" class="btn btn-primary">Upload</button></center>
</div>

</form>
    </fieldset>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>""")
