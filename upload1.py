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

data = XML_B2d2.xml2B2d(message)


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

data['format1'], data['format2'] = liste(format1, data['forma'])
data['subject1'], data['subject2'] = liste(Subject_study, data['subj'])
data['project1'], data['project2'] = liste(Project_phase,data['proj'])
location1, location2 = liste(Location, data['loc'])
data['variable1'], data['variable2'] = liste(Variable, data['var'])

data['location1'] = location1.encode('ascii', 'xmlcharrefreplace')
data['location2'] = location2.encode('ascii', 'xmlcharrefreplace')

 ##############################################################
################# Template processing  ########################
#############################################################   
temp = Template(file.read())
if data['T3'] ==1:
    data['radiotime1'] = 'checked'
    data['radiotime2'] = ''
    data['date1'] = java_date('datepicker', 'timepicker1', 'startdate', 'starttime',
                      data['t1'], data['h1'])
    data['date2'] = java_date('datepicker2', 'timepicker2', 'enddate', 'endtime',
                      data['t2'], data['h2'])
    data['date3'] = java_date('datepicker3', 'timepicker3', 'date1', 'time', 
                      '', '00:00:00')
else:
    data['radiotime1'] = ''
    data['radiotime2'] = 'checked'
    data['date1'] = java_date('datepicker', 'timepicker1', 'startdate', 'starttime', 
                      '', '00:00:00')
    data['date2'] = java_date('datepicker2', 'timepicker2', 'enddate', 'endtime',
                      '', '00:00:00')
    data['date3'] = java_date('datepicker3', 'timepicker3', 'date1', 'time', 
                      data['t1'], data['h1'])

if data['east'] == data['west'] and data['south'] == data['north']:
    data['radiogeo1'] = 'checked'
    data['radiogeo2'] = ''
else:
    data['radiogeo1'] = ''
    data['radiogeo2'] = 'checked'
                        
data['format1_button'] = java_button('button1', 'button2', 'listformat1', 'listformat2')
data['subject_button'] = java_button('button3', 'button4', 'listsubj1', 'listsubj2')
data['project_button'] =  java_button('button5', 'button6', 'listproj1', 'listproj2')
data['location_button'] = java_button('button7', 'button8', 'listloc1', 'listloc2')
data['variable_button'] = java_button('button9', 'button10', 'listvar1', 'listvar2')

dataType_list = [['Dataset'], ['Series'], ['Services']]
data['datatype'] = liste_deroulante(dataType_list, data['data_type'])
data['access'] = liste_deroulante(Confidentiality, data['access1'])
owner = liste_deroulante(Contact, data['owner1'])
data['owner'] = owner.encode('ascii', 'xmlcharrefreplace')
if data['owner2'] == 'None':
    owner2 = liste_deroulante(Contact, data['owner2'])
    data['owner2'] = owner2.encode('ascii', 'xmlcharrefreplace')
else:
    owner2 = liste_deroulante(Contact, data['owner2']) + '<option >None</option>'
    data['owner2'] =  owner2.encode('ascii', 'xmlcharrefreplace')# + '<option >None</option>'
distributor = liste_deroulante(Contact, data['distributor1'])
data['distributor'] = distributor.encode('ascii', 'xmlcharrefreplace')
contact = liste_deroulante(Contact, data['resource_contact1'])
data['contact'] = contact.encode('ascii', 'xmlcharrefreplace')




print("Content-type: text/html; charset=utf-8\n")
print(temp.substitute(data))
#print(temp.substitute(d))



