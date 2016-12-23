# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:29:52 2016

@author: Standard
"""
# Import modules for CGI handling
import cgi
import cgitb
import B2d_XML2

cgitb.enable()

class IdentityData:
    """Class that define data by:
        - its title
        -its abstract
        -its data type"""

    def __init__(self, title, abstract, data_type):
        "Building the class"""
        self.title = title
        self.abstract = abstract
        self.data_type = data_type

class LocationData:
    """ Class that gives location information:
    -geographic coordinate system
    -North, SOuth, East, West
    -Depth"""

    def __init__(self, geosys, north, south, east, west, depth1, depth2):
        self.geosys = geosys
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.depth1 = depth1
        self.depth2 = depth2

class TimeData:
    """Class that gives information about time:
        -creation date of data
        -start time, end time of experiment"""
    def __init__(self, T1, T2, Creation_date):
        self.T1 = T1
        self.T2 = T2
        self.Creation_date = Creation_date

class KeywordData:
    """Class that gives information about keywords:
        - subject of study
        - project phase
        - location
        -variable"""
    def __init__(self, subject_study, project_phase, location, variables):
        self.subject_study = subject_study
        self.project_phase = project_phase
        self.location = location
        self.variables = variables

class QualityData:
    """class that gives information about quality of data:
        -format1
        - quality
        - process
        - use_lim
        - access
        - citation"""
    def __init__(self, format1, quality, process, use_lim, access, citation):
        self.format1 = format1
        self.quality = quality
        self.process = process
        self.use_lim = use_lim
        self.access = access
        self.citation = citation

class PersonneData:
    """"Clas that gives information about :
        - the distributor
        - the owner
        - the resource contact of the data """

    def __init__(self, resource_contact, owner1, owner2, distributor):
        self.resource_contact = resource_contact
        self.owner1 = owner1
        self.owner2 = owner2
        self.distributor = distributor

##############################################################
########## GET THE VALUE FROM THE HTML FORM  ################
#############################################################

form = cgi.FieldStorage()

DataID = IdentityData(form.getvalue("title"), form.getvalue("abstract"), form.getvalue("datatype"))

radiogeo = form.getvalue("radiogeo")


if radiogeo == 'point':
    longitude = form.getvalue("longitude")
    latitude = form.getvalue("latitude")
    North = longitude
    South = longitude
    East = latitude
    West = latitude
elif radiogeo == 'box':
    North = form.getvalue("north")
    South = form.getvalue("south")
    East = form.getvalue("east")
    West = form.getvalue("west")

Depth1 = form.getvalue("depth1")
Depth2 = form.getvalue("depth2")
DataLoc = LocationData(form.getvalue("geosys"), North, South, East, West, Depth1, Depth2)

radiotime = form.getvalue("radiotime")

if radiotime == 'extent':
    startdate = form.getvalue("startdate")
    starttime = form.getvalue("starttime")
    t1 = startdate + 'T' + starttime
    enddate = form.getvalue("enddate")
    endtime = form.getvalue("endtime")
    t2 = enddate + 'T' + endtime
    t3 = 1
elif radiotime == 'date':
    date = form.getvalue("date")
    time = form.getvalue("time")
    t1 = date + 'T' + time
    t2 = ''
    t3 = 0

creadate = form.getvalue("creadate")
creatime = form.getvalue("creatime")
creation_date = creadate+'T'+creatime

DataTime = TimeData(t1, t2, creation_date)

Subject_study = form.getvalue("subject")
Project_phase = form.getvalue("project")
Location = form.getvalue("location")
Variables = form.getvalue("variables")
Format1 = form.getvalue("format")
Quality = form.getvalue("quality")
Process = form.getvalue("process")
Resource_contact = form.getvalue("resource")
Owner1 = form.getvalue("owner")
Distributor = form.getvalue("distributor")
Use_lim = form.getvalue("use")
Access = form.getvalue("access")
Citation = form.getvalue("citation")
Owner2 = form.getvalue("owner")

if isinstance(Format1, str):
    temp = []
    temp.append(Format1)
    Format1 = [Format1]
if isinstance(Subject_study, str):
    temp = []
    temp.append(Subject_study)
    Subject_study = [Subject_study]
if isinstance(Project_phase, str):
    temp = []
    temp.append(Project_phase)
    Project_phase = [Project_phase]
if isinstance(Location, str):
    temp = []
    temp.append(Location)
    Location = [Location]
if isinstance(Variables, str):
    temp = []
    temp.append(Variables)
    Variables = [Variables]

DataTime = TimeData(t1, t2, creation_date)
DataKeyword = KeywordData(Subject_study, Project_phase, Location, Variables)
DataQuality = QualityData(Format1, Quality, Process, Use_lim, Access, Citation)
DataPersonne = PersonneData(Resource_contact, Owner1, Owner2, Distributor)

##############################################################
########## TRANSFORM VALUE INTO XML METADATA  ################
#############################################################

#B2d_XML2.xml(title, abstract, data_type, North, East, South,
#             West, Depth1, Depth2, T1, T2, Creation_date, subject_Study,
#             project_Phase, location, variables, format1, quality, process,
#             use_lim, access, citation, resource_contact, owner1, owner1,
#             distributor)

B2d_XML2.xml(DataID, DataLoc, DataTime, DataKeyword, DataQuality, DataPersonne)

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
            <li class="active" href='index.py'><a href='index.py'>Metadata implementation tool</a></li>
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
print('<h4><b>Title </b>: %s </h4>'%DataID.title)
print('<h4><b>Abstract </b>: %s </h4>' %DataID.abstract)
print('<h4><b>Data Type </b>: %s </h4>' %DataID.data_type)
print('</fieldset><fieldset>')
print('<h4><b>Geographic coordinate system</b>: %s </h4>' %DataLoc.geosys)
print('<div class="row">')
#print('<h4 class="col-xs-5"><b>Longitude </b>: %s </h4>' %longitude)
#print('<h4 class="col-xs-5"><b>Latitude </b>: %s </h4>' %latitude)
print('</div>')
print('<div class="row">')
print('<h4 class="col-xs-5"><b>North </b>: %s </h4>' %DataLoc.north)
print('<h4 class="col-xs-5"><b>South </b>: %s </h4>' %DataLoc.south)
print('</div>')
print('<div class="row">')
print('<h4 class="col-xs-5"><b>East </b>: %s </h4>' %DataLoc.east)
print('<h4 class="col-xs-5"><b>West </b>: %s </h4>' %DataLoc.west)
print('</div>')
print('<div class="row">')
print('<h4 class="col-xs-5"><b>Depth1 </b>: %s </h4>' %DataLoc.depth1)
print('<h4 class="col-xs-5"><b>Depth2 </b>: %s </h4>' %DataLoc.depth2)
print('</div>')
print('</fieldset><fieldset>')
if radiotime == 'extent':
    print('<h4 ><b>Start date </b>: %s </h4>' %DataTime.T1)
    print('<h4 ><b>End date </b>: %s </h4>' %DataTime.T2)
elif radiotime == 'date':
    print('<h4 ><b>Date </b>: %s </h4>' %DataTime.T1)
print('<h4><b>Creation date </b>: %s </h4>' %DataTime.Creation_date)
print('</fieldset><fieldset>')
print('<h4><b>Formats </b>: %s </h4>' %DataQuality.format1)
print('<h4><b>Subject of study </b>: %s </h4>' %DataKeyword.subject_study)
print('<h4><b>Project phase </b>: %s </h4>' %DataKeyword.project_phase)
print('<h4><b>Location </b>: %s </h4>' %DataKeyword.location)
print('<h4><b>Variables </b>: %s </h4>' %DataKeyword.variables)
print('</fieldset><fieldset>')
print('<h4><b>Quality </b>: %s </h4>' %DataQuality.quality)
print('<h4><b>Process step</b>: %s </h4>' %DataQuality.process)
print('<h4><b>Resource contact</b>: %s </h4>' %DataPersonne.resource_contact)
print('</fieldset><fieldset>')
print('<h4><b>Owner of the data</b>: %s </h4>' %DataPersonne.owner1)
print('<h4><b>Distributor</b>: %s </h4>' %DataPersonne.distributor)
print('<h4><b>Use limitation</b>: %s </h4>' %DataQuality.use_lim)
print('<h4><b>Access </b>: %s </h4>' %DataQuality.access)
print('<h4><b>Citation </b>: %s </h4>' %DataQuality.citation)
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

