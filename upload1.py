#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import XML_B2d2
import codecs
import csv
from string import Template


##############################################################
########## GET THE XML FILE FROM THE HTML FORM  ##############
#############################################################
form = cgi.FieldStorage()
message = form["path"].value

##############################################################
######### RUN THE PROGRAM THAT READ XML METADATA ############
#############################################################

DataID, DataLoc, DataTime, DataKeyword, DataQuality, DataPersonne = XML_B2d2.xml2B2d(message)


##############################################################
##################### FUNCTIONS  ############################
#############################################################

def java_button(button1, button2, list1, list2):
    button = """
	<script language="JavaScript">
		$(function(){
			$("#%s").click(function(){
				$("#%s > option:selected").each(function(){
					$(this).remove().appendTo("#%s");
				});
			});
		})
		$(function(){
			$("#%s").click(function(){
				$("#%s > option:selected").each(function(){
					$(this).remove().appendTo("#%s");
				});
			});
		})
		$(function(){
			$("select#%s").dblclick(function(){
				$("#%s > option:selected").each(function(){
					$(this).remove().appendTo("#%s");
				});
			});
		})
		$(function(){
			$("select#%s").dblclick(function(){
				$("#%s > option:selected").each(function(){
					$(this).remove().appendTo("#%s");
				});
			});
		})

	</script>""" %(button1,list1, list2, button2, list2, list1, list1, list1,
                list2, list2, list2, list1)
    return button


def java_date(datepicker, timepicker, namedate, nametime, valuedate, valuetime):
    date ="""			<div id="%s" class="col-xs-3 input-append date" >
				<input type="text" name="%s" value="%s"></input>
				<span class="add-on">
					<i data-date-icon="icon-calendar"></i>
				</span>
				<script type="text/javascript">
				  $('#%s').datetimepicker({
					format: 'yyyy-MM-dd',
					pickTime:false,
				  });
				</script>
			</div>
			<div id="%s" class="col-xs-3 input-append date" >
				<input type="text" name="%s" value="%s"></input>
				<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#%s').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>"""%(datepicker, namedate, valuedate, datepicker, 
                  timepicker, nametime, valuetime, timepicker)
    return date
    
def liste_deroulante(listvalues, realvalue):
    a = ''
    for i in range(0, len(listvalues)):
        if realvalue == listvalues[i][0]:
            listvalues[i][0] = 0
        if listvalues[i][0] != 0:
            a= a + """<option >%s</option>""" %listvalues[i][0]
    a= a + '<option selected="selected">%s</option>' %realvalue
    return a

def liste(liste_1, liste_2):
    list1 = ""
    list2 = ""
    for i in range(0, len(liste_1)):
        for j in range(0, len(liste_2)):
            if liste_2[j] == liste_1[i][0]:
                liste_1[i][0] = 0
        if liste_1[i][0] != 0:
           list1 = list1 + '<option class="list-group-item">%s</option>\n'%liste_1[i][0]
    for j in range(0, len(liste_2)):
        list2 = list2 + '<option class="list-group-item" selected>%s</option>\n' %liste_2[j]
    return list1, list2
 
##############################################################
###################### OPEN FILES  ##########################
#############################################################
file = open('Template_upload.html')

with open('Format.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    format1 = list(reader)
with open('Project_phase.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    Project_phase = list(reader)
with open('Subject_study.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    Subject_study = list(reader)
with open('Variable.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    Variable = list(reader)
with open('Contact.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    Contact = list(reader)
with open('Location.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    Location = list(reader)
with open('Confidentiality.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    Confidentiality = list(reader)

format_1, format_2 = liste(format1, DataQuality.format1)
subject1, subject2 = liste(Subject_study, DataKeyword.subject_study)
project1, project2 = liste(Project_phase, DataKeyword.project_phase)
location1, location2 = liste(Location, DataKeyword.location)
variable1, variable2 = liste(Variable, DataKeyword.variables)



 ##############################################################
################# Template processing  ########################
#############################################################   
temp = Template(file.read())
if DataTime.T3 ==1:
    radiotime1 = 'checked'
    radiotime2 = ''
    date1 = java_date('datepicker', 'timepicker1', 'startdate', 'starttime',
                      DataTime.t1, DataTime.h1)
    date2 = java_date('datepicker2', 'timepicker2', 'enddate', 'endtime',
                      DataTime.t2, DataTime.h2)
    date3 = java_date('datepicker3', 'timepicker3', 'date', 'time', 
                      '', '00:00:00')
else:
    radiotime1 = ''
    radiotime2 = 'checked'
    date1 = java_date('datepicker', 'timepicker1', 'startdate', 'starttime', 
                      '', '00:00:00')
    date2 = java_date('datepicker2', 'timepicker2', 'enddate', 'endtime',
                      '', '00:00:00')
    date3 = java_date('datepicker3', 'timepicker3', 'date', 'time', 
                      DataTime.t1, DataTime.h1)

if DataLoc.east == DataLoc.west and DataLoc.south == DataLoc.north:
    radiogeo1 = 'checked'
    radiogeo2 = ''
else:
    radiogeo1 = ''
    radiogeo2 = 'checked'
                        
format1_button = java_button('button1', 'button2', 'listformat1', 'listformat2')
subject_button = java_button('button3', 'button4', 'listsubj1', 'listsubj2')
project_button =  java_button('button5', 'button6', 'listproj1', 'listproj2')
location_button = java_button('button7', 'button8', 'listloc1', 'listloc2')
variable_button = java_button('button9', 'button10', 'listvar1', 'listvar2')

dataType_list = [['Dataset'], ['Series'], ['Services']]
datatype = liste_deroulante(dataType_list, DataID.data_type)
access = liste_deroulante(Confidentiality, DataQuality.access)
owner = liste_deroulante(Contact, DataPersonne.owner1)
distributor = liste_deroulante(Contact, DataPersonne.distributor)
contact = liste_deroulante(Contact, DataPersonne.resource_contact)
 ##############################################################
###################### DICTIONARY  ##########################
############################################################# 

d={'format1' : format_1, 'format2' : format_2, 'date1' : date1, 'date2' : date2,
   'date3' : date3, 'format1_button' : format1_button, 'radiogeo1' : radiogeo1,
   'radiogeo2' : radiogeo2, 'radiotime1' : radiotime1, 'radiotime2' : radiotime2,
   'subject1' : subject1, 'subject2' : subject2, 'subject_button' : subject_button,
   'project1' : project1, 'project2' : project2, 'project_button' : project_button,
   'location1' : location1.encode('ascii', 'xmlcharrefreplace'),
   'location2' : location2.encode('ascii', 'xmlcharrefreplace'), 'location_button' : location_button,
   'variable1' : variable1, 'variable2' : variable2, 'variable_button' : variable_button,
   'title' : DataID.title.decode('utf-8', 'ignore'), 'id_title' : DataID.ID_title,
   'abstract' : DataID.abstract.decode('utf-8', 'ignore'), 
   'datatype' : datatype, 'north' : DataLoc.north, 'south' : DataLoc.south,
   'east' : DataLoc.east, 'west' : DataLoc.west, 'depth1' : DataLoc.depth1,
   'depth2' : DataLoc.depth2, 'quality' : DataQuality.quality,
   'process' : DataQuality.process, 'access' : access,
   'use_lim' : DataQuality.use_lim, 
   'citation' : DataQuality.citation.decode('utf-8', 'ignore'), 'owner' : owner,
   'distributor' : distributor, 'contact' : contact}
   

print("Content-type: text/html; charset=utf-8\n")
print(temp.substitute(d))
#print(temp.substitute(d))
