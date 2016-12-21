# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:39:51 2016

@author: Standard
"""

import cgi, cgitb
import os
import B2d_XML2_excel
import xlrd, csv
import B2d_XML2_excel
from datetime import datetime
import shutil
from collections import defaultdict

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
            <li href='index.py'><a href='index.py'>Metadata implementation tool</a></li>
            <li><a href="upload.py">Uploading metadata</a></li>
			<li class="active" ><a href="excel.py">Excel tools</a></li>
			<li><a href="about.py">About</a></li>
            <li><a href="contact.py">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


        <h1><center>The XML files have been created</center></h1>
        <h2><center> Here is the list of your xml files</center></h2>
        <fieldset>
""")

cgitb.enable()
form = cgi.FieldStorage()
#filePath= form['path'].value
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
   
print("""
   <p>%s</p>
""" % (message,))

filePath='File/tmp/'+fn
mypath ='File/tmp/XML'
if not os.path.isdir(mypath):
   os.makedirs(mypath)

#xls_filelike = io.BytesIO(filePath)
#print(filePath)#io.BytesIO(filePath).read())
#Ouverture du fichier excel comportant les métadonnées
columns = defaultdict(list)
with open(filePath) as f:
    metadata_file=csv.reader(f, delimiter=';')#io.BytesIO(filePath),'r')
    next(metadata_file)
    for row in metadata_file:
        for (x,v) in enumerate(row):
            columns[x].append(v)


#Ouverture du fichier excel comportant les coordonnées géographiques des différents puits + keywords
location_file=xlrd.open_workbook('location.xlsx')
#print(location_file)
#Lecture de la feuille 1 du fichier excel

location_feuil=location_file.sheet_by_name('Feuil1')
Keyword_subj=location_file.sheet_by_name('subject')
Keyword_var=location_file.sheet_by_name('variable')
#Chargement des variables
#Donnees comprises dans la feuille Keyword
Keyword_subject0=Keyword_subj.col_values(0, start_rowx=0)
Keyword_variable0=Keyword_var.col_values(0, start_rowx=0)
Keyword_subject=Keyword_subj.col_values(1, start_rowx=0)
Keyword_variable=Keyword_var.col_values(1, start_rowx=0)
#Chargement des variables
#Donnees comprises dans la feuille 1
name=columns[1]
title=columns[2]
abstract=columns[3]
data_type=columns[5]
Geo_location=columns[7]
North=[]
South=[]
East=[]
West=[]

def geoloc(file, Location):
    global North, South, East, West
    for j in range(0, len(Location)):
        if file==Location[j]:
            North.append(location_feuil.cell_value(j+1, 1))
            South.append(location_feuil.cell_value(j+1, 2))
            West.append(location_feuil.cell_value(j+1,3))
            East.append(location_feuil.cell_value(j+1, 4))

Location_list=['EPS1', 'OPS4', '4550','4616','4601','GPK1', 'GPK2', 'GPK3','GPK4','Soultz-sous-Forêts' ]
for i in range(0,len(Geo_location)):
    geoloc(Geo_location[i],Location_list)
  
Depth1=columns[8]
Depth2=columns[9]
t1=columns[10]
t2=columns[11]
t3=columns[12]
creation_date=columns[13]
t11=[]
t22=[]
t33=[]
T1=[]
T2=[]
Creation_date1=[]
Creation_date=[]
for i in range(0, len(t1)):
    if t1[i]=='':
        t11.append('')
    else:
        dd,mm,yy=t1[i].split('/')
        t11.append(datetime(int(yy),int(mm),int(dd)))
        
    if t2[i]=='':
        t22.append('')
    else:
        dd,mm,yy=t2[i].split('/')
        t22.append(datetime(int(yy),int(mm),int(dd)))
        
    if t3[i]!='' and t2[i]!='':
        dd,mm,yy=t3[i].split('/')
        t33.append(datetime(int(yy),int(mm),int(dd)))
    else:
        t33.append('')
    Creation_date1.append(datetime(int(yy),int(mm),int(dd)))
    
for i in range(0, len(t11)):    
    if t22[i] !='':
        T1.append(t22[i].strftime("%Y-%m-%dT%H:%M:%S"))
        T2.append(t33[i].strftime("%Y-%m-%dT%H:%M:%S"))
    else:
        T1.append(t11[i].strftime("%Y-%m-%dT%H:%M:%S"))
        T2.append(t11[i].strftime("%Y-%m-%dT%H:%M:%S"))
    Creation_date.append(Creation_date1[i].strftime("%Y-%m-%dT%H:%M:%S"))


format1=columns[14]
quality=columns[15]
process=columns[16]
subject_Study=columns[17]
project_Phase=columns[18]
location=columns[19]
variables=columns[20]

for i in range (0, len(name)):
    if type(format1[i])==str:
        format1[i]=format1[i].split(';')
    if type(subject_Study[i])==str:        
        for j in range(0, len(Keyword_subject0)):
            subject_Study[i]=subject_Study[i].replace(Keyword_subject0[j], Keyword_subject[j])
        subject_Study[i]=subject_Study[i].split(';')
    if type(project_Phase[i])==str:
        project_Phase[i]=project_Phase[i].split(';')
    if type(location[i])==str:
        location[i]=location[i].replace('Soultz-sous-Forêts', 'Soultz-sous-Forêts (67250)')
        location[i]=location[i].split(';')
        location[i].append('Upper Rhine Graben')
        location[i].append('Alsace')
        location[i].append('France')
    else:
        location[i]=[str(location[i])]
    if type(variables[i])==str:
        for j in range(0, len(Keyword_variable0)):
            variables[i]=variables[i].replace(Keyword_variable0[j], Keyword_variable[j])
        variables[i]=variables[i].split(';')
        
        
access=columns[21]
use_lim=columns[22]
citation=columns[23]
owner1=columns[24]
owner2=columns[25]
resource_contact=columns[26]
distributor=columns[27]
for i in range(0, len(name)):
    print('<p>- %s <p>' %title[i])



for i in range(0, len(name)-1):
    B2d_XML2_excel.xml(title[i], abstract[i],data_type[i],North[i],East[i],South[i],West[i],Depth1[i],Depth2[i],T1[i],T2[i],Creation_date[i],subject_Study[i], project_Phase[i], location[i], variables[i], format1[i], quality[i],process[i], use_lim[i],access[i],citation[i], resource_contact[i], owner1[i], owner1[i], distributor[i],name[i])

shutil.make_archive('File/tmp/XML', 'zip', 'File/tmp/XML')
shutil.rmtree('File/tmp/XML')
print("""
    </fieldset>
    <form method="post" action="webapp1.py">
    <fieldset>
	<p>
	<h2> Zip file containing the created XML metadata </h2>
	</p>
 <h3>Click on the image logo to download the zip file:</h3>
 <a href="File/XML.zip" download="XML.zip"><center>
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
