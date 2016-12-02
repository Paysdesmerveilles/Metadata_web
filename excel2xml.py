# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:39:51 2016

@author: Standard
"""

import cgi, cgitb
import B2d_XML2_excel
import io 
import xlrd
import B2d_XML2_excel
from datetime import datetime

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


        <h1><center>Succeed!! Here are the value you entered !</center></h1>
        <h2><center> Please check the value and validate to create your xml file</center></h2>
        <fieldset>
""")

cgitb.enable()
form = cgi.FieldStorage()
filePath= form['path'].value

#xls_filelike = io.BytesIO(filePath)
print(filePath)#io.BytesIO(filePath).read())
#Ouverture du fichier excel comportant les métadonnées

#metadata_file=xlrd.open_workbook(file_contents=filePath)#io.BytesIO(filePath),'r')
#
#
##Ouverture du fichier excel comportant les coordonnées géographiques des différents puits + keywords
#location_file=xlrd.open_workbook('location.xlsx')
#print(location_file)
#Lecture de la feuille 1 du fichier excel
#Data=metadata_file.sheet_by_name('Log')
#location_feuil=location_file.sheet_by_name('Feuil1')
#Keyword_subj=location_file.sheet_by_name('subject')
#Keyword_var=location_file.sheet_by_name('variable')
##Chargement des variables
##Donnees comprises dans la feuille Keyword
#Keyword_subject0=Keyword_subj.col_values(0, start_rowx=0)
#Keyword_variable0=Keyword_var.col_values(0, start_rowx=0)
#Keyword_subject=Keyword_subj.col_values(1, start_rowx=0)
#Keyword_variable=Keyword_var.col_values(1, start_rowx=0)
##Chargement des variables
##Donnees comprises dans la feuille 1
#name=Data.col_values(2, start_rowx=3)
#title=Data.col_values(3, start_rowx=3)
#abstract=Data.col_values(4, start_rowx=3)
#data_type=Data.col_values(6, start_rowx=3)
#Geo_location=Data.col_values(8, start_rowx=3)
#North=[]
#South=[]
#East=[]
#West=[]
#
#def geoloc(file, Location):
#    global North, South, East, West
#    for j in range(0, len(Location)):
#        if file==Location[j]:
#            North.append(location_feuil.cell_value(j+1, 1))
#            South.append(location_feuil.cell_value(j+1, 2))
#            West.append(location_feuil.cell_value(j+1,3))
#            East.append(location_feuil.cell_value(j+1, 4))
#
#Location_list=['EPS1', 'OPS4', 4550,4616,4601,'GPK1', 'GPK2', 'GPK3','GPK4','Soultz-sous-Forêts' ]
#for i in range(0,len(Geo_location)):
#    geoloc(Geo_location[i],Location_list)
#  
#Depth1=Data.col_values(9, start_rowx=3)
#Depth2=Data.col_values(10, start_rowx=3)
#t1=Data.col_values(11, start_rowx=3)
#t2=Data.col_values(12, start_rowx=3)
#t3=Data.col_values(13, start_rowx=3)
#creation_date=Data.col_values(14, start_rowx=3)
#t11=[]
#t22=[]
#t33=[]
#T1=[]
#T2=[]
#Creation_date1=[]
#Creation_date=[]
#for i in range(0, len(t1)):
#    if t1[i]=='':
#        t11.append('')
#    else:
#        t11.append(datetime(*xlrd.xldate_as_tuple(t1[i],0)))
#        
#    if t2[i]=='':
#        t22.append('')
#    else:
#        t22.append(datetime(*xlrd.xldate_as_tuple(t2[i],0)))
#        
#    if t3[i]!='' and t2[i]!='':
#        t33.append(datetime(*xlrd.xldate_as_tuple(t3[i],0)))
#    else:
#        t33.append('')
#    Creation_date1.append(datetime(*xlrd.xldate_as_tuple(creation_date[i],0)))
#    
#for i in range(0, len(t1)):    
#    if t2[i] !='':
#        T1.append(t22[i].strftime("%Y-%m-%dT%H:%M:%S"))
#        T2.append(t33[i].strftime("%Y-%m-%dT%H:%M:%S"))
#    else:
#        T1.append(t11[i].strftime("%Y-%m-%dT%H:%M:%S"))
#        T2.append(t11[i].strftime("%Y-%m-%dT%H:%M:%S"))
#    Creation_date.append(Creation_date1[i].strftime("%Y-%m-%dT%H:%M:%S"))
#
#
#format1=Data.col_values(15, start_rowx=3)
#quality=Data.col_values(16, start_rowx=3)
#process=Data.col_values(17, start_rowx=3)
#subject_Study=Data.col_values(18, start_rowx=3)
#project_Phase=Data.col_values(19, start_rowx=3)
#location=Data.col_values(20, start_rowx=3)
#variables=Data.col_values(21, start_rowx=3)
#for i in range (0, len(name)):
#    if type(format1[i])==str:
#        format1[i]=format1[i].split(';')
#    if type(subject_Study[i])==str:        
#        for j in range(0, len(Keyword_subject0)):
#            subject_Study[i]=subject_Study[i].replace(Keyword_subject0[j], Keyword_subject[j])
#        subject_Study[i]=subject_Study[i].split(';')
#    if type(project_Phase[i])==str:
#        project_Phase[i]=project_Phase[i].split(';')
#    if type(location[i])==str:
#        location[i]=location[i].replace('Soultz-sous-Forêts', 'Soultz-sous-Forêts (67250)')
#        location[i]=location[i].split(';')
#        location[i].append('Upper Rhine Graben')
#        location[i].append('Alsace')
#        location[i].append('France')
#    else:
#        location[i]=[str(location[i])]
#    if type(variables[i])==str:
#        for j in range(0, len(Keyword_variable0)):
#            variables[i]=variables[i].replace(Keyword_variable0[j], Keyword_variable[j])
#        variables[i]=variables[i].split(';')
#        
#        
#access=Data.col_values(22, start_rowx=3)
#use_lim=Data.col_values(23, start_rowx=3)
#citation=Data.col_values(24, start_rowx=3)
#owner1=Data.col_values(25, start_rowx=3)
#owner2=Data.col_values(26, start_rowx=3)
#resource_contact=Data.col_values(27, start_rowx=3)
#distributor=Data.col_values(28, start_rowx=3)
#for i in range(0, len(name)):
#    print(title[i])
#
#for i in range(0, len(name)):
#    B2d_XML2_excel.xml(title[i], abstract[i],data_type[i],North[i],East[i],South[i],West[i],Depth1[i],Depth2[i],T1[i],T2[i],Creation_date[i],subject_Study[i], project_Phase[i], location[i], variables[i], format1[i], quality[i],process[i], use_lim[i],access[i],citation[i], resource_contact[i], owner1[i], owner1[i], distributor[i],name[i])
#
##shutil.make_archive(XML, 'zip', File/XML)    
#html = open('excel2xml.html', 'r')
#print("Content-type: text/html; charset=utf-8\n")
#print(html.read())