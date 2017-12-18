#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:34:44 2017

@author: alice FREMAND
"""
import cgi
import cgitb; cgitb.enable()
import csv
from string import Template


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


def java_date(datepicker, timepicker, namedate, nametime):
    date ="""			<div id="%s" class="col-xs-3 input-append date" >
				<input type="text" name="%s" id="%s"/>
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
				<input type="text" name="%s" value="00:00:00"></input>
				<span class="add-on">
					<i data-time-icon="icon-time"></i>
				</span>
				<script type="text/javascript">
				  $('#%s').datetimepicker({
					format: 'hh:mm:ss',
					pickDate: false
				  });
				</script>"""%(datepicker, namedate, namedate, datepicker, 
                  timepicker, nametime, timepicker)
    
    return date

##############################################################
###################### OPEN FILES  ##########################
#############################################################
file = open('Template_index3.html')

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

 ##############################################################
################# Template processing  ########################
#############################################################   
temp = Template(file.read())
date1 = java_date('datepicker', 'timepicker1', 'startdate', 'starttime')
date2 = java_date('datepicker2', 'timepicker2', 'enddate', 'endtime')
date3 = java_date('datepicker3', 'timepicker3', 'date1', 'time')
    
format1_button = java_button('button1', 'button2', 'listformat1', 'listformat2')
subject_button = java_button('button3', 'button4', 'listsubj1', 'listsubj2')
project_button =  java_button('button5', 'button6', 'listproj1', 'listproj2')
location_button = java_button('button7', 'button8', 'listloc1', 'listloc2')
variable_button = java_button('button9', 'button10', 'listvar1', 'listvar2')

Format_to_replace=''
for i in range(0, len(format1)):
    Format_to_replace = Format_to_replace+'<option class="list-group-item">%s</option>\n' %format1[i][0]

Subject_to_replace = ''
for i in range(0, len(Subject_study)):
    Subject_to_replace = Subject_to_replace + '<option class="list-group-item">%s</option>\n' %Subject_study[i][0]
    
Project_to_replace = ''
for i in range(0, len(Project_phase)):
    Project_to_replace = Project_to_replace + '<option class="list-group-item">%s</option>\n' %Project_phase[i][0]
 
Location_to_replace = ''
for i in range(0, len(Location)):
    Location_to_replace = Location_to_replace + '<option class="list-group-item">%s</option>\n' %Location[i][0]

Variable_to_replace = ''
for i in range(0, len(Variable)):
    Variable_to_replace= Variable_to_replace + '<option class="list-group-item">%s</option>\n' %Variable[i][0]

Confidentiality_to_replace = ''
for i in range(0, len(Confidentiality)):
    Confidentiality_to_replace= Confidentiality_to_replace + '<option>%s</option>\n' %Confidentiality[i][0]

Contact_to_replace = ''
for i in range(0, len(Contact)):
    Contact_to_replace= Contact_to_replace + '<option>%s</option>\n' %Contact[i][0]

 ##############################################################
###################### DICTIONARY  ##########################
############################################################# 

d={'format1' : Format_to_replace, 'date1' : date1, 'date2' : date2,
   'date3' : date3, 'format1_button' : format1_button, 
   'Subject_study' : Subject_to_replace, 'subject_button' : subject_button,
   'Project_phase' : Project_to_replace, 'project_button' : project_button,
   'Location' : Location_to_replace.encode('ascii', 'xmlcharrefreplace'), 'location_button' : location_button,
   'Variable' : Variable_to_replace, 'variable_button' : variable_button,
   'Confidentiality' : Confidentiality_to_replace, 'Contact' : Contact_to_replace.encode('ascii', 'xmlcharrefreplace')}

print("Content-type: text/html; charset=utf-8\n")
print(temp.substitute(d))



