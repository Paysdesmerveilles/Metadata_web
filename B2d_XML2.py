#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:15:57 2016

@author: Alice FREMAND
"""

def xml(data):
    from lxml import etree
    import codecs
    from copy import deepcopy
    from datetime import datetime
    import csv
    with open('Contact.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        contact_list = list(reader)

# The variables are uploadede via the online form index3.html

###############PROCESSING OF THE XML#########################

    doc = etree.parse('Metadata_template3.xml')
    root = doc.getroot()
    tree = etree.ElementTree(root)
    for e in root.iter():
        if tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            POC_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            POC_Adress_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            POC_City_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            POC_Postalcode_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            POC_email_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            POC_Country_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code/gco:CharacterString":
            reference_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:alternateTitle/gco:CharacterString":
            ID_title_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime":
            Creation_date_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:abstract/gco:CharacterString":
            Abstract_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            D_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            D_Adress_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            D_City_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            D_Postalcode_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            D_Country_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            D_email_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            OW1_Organisation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            OW1_Adress_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            OW1_City_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            OW1_Postalcode_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            OW1_Country_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            OW1_email_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty":
            OW1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[1]/gmd:MD_Keywords/gmd:keyword":
            subject_study0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[1]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            subject_study_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[2]/gmd:MD_Keywords/gmd:keyword":
            project_phase0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[2]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            project_phase_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[3]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            location_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[3]/gmd:MD_Keywords/gmd:keyword":
            location0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[4]/gmd:MD_Keywords/gmd:keyword":
            variable0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[4]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            variable_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useLimitation/gco:CharacterString":
            Use_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition":
            Date1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition":
            Date2_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]":
            Depth_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:minimumValue/gco:Real":
            Depth1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:maximumValue/gco:Real":
            Depth2_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal":
            West_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal":
            East_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal":
            South_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal":
            North_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:name":
            format0_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:name/gco:CharacterString":
            format1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement/gco:CharacterString":
            Quality_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:processStep/gmd:LI_ProcessStep/gmd:description/gco:CharacterString":
            Process_step_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:processStep/gmd:LI_ProcessStep/gmd:source/gmd:LI_Source/gmd:description/gco:CharacterString":
            Citation_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:scope/gmd:DQ_Scope/gmd:level/gmd:MD_ScopeCode":
            datatype_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:otherConstraints[1]/gco:CharacterString":
            access_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:otherConstraints[2]/gco:CharacterString":
            cite_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:applicationSchemaInfo/gmd:MD_ApplicationSchemaInformation/gmd:name/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:applicationSchemaInfo/gmd:MD_ApplicationSchemaInformation/gmd:name/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime":
            Creation_date1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL":
            url_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString":
            urlname_xml = e


    Title_xml.text =data['title']
    ID_title_xml.text = data['ID_title']
    Title1_xml.text = data['title']
    Abstract_xml.text = data['abstract']
    root[10][0][0][0][0][0].attrib['codeListValue'] = data['datatype']
    if data['radiotime'] == 'point':
        North_xml.text = str(data['longitude'])
        East_xml.text = str(data['latitude'])
        South_xml.text = str(data['longitude'])
        West_xml.text = str(data['latitude'])
    else:            
        North_xml.text = str(data['north'])
        East_xml.text = str(data['east'])
        South_xml.text = str(data['south'])
        West_xml.text = str(data['west'])
    if 'Depth1' in data.keys():
        Depth1_xml.text = str(data['depth1'])
        Depth2_xml.text = str(data['depth2'])
    else:
        Depth_xml.getparent().remove(Depth_xml)        

    if data['radiotime'] == 'extent':
        t1 = data["startdate"]+ 'T' + data['starttime']
        t2 = data["enddate"] + 'T' + data["endtime"]
        t3 = 1
    else:
        t1 = data["date1"]+ 'T' + data["time"]
        t2 = ''
        t3 = 0
    Date1_xml.text = t1
    Date2_xml.text = t2
    
    creadate = datetime.now().strftime('%Y-%m-%d')
    creatime = datetime.now().strftime('%H:%M:%S')
    creation_date = str(creadate)+'T'+str(creatime)    
    Creation_date_xml.text = creation_date
    Creation_date1_xml.text = creation_date
    
    url_xml.text = 'http://s-cdgp.u-strasbg.fr/CDGP-AAAI/comm.php?resource=%s' %data['ID_title']
    urlname_xml.text = data['ID_title']
    

    Len_su = len(data['subject'])
    if isinstance(data['subject'], list):
        subject_study_xml.text = data['subject'][0]
        for i in range(0, Len_su - 1):
            subject_study0_xml.getparent()[i].addnext(deepcopy(subject_study0_xml))
            subject_study0_xml.getparent()[i + 1][0].text = data['subject'][i + 1]
    else:
        temp = []
        temp.append(data['subject'])
        subject_study_xml.text =[data['subject']][0]

    Len_pro = len(data['project'])
    if isinstance(data['project'], list):
        project_phase_xml.text = data['project'][0]
        for i in range(0, Len_pro - 1):
            project_phase0_xml.getparent()[i].addnext(deepcopy(project_phase0_xml))
            project_phase0_xml.getparent()[i + 1][0].text = data['project'][i + 1]
    else:
        temp = []
        temp.append(data['project'])
        project_phase_xml.text =[data['project']][0]

    Len_loc = len(data['location'])
    if isinstance(data['location'], list):
        location_xml.text = data['location'][0]
        for i in range(0, Len_loc - 1):
            location0_xml.getparent()[i].addnext(deepcopy(location0_xml))
            location0_xml.getparent()[i + 1][0].text = data['location'][i + 1]
    else:
        temp = []
        temp.append(data['location'])
        location_xml.text =[data['location']][0]


    Len_var = len(data['variables'])
    if isinstance(data['variables'], list):
        variable_xml.text = data['variables'][0]
        for i in range(0, Len_var - 1):
            variable0_xml.getparent()[i].addnext(deepcopy(variable0_xml))
            variable0_xml.getparent()[i + 1][0].text = data['variables'][i + 1]
    else:
        temp = []
        temp.append(data['variables'])
        variable_xml.text =[data['variables']][0]


    Len_for = len(data['format'])
    if isinstance(data['format'], list):
        format1_xml.text =data['format'][0]
        for i in range(0, Len_for - 1):
            format0_xml.getparent()[i].addnext(deepcopy(format0_xml))
            format0_xml.getparent()[i + 1][0].text = data['format'][i + 1]
    else:
        temp = []
        temp.append(data['format'])
        format1_xml.text =[data['format']][0]


    if 'quality' in data.keys():
        Quality_xml.text = data['quality']
    else:
        Quality_xml.getparent().remove(Quality_xml)		
    if 'process' in data.keys():
        Process_step_xml.text = data['process']
    else:
        Process_step_xml.getparent().remove(Process_step_xml)	
    if 'use' in data.keys():
        Use_xml.text = data['use']
    else:
        Use_xml.getparent().remove(Use_xml)	
    access_xml.text = data['access']
    cite_xml.text = 'How to cite: '+ data['cite']        
    if 'biblio' in data.keys():
        Citation_xml.text = 'References: ' + data['biblio']
    else:
        Citation_xml.getparent().remove(Citation_xml)
        

    condition_contact(data['resource'], POC_Organisation_xml, POC_Adress_xml,
                      POC_City_xml, POC_Postalcode_xml, POC_Country_xml,
                      POC_email_xml, contact_list)
    condition_contact(data['distributor'], D_Organisation_xml, D_Adress_xml,
                      D_City_xml, D_Postalcode_xml, D_Country_xml, D_email_xml,
                      contact_list)
    condition_contact(data['owner'], OW1_Organisation_xml, OW1_Adress_xml,
                      OW1_City_xml, OW1_Postalcode_xml, OW1_Country_xml,
                      OW1_email_xml, contact_list)
    if data['owner2'] != 'None':
        OW1_xml.getparent().addnext(deepcopy(OW1_xml.getparent()))
        condition_contact(data['owner2'], OW1_Organisation_xml, OW1_Adress_xml,
                      OW1_City_xml, OW1_Postalcode_xml, OW1_Country_xml,
                      OW1_email_xml, contact_list)

    doc.write('File/XML_temp.xml', xml_declaration=True, encoding = 'utf-8')


def condition_contact(type_contact, organisation, adress, city, post_code,
                      country, mail, contact_list):
    for variable in range(0, len(contact_list)):
        if type_contact == contact_list[variable][0]:
            organisation.text = contact_list[variable][0]
            adress.text = contact_list[variable][1]
            city.text = contact_list[variable][3]
            post_code.text = contact_list[variable][2]
            country.text = contact_list[variable][4]
            mail.text = contact_list[variable][5]
