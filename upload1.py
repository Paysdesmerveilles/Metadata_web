# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:29:52 2016

@author: Standard
"""
import cgi, cgitb
import XML_B2d2
cgitb.enable()

##############################################################
########## GET THE XML FILE FROM THE HTML FORM  ##############
#############################################################
form = cgi.FieldStorage()
filePath=form["path"].value

##############################################################
######### RUN THE PROGRAM THAT READ XML METADATA ############
#############################################################
  
title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1, T2, T3, t1,h1,t2,h2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor=XML_B2d2.xml2B2d(filePath)
print("Content-type: text/html; charset=utf-8\n")
#print('%s est le chemin du fichier' %filePath)
#Les contrôles

##############################################################
########## DISPLAY THE METADATA INTO THE FORM  ##############
#############################################################

html1="""
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
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
	<div class="container">
		<div class="page-header">
        <h1><center>Metadata implementation</center></h1>
	</div>
	</div>
<form method="post" action="webapp.py">
<fieldset>
<p><h2> Resource identification </h2></p>
<p>
<div class="form-group row">
<label for="title" class="col-xs-2 col-form-label">Title</label>"""

print(html1)
print('<div class="col-xs-9"><input class="form-control" type="text" name="title" value="%s" required>' %title)			
html2="""</div>
	</div>
	</p>
	<p>
	<div class="form-group row">
		<label for="abstract" class="col-xs-2 col-form-label">Abstract</label>
		<div class="col-xs-9">"""
print(html2)
print('<textarea class="form-control" name="abstract" rows="3" required>%s</textarea>' %abstract )

print("""</div>
	</div>
	</p>
	<p>
	<div class="form-group row">
		<label for="datatype" class="col-xs-2 col-form-label">Data Type</label>
		<div class="col-xs-9">
		<select class="form-control" name="datatype">""")
  
dataType_list=['Dataset', 'Series', 'Services']
for i in range(0, len(dataType_list)):
    if data_type==dataType_list[i]:
        dataType_list[i]=0
    if dataType_list[i]!=0:
        print('<option >%s</option>' %dataType_list[i])
print('<option selected="selected">%s</option>' %data_type)

print("""		</select>
		</div>
	</div>
	</p>
</fieldset>
<fieldset>
	<h2> Spatial and temporal extent</h2>

 <p>
	<legend> Geographic extent </legend>
 </p>
	<p>
	<div class="form-group row">
		<label for="geosys" class="col-xs-2 col-form-label">Geographic coordinate system</label>
		<div class="col-xs-9">
		<select class="form-control" name="geosys">
		  <option>WGS84</option>
		  <option>Lambert III</option>
		</select>
		</div>
	</div>
	</p>
	<div class="form-check">
		<div class="row">""")

#Spatial extent
if North==South and East==West:
    print("""	<input type="radio" class="col-xs-1" name="radiogeo" value="point" required checked>
    <label class="col-xs-3 col-form-label">Point **: Longitude (&degN)</label>""")
    print('<input type="number"  min="-90" max="90" value="%f" step="0.000001" class="col-xs-2 col-form-label" name="longitude" required>' % North)
    print('<label for="lat1" class="col-xs-2 col-form-label">Latitude (&degE)</label>')
    print('<input type="number" min="-180" max="180" value="%f" step="0.000001" class="col-xs-2 col-form-label" name="latitude"required>' % East)
    print("""    
          </div>
		<div class="row">
		<input type="radio" class="col-xs-1" name="radiogeo" value="box" required>
		<label class="col-xs-3 col-form-label">Bounding box **:</label>
		</div>
		<div class="row">  
		<label for="space" class="col-xs-1 col-form-label"></label>
		  <label class="col-xs-2 col-form-label">North (&degN)</label>
		  <input type="number" min="document.getElementById('south').value" max="90" value="48.94"step="0.01" class="col-xs-2 col-form-label" name="north"required>
		  <label for="south" class="col-xs-2 col-form-label">South (&degN)</label>
		  <input type="number" min="-90" max="90" value="48.93"step="0.01" class="col-xs-2 col-form-label" name="south"required>
		</div>
		<div class="row">
			<label for="space" class="col-xs-1 col-form-label"></label>
		  <label for="east"class="col-xs-2 col-form-label">East(&degE)</label>
		  <input type="number" min="-180" max="180" value="7.86" step="0.000001" class="col-xs-2 col-form-label" name="east" required>
		  <label for="west" class="col-xs-2 col-form-label">West (&degE)</label>
		  <span id="container">
		  <input type="number" min="-180" max="180" value="7.87"step="0.000001" class="col-xs-2 col-form-label" name="west" required>
		</span>
	</div>
	</div>
	</p>
	<P>""")
else:
    print("""
    		<input type="radio" class="col-xs-1" name="radiogeo" value="point" required >
		 <label class="col-xs-3 col-form-label">Point **: Longitude (&degN)</label>
		  <input type="number"  min="-90" max="90" value="48.94" step="0.000001" class="col-xs-2 col-form-label" name="longitude" required>
		  <label for="lat1" class="col-xs-2 col-form-label">Latitude (&degE)</label>
		  <input type="number" min="-180" max="180" value="7.86" step="0.000001" class="col-xs-2 col-form-label" name="latitude"required>
		</div>
		<div class="row">
		<input type="radio" class="col-xs-1" name="radiogeo" value="box" required checked>
		<label class="col-xs-3 col-form-label">Bounding box **:</label>
		</div>
		<div class="row">  
		<label for="space" class="col-xs-1 col-form-label"></label>
		  <label class="col-xs-2 col-form-label">North (&degN)</label>""")
    print('<input type="number" min="document.getElementById("south").value" max="90" value="%f" step="0.000001" class="col-xs-2 col-form-label" name="north"required>' %North)
    print('<label for="south" class="col-xs-2 col-form-label">South (&degN)</label>')
    print('<input type="number" min="-90" max="90" value="%f" step="0.000001" class="col-xs-2 col-form-label" name="south"required>' %South)
    print("""</div>
		<div class="row">
			<label for="space" class="col-xs-1 col-form-label"></label>
		  <label for="east"class="col-xs-2 col-form-label">East(&degE)</label>""")
    print('<input type="number" min="-180" max="180" value="%f" step="0.000001" class="col-xs-2 col-form-label" name="east" required>' %East)
    print('<label for="west" class="col-xs-2 col-form-label">West (&degE)</label>')
    print('<span id="container"><input type="number" min="-180" max="180" value="%f" step="0.000001" class="col-xs-2 col-form-label" name="west" required></span>' %West)
    print("""
	</div>
	</div>
	</p>
	<P>""")
#End spatial extent
#Depth
if type(Depth1)==float and type(Depth2)==float:
    print("""<div class="row">
    	  <label for="depth" class="col-xs-2 col-form-label">Depth : From (m)</label>""")
    print('<input type="number" class="col-xs-2 col-form-label" name="depth1" value="%f">' %Depth1)
    print('<label for="depth2" class="col-xs-2 col-form-label">to (m)</label>')
    print('<input type="number"  min="-7000" max="0" class="col-xs-2 col-form-label" name="depth2" value="%f">' %Depth2)
else:
    print("""<div class="row">
    	  <label for="depth" class="col-xs-2 col-form-label">Depth : From (m)</label>
    <input type="number" class="col-xs-2 col-form-label" name="depth1">
    <label for="depth2" class="col-xs-2 col-form-label">to (m)</label>
    <input type="number"  min="-7000" max="0" class="col-xs-2 col-form-label" name="depth2" >""")
    

#Temporal extent
print(""" </div>
	  </p>
       <p>
	<legend> Temporal extent </legend>
     </p>
	<p>
	<div class="form-check">
		<div class="row">""")
if T3==1:
    print('<input type="radio" class="col-xs-2"  name="radiotime" value="extent" required checked>')
    print("""
		<label class="col-xs-3 col-form-label">Temporal extent** :</label>
		<label class="col-xs-3 col-form-label">Time interval</label>
		</div>
		<div class="row">
		<label class="col-xs-3 col-form-label"></label>
		<label class="col-xs-1 col-form-label"> Start</label>
			<div id="datepicker" class="col-xs-3 input-append date" >""")
    print('<input type="text" name="startdate" value="%s" ></input>'%t1)
    print("""<span class="add-on">
					<i data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker').datetimepicker({
					format: 'yyyy-MM-dd',
					pickTime:false,
				  });
				</script>
			</div>
			<div id="timepicker1" class="col-xs-3 input-append date" >""")
    print('<input type="text" name="starttime" value="%s" ></input>' %h1)
    print("""<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker1').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>
			</div>
		</div>
		<div class="row">
		<label class="col-xs-3 col-form-label"></label>
		<label class="col-xs-1 col-form-label">End</label>
			<div id="datepicker2" class="col-xs-3 input-append date">""")
    print('<input type="text"name="enddate" value="%s" ></input>' %t2)
    print("""	<span class="add-on">
					<i  data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker2').datetimepicker({
					format: 'yyyy-MM-dd',
					pickTime:false
					
				  });
				</script>
			</div>
			<div id="timepicker2" class="col-xs-3 input-append date">""")
    print('<input type="text" name="endtime" value="%s" ></input>' %h2)
    print("""
				<span class="add-on">
					<i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker2').datetimepicker({
					format: 'hh:mm:ss',
					pickDate:false
				  });
				</script>
			</div>
		</div>
		</p>
		<p>
		<div class="row">
			<input type="radio" class="col-xs-2" name="radiotime" value="date" required>
			<label class="col-xs-3 col-form-label">Temporal extent** : Date</label>
			<div id="datepicker3" class="col-xs-3 input-append date">
				<input type="text" name="date" ></input>
				<span class="add-on">
					<i data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker3').datetimepicker({
					format: 'yyy-MM-dd',
					pickTime:false
				  });
				</script>
			</div>
			<div id="timepicker3" class="col-xs-3 input-append date">
				<input type="text" name="time" value="00:00:00" ></input>
				<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker3').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>
			</div>
		</div>
	</div>
	</p>
<p>""")
    
else:
    print("""   
		<input type="radio" class="col-xs-2"  name="radiotime" value="extent" required>
		<label class="col-xs-3 col-form-label">Temporal extent** :</label>
		<label class="col-xs-3 col-form-label">Time interval</label>
		</div>
		<div class="row">
		<label class="col-xs-3 col-form-label"></label>
		<label class="col-xs-1 col-form-label"> Start</label>
			<div id="datepicker" class="col-xs-3 input-append date" >
				<input type="text" name="startdate" ></input>
				<span class="add-on">
					<i data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker').datetimepicker({
					format: 'yyyyy-MM-dd',
					pickTime:false,
				  });
				</script>
			</div>
			<div id="timepicker1" class="col-xs-3 input-append date" >
				<input type="text" name="starttime" value="00:00:00" ></input>
				<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker1').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>
			</div>
		</div>
		<div class="row">
		<label class="col-xs-3 col-form-label"></label>
		<label class="col-xs-1 col-form-label">End</label>
			<div id="datepicker2" class="col-xs-3 input-append date">
				<input type="text"name="enddate" min= ></input>
				<span class="add-on">
					<i  data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker2').datetimepicker({
					format: 'yyyy-MM-dd',
					pickTime:false
					
				  });
				</script>
			</div>
			<div id="timepicker2" class="col-xs-3 input-append date">
				<input type="text" name="endtime" value="00:00:00" ></input>
				<span class="add-on">
					<i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker2').datetimepicker({
					format: 'hh:mm:ss',
					pickDate:false
				  });
				</script>
			</div>
		</div>
		</p>
		<p>
		<div class="row">""")
    print('<input type="radio" class="col-xs-2" name="radiotime" value="date" required checked>')
    print("""<label class="col-xs-3 col-form-label">Temporal extent** : Date</label>
			<div id="datepicker3" class="col-xs-3 input-append date">""")
    print('<input type="text" name="date" value="%s"></input>' %t1)
    print("""
				<span class="add-on">
					<i data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker3').datetimepicker({
					format: 'yyyy-MM-dd',
					pickTime:false
				  });
				</script>
			</div>
			<div id="timepicker3" class="col-xs-3 input-append date">""")
    print('<input type="text" name="time" value="%s" ></input>' %h1)
    print("""
				<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker3').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>
			</div>
		</div>
	</div>
	</p>
<p>""")
# End temporal extent
#Creation date
print("""
	<legend> Creation date </legend>
 </p>
	<p>
	<div class="row">
	<label class="col-xs-3 col-form-label">Creation date</label>
		<div id="datepicker4" class="col-xs-3 input-append date">""")
(t3, h3)=Creation_date.split('T')
print('<input type="text" name="creadate" value="%s" required></input>' %t3)
print("""
				<span class="add-on">
					<i data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#datepicker4').datetimepicker({
					format: 'yyyy-MM-dd',
					pickTime:false
				  });
				</script>
			</div>
			<div id="timepicker4" class="col-xs-3 input-append date">""")
print('<input type="text" name="creatime" value="%s" required></input>)' %h3)
print("""
				<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#timepicker4').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>
			</div>
		</div>
	</p>

</fieldset>
<fieldset>	
	<p><h2>Processing</h2></p>
	<p>
	<div class="row">
		<label class="col-xs-2 col-form-label">Format *</label>
		<select id="listformat1" class="multiselect col-xs-4" multiple="multiple">""")
format1_list=['csv','mSEED','SEG-Y','pdf','jpg', 'excel', 'text']
for i in range(0, len(format1_list)):
    for j in range(0, len(format1)):
        if format1[j]==format1_list[i]:
            format1_list[i]=0
    if format1_list[i]!=0:
        print('<option class="list-group-item">%s</option>' %format1_list[i])
        
print("""	</select>
		<div class="col-xs-1">
			<input id="button1" type="button" value=">>" />
			<br/>
			<input id="button2" type="button" value="<<" />
		</div>
		<select class="multiselect col-xs-4" id="listformat2" multiple="multiple" rows=2 name="format" required> """   )
for j in range(0, len(format1)):
    print('<option class="list-group-item">%s</option>' %format1[j])

print("""
		</select>
    </div>
	<script language="JavaScript">
		$(function(){
			$("#button1").click(function(){
				$("#listformat1 > option:selected").each(function(){
					$(this).remove().appendTo("#listformat2");
				});
			});
		})
		$(function(){
			$("#button2").click(function(){
				$("#listformat2 > option:selected").each(function(){
					$(this).remove().appendTo("#listformat1");
				});
			});
		})
	</script>
	</p>
	<p>
	<div class="form-group row">
		<label for="quality" class="col-xs-2 col-form-label">Quality</label>
		<div class="col-xs-9">""")
print('<input class="form-control" type="text" name="quality" value="%s">' %quality)
print("""
		</div>
	</div>
	</p>
	<p>
	<div class="form-group row">
		<label for="process" class="col-xs-2 col-form-label">Processing text</label>
		<div class="col-xs-9">""")
print('<textarea class="form-control" id="process" rows="3" name="process">%s</textarea>' %process)

#Keywords:
Subject_list=['Hydraulics','Chemistry, Tracer test','Geology, Minerals','Gravimetry, Gravimetric measurements','Logging, Logs, Downhole methods, Drilling','Magnetotellurics, MT','Geodesy, InSAR','Fracture caracterisation, Fracture,Tectonics','Seismics, Seismic reflection, VSP, Vertical Seismic Profile','Modelisation','Seismology, Earthquakes, Seismic sources, Micro-seismicity']
Project_list=['Circulation','Hydraulic Stimulation','Drilling','Exploration','Injection Test','Exploitation','Chemical stimulation','Production Test']
location_list=['GPK1','GPK2','GPK3','GPK4','EPS1','Soultz-sous-Forêts (67250)','Upper Rhine Graben','Alsace','Rittershoffern (67690)','France']
variable_list=['T (Temperature)','P (Pressure)','Q, FLOW (Flow rate)','Density logs (RHOB, DECA, DRHOB, ...)','Imagery logs (ARI, BHTV, FMS, BI FMI, ...)','PHI (Porosity)','Hole caracterisation (Hole azimuth, radius, caliper, inclination, trajectry, deviation, ...)','Magnetic parameters (FNOR, FX, FY, FZ, ...)','V (Volume of water)','Velocities and slowness logs (DTP, DTS, DTST, VP/VS)','GR (Gamma Ray)','Other','Seismology parameters','Resistivity logs (MPHI, IDPH, ILD, ILM, MSFL, LLD, LLS)','Drilling parameters (drilling rate, velocity, WOH, WOB, Rate of penetration, ...)','Chemical content (U, Th, O2, CH4, CO2, H2S, K, ...)','Geological log (Age, Unit, Fracture, Minerals content, Petrographical description ...)','Elastic properties (Young modulus, Poisson ratio, ...)','Ph (pH)']
print("""
		</div>
	</div>
	</p>
</fieldset>
<fieldset>
	<p><h2> Keywords </h2></p>
	<p>
	<h4> Please select at least one keyword by categories </h4>
	</p>
	<div class="row">
		<label class="col-xs-2 col-form-label">Subject study *</label>
		<select id="listsubj1" class="multiselect col-xs-4" multiple="multiple">""")
for i in range(0, len(Subject_list)):
    for j in range(0, len(subject_Study)):
        if subject_Study[j]==Subject_list[i]:
            Subject_list[i]=0
    if Subject_list[i]!=0:
        print('<option class="list-group-item">%s</option>' %Subject_list[i])
print("""
		</select>
		<div class="col-xs-1">
			<input id="button3" type="button" value=">>" />
			<br/>
			<input id="button4" type="button" value="<<" />
		</div>
		<select class="multiselect col-xs-4" id="listsubj2" multiple="multiple" rows=2 name="subject" required> """ )
for j in range(0, len(subject_Study)):
    print('<option class="list-group-item">%s</option>' %subject_Study[j])     
print("""
		</select>
    </div>
	<script language="JavaScript">
		$(function(){
			$("#button3").click(function(){
				$("#listsubj1 > option:selected").each(function(){
					$(this).remove().appendTo("#listsubj2");
				});
			});
		})
		$(function(){
			$("#button4").click(function(){
				$("#listsubj2 > option:selected").each(function(){
					$(this).remove().appendTo("#listsubj1");
				});
			});
		})
	</script>
	</p>
		<div class="row">
		<label class="col-xs-2 col-form-label">Project Phase *</label>
		<select id="listproj1" class="multiselect col-xs-4" multiple="multiple">""")
for i in range(0, len(Project_list)):
    for j in range(0, len(project_Phase)):
        if project_Phase[j]==Project_list[i]:
            Project_list[i]=0
    if Project_list[i]!=0:
        print('<option class="list-group-item">%s</option>' %Project_list[i])
print("""
		</select>
		<div class="col-xs-1">
			<input id="button5" type="button" value=">>" />
			<br/>
			<input id="button6" type="button" value="<<" />
		</div>
		<select class="multiselect col-xs-4" id="listproj2" multiple="multiple" rows=2 name="project" required>""")
for j in range(0, len(project_Phase)):
    print('<option class="list-group-item">%s</option>' %project_Phase[j])     
print("""
		</select>
    </div>
	<script language="JavaScript">
		$(function(){
			$("#button5").click(function(){
				$("#listproj1 > option:selected").each(function(){
					$(this).remove().appendTo("#listproj2");
				});
			});
		})
		$(function(){
			$("#button6").click(function(){
				$("#listproj2 > option:selected").each(function(){
					$(this).remove().appendTo("#listproj1");
				});
			});
		})
	</script>
	</p>
		<div class="row">
		<label class="col-xs-2 col-form-label">Location *</label>
		<select id="listloc1" class="multiselect col-xs-4" multiple="multiple">""")
for i in range(0, len(location_list)):
    for j in range(0, len(location)):
        if location[j]==location_list[i]:
            location_list[i]=0
    if location_list[i]!=0:
        print('<option class="list-group-item">%s</option>' %location_list[i])
print("""
		</select>
		<div class="col-xs-1">
			<input id="button7" type="button" value=">>" />
			<br/>
			<input id="button8" type="button" value="<<" />
		</div>
		<select class="multiselect col-xs-4" id="listloc2" multiple="multiple" rows=2 name="location" required>""")
for j in range(0, len(location)):
    print('<option class="list-group-item">%s</option>' %location[j])     
print("""   
		</select>
    </div>
	<script language="JavaScript">
		$(function(){
			$("#button7").click(function(){
				$("#listloc1 > option:selected").each(function(){
					$(this).remove().appendTo("#listloc2");
				});
			});
		})
		$(function(){
			$("#button8").click(function(){
				$("#listloc2 > option:selected").each(function(){
					$(this).remove().appendTo("#listloc1");
				});
			});
		})
	</script>
	</p>
		<div class="row">
		<label class="col-xs-2 col-form-label">Variables *</label>
		<select id="listvar1" class="multiselect col-xs-4" multiple="multiple">""")
for i in range(0, len(variable_list)):
    for j in range(0, len(variables)):
        if variables[j]==variable_list[i]:
            variable_list[i]=0
    if variable_list[i]!=0:
        print('<option class="list-group-item">%s</option>' %variable_list[i])
print("""    
	</select>
		<div class="col-xs-1">
			<input id="button9" type="button" value=">>" />
			<br/>
			<input id="button10" type="button" value="<<" />
		</div>
		<select class="multiselect col-xs-4" id="listvar2" multiple="multiple" rows=2 name="variables" required>""")
for j in range(0, len(variables)):
    print('<option class="list-group-item">%s</option>' %variables[j])     
print("""    
		</select>
    </div>
	<script language="JavaScript">
		$(function(){
			$("#button9").click(function(){
				$("#listvar1 > option:selected").each(function(){
					$(this).remove().appendTo("#listvar2");
				});
			});
		})
		$(function(){
			$("#button10").click(function(){
				$("#listvar2 > option:selected").each(function(){
					$(this).remove().appendTo("#listvar1");
				});
			});
		})
	</script>
	</p>
</fieldset>
<fieldset>
	<p><h2> Constraints </h2></p>
	<p>
	<p>
	<div class="form-group row">
		<label for="access" class="col-xs-2 col-form-label">Access constraints *</label>
		<div class="col-xs-9">
		<select class="form-control" name="access">
""")
access_constraint=['Confidentiality Level 0: Public','Confidentiality Level 1: Public and traceability','Confidentiality Level 2: Restricted','Confidentiality Level 3: Case-by-case']
for i in range(0, len(access_constraint)):
    if access==access_constraint[i]:
        access_constraint[i]=0
    if access_constraint[i]!=0:
        
        print('<option>%s</option>' %access_constraint[i])
print('<option selected="selected">%s</option>' %access)
print("""
		</select>
		</div>
	</div>
	</p>
	<div class="form-group row">
		<label for="use" class="col-xs-2 col-form-label">Use limitation</label>
		<div class="col-xs-9">""")
print('<input class="form-control" type="text" name="use" value="%s">' %use_lim)
print("""    
		</div>
	</div>
	</p>
	<p>
	<div class="form-group row">
		<label for="citation" class="col-xs-2 col-form-label">Citation</label>
		<div class="col-xs-9">""")
print('<textarea class="form-control" name="citation" rows="3" >%s</textarea>' %citation)
print("""		</div>
	</div>
	</p>

</fieldset>
<fieldset>
<p>
	<h2> Contact</h2>
</p>
	<p>
	<div class="form-group row">
		<label for="geosys" class="col-xs-2 col-form-label">Owner of the data *</label>
		<div class="col-xs-9">
		<select class="form-control"  name="owner">""")
institution_list=['EOST/ IPGS','BRGM','ESG','GEIE']
for i in range(0, len(institution_list)):
    if owner1==institution_list[i]:
        institution_list[i]=0
    if institution_list[i]!=0:
        
        print('<option>%s</option>' %institution_list[i])
print('<option selected="selected">%s</option>' %owner1)
print("""
		</select>
		</div>
	</div>
	</p>
		<p>
	<div class="form-group row">
		<label for="geosys" class="col-xs-2 col-form-label">Distributor *</label>
		<div class="col-xs-9">
		<select class="form-control"  name="distributor">""")
for i in range(0, len(institution_list)):
    if owner1==institution_list[i]:
        institution_list[i]=0
    if institution_list[i]!=0:
        print('<option>%s</option>' %institution_list[i])
print('<option selected="selected">%s</option>' %distributor)
print("""
		</select>
		</div>
	</div>
	</p>
		<p>
	<div class="form-group row">
		<label for="geosys" class="col-xs-2 col-form-label">Resource contact *</label>
		<div class="col-xs-9">
		<select class="form-control"  name="resource">""")
for i in range(0, len(institution_list)):
    if owner1==institution_list[i]:
        institution_list[i]=0
    if institution_list[i]!=0:
        print('<option >%s</option>' %institution_list[i])
print('<option selected="selected">%s</option>' %resource_contact)
print("""
		</select>
		</div>
	</div>
	</p>
	  <p>
   </div>
  <center><button type="submit" class="btn btn-primary">Submit</button></center>
</p>
</fieldset>

</form>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

  </body>
</html>
""")
