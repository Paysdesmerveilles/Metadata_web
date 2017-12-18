#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Oct  3 09:15:57 2016

@author: Alice FREMAND
"""
def xml(data, i):
    "The goal of this function is to fill the XML template (Metadata_template3.xml) with the information from the excel sheet (information that are gathered in a dictionary named 'data')"
    from lxml import etree
    from datetime import datetime
    from copy import deepcopy
    import codecs
    import csv
    with open('Contact.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        contact_list = list(reader) 

##############PROCESSING OF THE XML#########################

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


    Title_xml.text =data['title'][i]
    ID_title_xml.text = data['ID_title'][i]
    Title1_xml.text = data['title'][i]
    Abstract_xml.text = data['abstract'][i]
    root[10][0][0][0][0][0].attrib['codeListValue'] = data['datatype'][i]
    North_xml.text = str(data['north'][i])
    East_xml.text = str(data['east'][i])
    South_xml.text = str(data['south'][i])
    West_xml.text = str(data['west'][i])
    if 'Depth1' in data.keys():
        Depth1_xml.text = str(data['depth1'][i])
        Depth2_xml.text = str(data['depth2'][i])
    else:
        Depth_xml.getparent().remove(Depth_xml)        

    if isinstance(data["start_date"][i], str):
        t1 = data["start_date"][i]+ 'T' + '00:00:00'
    if isinstance(data["end_date"][i], str):
        t2 = data["end_date"][i] + 'T' +  '00:00:00'
        t3 = 1
    else:
        t2 = ''
        t3 = 0
    Date1_xml.text = t1
    Date2_xml.text = t2
    
    creadate = datetime.now().strftime('%Y-%m-%d')
    creatime = datetime.now().strftime('%H:%M:%S')
    creation_date = str(creadate)+'T'+str(creatime)    
    Creation_date_xml.text = creation_date
    Creation_date1_xml.text = creation_date
    
    url_xml.text = 'http://s-cdgp.u-strasbg.fr/CDGP-AAAI/comm.php?resource=%s' %data['ID_title'][i]
    urlname_xml.text = data['ID_title'][i]
    

    Len_su = len(data['subject_study'][i])
    if isinstance(data['subject_study'][i], list):
        subject_study_xml.text = data['subject_study'][i][0]
        for j in range(0, Len_su - 1):
            subject_study0_xml.getparent()[j].addnext(deepcopy(subject_study0_xml))
            subject_study0_xml.getparent()[j + 1][0].text = data['subject_study'][i][j + 1]
    else:
        temp = []
        temp.append(data['subject_study'][i])
        subject_study_xml.text =[data['subject_study'][i]][0]

    Len_pro = len(data['project_phase'][i])
    if isinstance(data['project_phase'][i], list):
        project_phase_xml.text = data['project_phase'][i][0]
        for j in range(0, Len_pro - 1):
            project_phase0_xml.getparent()[j].addnext(deepcopy(project_phase0_xml))
            project_phase0_xml.getparent()[j + 1][0].text = data['project_phase'][i][j + 1]
    else:
        temp = []
        temp.append(data['project_phase'][i])
        project_phase_xml.text =[data['project_phase'][i]][0]

    Len_loc = len(data['location'][i])
    if isinstance(data['location'][i], list):
        location_xml.text = data['location'][i][0]
        for j in range(0, Len_loc - 1):
            location0_xml.getparent()[j].addnext(deepcopy(location0_xml))
            location0_xml.getparent()[j + 1][0].text = data['location'][i][j + 1]
    else:
        temp = []
        temp.append(data['location'][i])
        location_xml.text =[data['location'][i]][0]


    Len_var = len(data['variables'][i])
    if isinstance(data['variables'][i], list):
        variable_xml.text = data['variables'][i][0]
        for j in range(0, Len_var - 1):
            variable0_xml.getparent()[j].addnext(deepcopy(variable0_xml))
            variable0_xml.getparent()[j + 1][0].text = data['variables'][i][j + 1]
    else:
        temp = []
        temp.append(data['variables'][i])
        variable_xml.text =[data['variables'][i]][0]


    Len_for = len(data['format1'][i])
    if isinstance(data['format1'][i], list):
        format1_xml.text =data['format1'][i][0]
        for j in range(0, Len_for - 1):
            format0_xml.getparent()[j].addnext(deepcopy(format0_xml))
            format0_xml.getparent()[j + 1][0].text = data['format1'][i][j + 1]
    else:
        temp = []
        temp.append(data['format1'][i])
        format1_xml.text =[data['format1'][i]][0]


    if 'quality' in data.keys():
        Quality_xml.text = data['quality'][i]
    else:
        Quality_xml.getparent().remove(Quality_xml)		
    if 'process' in data.keys():
        Process_step_xml.text = data['process'][i]
    else:
        Process_step_xml.getparent().remove(Process_step_xml)	
    if 'use' in data.keys():
        Use_xml.text = data['use'][i]
    else:
        Use_xml.getparent().remove(Use_xml)
    access_xml.text = data['access_constraint'][i]
    cite_xml.text = 'How to cite: '+ data['how_to_cite'][i]        
    if 'biblio' in data.keys():
        Citation_xml.text = 'References: ' + data['bibliography'][i]
    else:
        Citation_xml.getparent().remove(Citation_xml)
        

    condition_contact(data['resource_contact'][i], POC_Organisation_xml, POC_Adress_xml,
                      POC_City_xml, POC_Postalcode_xml, POC_Country_xml,
                      POC_email_xml, contact_list)
    condition_contact(data['distributor'][i], D_Organisation_xml, D_Adress_xml,
                      D_City_xml, D_Postalcode_xml, D_Country_xml, D_email_xml,
                      contact_list)
    condition_contact(data['owner1'][i], OW1_Organisation_xml, OW1_Adress_xml,
                      OW1_City_xml, OW1_Postalcode_xml, OW1_Country_xml,
                      OW1_email_xml, contact_list)
    if data['owner2'][i] != 'None':
        OW1_xml.getparent().addnext(deepcopy(OW1_xml.getparent()))
        condition_contact(data['owner2'][i], OW1_Organisation_xml, OW1_Adress_xml,
                      OW1_City_xml, OW1_Postalcode_xml, OW1_Country_xml,
                      OW1_email_xml, contact_list)

    doc.write('File/tmp/XML/%s.xml' %data['ID_title'][i], xml_declaration=True, encoding = 'utf-8')


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
