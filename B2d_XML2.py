#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:15:57 2016

@author: Alice FREMAND
"""

def xml(DataID, DataLoc, DataTime, DataKeyword, DataQuality, DataPersonne):
    from lxml import etree
    import codecs
    from copy import deepcopy
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
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:otherConstraints/gco:CharacterString":
            access_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:applicationSchemaInfo/gmd:MD_ApplicationSchemaInformation/gmd:name/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:applicationSchemaInfo/gmd:MD_ApplicationSchemaInformation/gmd:name/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime":
            Creation_date1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL":
            url_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString":
            urlname_xml = e


    Title_xml.text = DataID.title.decode('utf-8')
    ID_title_xml.text = DataID.ID_title
    Title1_xml.text = DataID.title.decode('utf-8')
    Abstract_xml.text = DataID.abstract.decode('utf-8')
    root[10][0][0][0][0][0].attrib['codeListValue'] = DataID.data_type
    North_xml.text = str(DataLoc.north)
    East_xml.text = str(DataLoc.east)
    South_xml.text = str(DataLoc.south)
    West_xml.text = str(DataLoc.west)
    Depth1_xml.text = str(DataLoc.depth1)
    Depth2_xml.text = str(DataLoc.depth2)
    Date1_xml.text = DataTime.T1
    Date2_xml.text = DataTime.T2
    Creation_date_xml.text = DataTime.Creation_date
    Creation_date1_xml.text = DataTime.Creation_date
    url_xml.text = 'http://s-cdgp.u-strasbg.fr/CDGP-AAAI/comm.php?resource=%s' %DataID.ID_title
    urlname_xml.text = DataID.ID_title
    if DataLoc.depth1 =='no_deep':
        Depth_xml.getparent().remove(Depth_xml)
    else:
    	Depth1_xml.text = str(DataLoc.depth1)
    	Depth2_xml.text = str(DataLoc.depth2)


    Len_su = len(DataKeyword.subject_study)
    subject_study_xml.text = DataKeyword.subject_study[0]
    if Len_su > 1:
        for i in range(0, Len_su - 1):
            subject_study0_xml.getparent()[i].addnext(deepcopy(subject_study0_xml))
            subject_study0_xml.getparent()[i + 1][0].text = DataKeyword.subject_study[i + 1]

    Len_pro = len(DataKeyword.project_phase)
    project_phase_xml.text = DataKeyword.project_phase[0]
    if Len_pro > 1:
        for i in range(0, Len_pro - 1):
            project_phase0_xml.getparent()[i].addnext(deepcopy(project_phase0_xml))
            project_phase0_xml.getparent()[i + 1][0].text = DataKeyword.project_phase[i + 1]

    Len_loc = len(DataKeyword.location)
    location_xml.text = DataKeyword.location[0]
    if Len_loc > 1:
        for i in range(0, Len_loc - 1):
            location0_xml.getparent()[i].addnext(deepcopy(location0_xml))
            location0_xml.getparent()[i + 1][0].text = DataKeyword.location[i + 1]


    Len_var = len(DataKeyword.variables)
    variable_xml.text = DataKeyword.variables[0]
    if Len_var > 1:
        for i in range(0, Len_var - 1):
            variable0_xml.getparent()[i].addnext(deepcopy(variable0_xml))
            variable0_xml.getparent()[i + 1][0].text = DataKeyword.variables[i + 1]


    Len_for = len(DataQuality.format1)
    format1_xml.text =DataQuality.format1[0]
    if Len_var > 1:
        for i in range(0, Len_for - 1):
            format0_xml.getparent()[i].addnext(deepcopy(format0_xml))
            format0_xml.getparent()[i + 1][0].text = DataQuality.format1[i + 1]
    else:
        format1_xml.text = DataQuality.format1[0]

    if DataQuality.quality is not None:
        Quality_xml.text = DataQuality.quality.decode('utf-8')
    else:
        Quality_xml.getparent().remove(Quality_xml)		
    if DataQuality.process is not None:
        Process_step_xml.text = DataQuality.process.decode('utf-8')
    else:
        Process_step_xml.getparent().remove(Process_step_xml)	
    if DataQuality.use_lim is not None:
        Use_xml.text = DataQuality.use_lim.decode('utf-8')
    else:
        Use_xml.getparent().remove(Use_xml)	
    access_xml.text = DataQuality.access
    if DataQuality.citation is not None:
        Citation_xml.text = DataQuality.citation.decode('utf-8')
    else:
        Citation_xml.getparent().remove(Citation_xml)	

    condition_contact(DataPersonne.resource_contact, POC_Organisation_xml, POC_Adress_xml,
                      POC_City_xml, POC_Postalcode_xml, POC_Country_xml,
                      POC_email_xml, contact_list)
    condition_contact(DataPersonne.distributor, D_Organisation_xml, D_Adress_xml,
                      D_City_xml, D_Postalcode_xml, D_Country_xml, D_email_xml,
                      contact_list)
    condition_contact(DataPersonne.owner1, OW1_Organisation_xml, OW1_Adress_xml,
                      OW1_City_xml, OW1_Postalcode_xml, OW1_Country_xml,
                      OW1_email_xml, contact_list)

#    if DataPersonne.owner2 == 0:
#        OW1_xml.remove(OW1_xml[1])
#    if DataPersonne.owner1 == 0:
#        OW1_xml.remove(OW1_xml[0])
    doc.write('File/XML_temp.xml', xml_declaration=True, encoding = 'utf-8')


def condition_contact(type_contact, organisation, adress, city, post_code,
                      country, mail, contact_list):
    if type_contact == 'EOST/ IPGS':
        variable = 0
    elif type_contact == 'CDGP':
        variable = 1
    elif type_contact == 'BRGM':
        variable = 2
    elif type_contact == 'ESG':
        variable = 3
    elif type_contact == 'GEIE':
        variable = 4
    else:
        return
    organisation.text = contact_list[variable][0]
    adress.text = contact_list[variable][1]
    city.text = contact_list[variable][3]
    post_code.text = contact_list[variable][2]
    country.text = contact_list[variable][4]
    mail.text = contact_list[variable][5]
