# -*- coding: utf-8 -*-

# Import modules for CGI handling
import cgi
import B2d_XML2

##############################################################
########## GET THE VALUE FROM THE HTML FORM  ################
#############################################################
form = cgi.FieldStorage()

title = form.getvalue("title")
abstract = form.getvalue("abstract")
data_type = form.getvalue("datatype")
geosys = form.getvalue("geosys")
longitude = form.getvalue("longitude")
latitude = form.getvalue("latitude")
North = form.getvalue("north")
South = form.getvalue("south")
East = form.getvalue("east")
West = form.getvalue("west")
Depth1 = form.getvalue("depth1")
Depth2 = form.getvalue("depth2")
radiotime = form.getvalue("radiotime")
if radiotime == 'extent':
    startdate = form.getvalue("startdate")
    starttime = form.getvalue("starttime")
    T1 = startdate + 'T' + starttime
    enddate = form.getvalue("enddate")
    endtime = form.getvalue("endtime")
    T2 = enddate + 'T' + endtime
    T3 = 1
elif radiotime == 'date':
    date = form.getvalue("date")
    time = form.getvalue("time")
    T1 = date + 'T' + time
    T2 = ''
    T3 = 0
creadate = form.getvalue("creadate")
creatime = form.getvalue("creatime")
Creation_date = creadate+'T'+creatime
format1 = form.getvalue("format")
subject_Study = form.getvalue("subject")
project_Phase = form.getvalue("project")
location = form.getvalue("location")
variables = form.getvalue("variables")
quality = form.getvalue("quality")
process = form.getvalue("process")
resource_contact = form.getvalue("resource")
owner1 = form.getvalue("owner")
distributor = form.getvalue("distributor")
use_lim = form.getvalue("use")
access = form.getvalue("access")
citation = form.getvalue("citation")
radiotime = form.getvalue("radiotime")



if isinstance(format1, str):
    temp = []
    temp.append(format1)
    format1 = [format1]
if isinstance(subject_Study, str):
    temp = []
    temp.append(subject_Study)
    subject_Study = [subject_Study]
if isinstance(project_Phase,str):
    temp = []
    temp.append(project_Phase)
    project_Phase = [project_Phase]
if isinstance(location, str):
    temp = []
    temp.append(location)
    location = [location]
if isinstance(variables, str):
    temp = []
    temp.append(variables)
    variables = [variables]

##############################################################
########## TRANSFORM VALUE INTO XML METADATA  ################
#############################################################

B2d_XML2.xml(title, abstract, data_type, North, East, South,
             West, Depth1, Depth2, T1, T2, Creation_date, subject_Study,
             project_Phase, location, variables, format1, quality, process,
             use_lim, access, citation, resource_contact, owner1, owner1,
             distributor)

##############################################################
################ DISPLAY RESULTS  ##########################
#############################################################
print("""
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Metadata implementation</title>

		<link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css" rel="stylesheet">
		<link rel="stylesheet" type="text/css" media="screen"
		 href="http://tarruda.github.com/bootstrap-datetimepicker/assets/css/bootstrap-datetimepicker.min.css">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript"
		 src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js">
		</script> 
		<script type="text/javascript"
		 src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/js/bootstrap.min.js">
		</script>
		<script type="text/javascript"
		 src="http://tarruda.github.com/bootstrap-datetimepicker/assets/js/bootstrap-datetimepicker.min.js">
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
          <a class="navbar-brand" href="welcome.py">Centre de Donn&eacutees de G&eacuteothermie Profonde</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active" href='index.py'><a href="#">Metadata implementation tool</a></li>
            <li><a href="upload.py">Uploading metadata</a></li>
			<li><a href="excel.py">Excel tools</a></li>
			<li><a href="about.py">About</a></li>
            <li><a href="contact.py">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


        <h1><center>Succeed!! Here are the value you entered !</center></h1>
        <h2><center> Please check the value and validate to create your xml file</center></h2>
        <fieldset>
""")
print('<h4><b>Title </b>: %s </h4>'%title)
print('<h4><b>Abstract </b>: %s </h4>' %abstract)
print('<h4><b>Data Type </b>: %s </h4>' %data_type)
print('</fieldset><fieldset>')
print('<h4><b>Geographic coordinate system</b>: %s </h4>' %geosys)
print('<div class="row">')
print('<h4 class="col-xs-5"><b>Longitude </b>: %s </h4>' %longitude)
print('<h4 class="col-xs-5"><b>Latitude </b>: %s </h4>' %latitude)
print('</div>')
print('<div class="row">')
print('<h4 class="col-xs-5"><b>North </b>: %s </h4>' %North)
print('<h4 class="col-xs-5"><b>South </b>: %s </h4>' %South)
print('</div>')
print('<div class="row">')
print('<h4 class="col-xs-5"><b>East </b>: %s </h4>' %East)
print('<h4 class="col-xs-5"><b>West </b>: %s </h4>' %West)
print('</div>')
print('<div class="row">')
print('<h4 class="col-xs-5"><b>Depth1 </b>: %s </h4>' %Depth1)
print('<h4 class="col-xs-5"><b>Depth2 </b>: %s </h4>' %Depth2)
print('</div>')
print('</fieldset><fieldset>')
if radiotime == 'extent':
    print('<h4 ><b>Start date </b>: %s </h4>' %T1)
    print('<h4 ><b>End date </b>: %s </h4>' %T2)
elif radiotime == 'date':
    print('<h4 ><b>Date </b>: %s </h4>' %T1)
print('<h4><b>Creation date </b>: %s </h4>' %Creation_date)
print('</fieldset><fieldset>')
print('<h4><b>Formats </b>: %s </h4>' %format1)
print('<h4><b>Subject of study </b>: %s </h4>' %subject_Study)
print('<h4><b>Project phase </b>: %s </h4>' %project_Phase)
print('<h4><b>Location </b>: %s </h4>' %location)
print('<h4><b>Variables </b>: %s </h4>' %variables)
print('</fieldset><fieldset>')
print('<h4><b>Quality </b>: %s </h4>' %quality)
print('<h4><b>Process step</b>: %s </h4>' %process)
print('<h4><b>Resource contact</b>: %s </h4>' %resource_contact)
print('</fieldset><fieldset>')
print('<h4><b>Owner of the data</b>: %s </h4>' %owner1)
print('<h4><b>Distributor</b>: %s </h4>' %distributor)
print('<h4><b>Use limitation</b>: %s </h4>' %use_lim)
print('<h4><b>Access </b>: %s </h4>' %access)
print('<h4><b>Citation </b>: %s </h4>' %citation)
print('<h4><b>Radiobutton</b>: %s </h4>' %radiotime)
print("""
    </fieldset>
    <form method="post" action="webapp1.py">
    <fieldset>
	<p>
	<h2> XML</h2>
	</p>
 <h3>Click on the image logo to download the XML:</h3>
 <a href="File/XML_test.xml" download="XML"><center>
  <img src="File/XML.jpg" width="104" height="142"/></center>
</a>
<p><b>Note:</b> The download attribute is not supported in Edge version 12, IE, Safari or Opera version 12 (and earlier).</p>

</fieldset>
    <fieldset>
	<p>
	<h2> Uploading data and Validation</h2>
	</p>
   	<div class="row">
<label class="custom-file col-xs-3">Uploading data</label>
  <input type="file" id="file" class="custom-file-input">
  <span class="custom-file-control col-xs-3"></span>
  <center><button type="submit" class="btn btn-primary">Validate</button></center>
</div>

</form>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>

""")

