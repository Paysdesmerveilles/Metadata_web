#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import B2d_XML2
from datetime import datetime

class IdentityData:
    """Class that define data by:
        - its title
        -its abstract
        -its data type"""

    def __init__(self, title, ID_title, abstract, data_type):
        "Building the class"""
        self.title = title
        self.ID_title = ID_title
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
DataID = IdentityData(form.getvalue("title").encode('utf-8'), form.getvalue("ID_title"), form.getvalue("abstract").encode('utf-8'), form.getvalue("datatype"))

radiogeo = form.getvalue("radiogeo")

if radiogeo == 'point':
    longitude = form.getvalue("longitude")
    latitude = form.getvalue("latitude")
    North = longitude
    South = longitude
    East = latitude
    West = latitude
else:
    North = form.getvalue("north")
    South = form.getvalue("south")
    East = form.getvalue("east")
    West = form.getvalue("west")
Depth1 = form.getvalue("depth1")
Depth2 = form.getvalue("depth2")
if isinstance(Depth1, str):
    DataLoc = LocationData(form.getvalue("geosys"), North, South, East, West, Depth1, Depth2)
else:
    DataLoc = LocationData(form.getvalue("geosys"), North, South, East, West, 'no_deep', Depth2)
radiotime = form.getvalue("radiotime")

if radiotime == 'extent':
    startdate = form.getvalue("startdate")
    starttime = form.getvalue("starttime")
    t1 = startdate + 'T' + starttime
    enddate = form.getvalue("enddate")
    endtime = form.getvalue("endtime")
    t2 = enddate + 'T' + endtime
    t3 = 1
else:
    date = form.getvalue("date")
    time = form.getvalue("time")
    t1 = str(date) + 'T' + str(time)
    t2 = ''
    t3 = 0

#creadate = form.getvalue("creadate")
#creatime = form.getvalue("creatime")
creadate = datetime.now().strftime('%Y-%m-%d')
creatime = datetime.now().strftime('%H:%M:%S')
creation_date = str(creadate)+'T'+str(creatime)

DataTime = TimeData(t1, t2, creation_date)

Subject_study = form.getvalue("subject")
Project_phase = form.getvalue("project")
Location = form.getvalue("location")
Variables = form.getvalue("variables")
Format1 = form.getvalue("format")
Quality = form.getvalue("quality")
if isinstance(Quality, str):
    Quality = Quality.encode('utf-8')
Process = form.getvalue("process")
if isinstance(Process, str):
    Process = Process.encode('utf-8')
Resource_contact = form.getvalue("resource")
Owner1 = form.getvalue("owner")
Distributor = form.getvalue("distributor")
Use_lim = form.getvalue("use")
if isinstance(Use_lim, str):
    Use_lim = Use_lim.encode('utf-8')
Access = form.getvalue("access")
Citation = form.getvalue("citation")
if isinstance(Citation, str):
    Citation = Citation.encode('utf-8')
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

B2d_XML2.xml(DataID, DataLoc, DataTime, DataKeyword, DataQuality, DataPersonne)

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
            <li class="active" href='index3.html'><a href='index3.html'>Metadata implementation tool</a></li>
            <li><a href="upload.html">Uploading metadata</a></li>
			<li><a href="excel.html">Excel tools</a></li>
			<li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
    </nav>


        <h1><center>Succeed!! Here are the value you entered </center></h1>
        <h2><center> Please check the value. XML available below</center></h2>""")

print("""   
        <fieldset>
""")
print('<h4><b>Title </b>: %s </h4>'%DataID.title)
print('<h4><b>Short Title </b>: %s </h4>'%DataID.ID_title)
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
#print('<h4><b>Location </b>: %s </h4>' %DataKeyword.location)
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
#print('<h4><b>Radiobutton</b>: %s </h4>' %radiotime)
print("""
    </fieldset>
    <fieldset>
	<p>
	<h2> XML</h2>
	</p>
 <h3>Click on the image logo to download the XML:</h3>""")
print(' <a href="File/XML_temp.xml" download="%s.xml"><center>' % DataID.ID_title)
print("""<img src="File/XML.jpg" width="104"/></center>
</a>
<p><b>Note:</b> The download attribute is not supported in Edge version 12, IE, Safari or Opera version 12 (and earlier).</p>
</fieldset>""")
print('<form method="post" action="webapp1.py?datatype=%s">'  % DataID.data_type)
print("""<fieldset>
<center><button class="btn btn-primary">Validate</button></center>
</p>
</fieldset>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>""")
#</form>
