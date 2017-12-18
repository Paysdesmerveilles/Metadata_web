#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:59:44 2016

@author: Standard
"""
def xml2B2d(filePath):
    from lxml import etree
    import io


    POC = "/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/"
    ID = "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/"
    loc = "/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/"
    doc = etree.parse(io.BytesIO(filePath))
    #    doc = etree.parse(filePath)
    root = doc.getroot()
    #Analyser le fichier xml pour remplacer les attributs voulus
    tree = etree.ElementTree(root)
    for e in root.iter():
        if tree.getpath(e) == POC + "gmd:organisationName/gco:CharacterString":
            POC_Organisation_xml = e
        elif tree.getpath(e) == POC + "gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            POC_Adress_xml = e
        elif tree.getpath(e) == POC + "gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            POC_City_xml = e
        elif tree.getpath(e) == POC + "gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            POC_Postalcode_xml = e
        elif tree.getpath(e) == POC + "gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            POC_email_xml = e
        elif tree.getpath(e) == POC + "gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            POC_Country_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code/gco:CharacterString":
            reference_xml = e
        elif tree.getpath(e) == ID + "gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title_xml = e
        elif tree.getpath(e) == ID + "gmd:citation/gmd:CI_Citation/gmd:alternateTitle/gco:CharacterString":
            ID_title_xml = e
        elif tree.getpath(e) == ID + "gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime":
            Creation_date_xml = e
        elif tree.getpath(e) == ID + "gmd:abstract/gco:CharacterString":
            Abstract_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            D_Organisation_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            D_Adress_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            D_City_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            D_Postalcode_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            D_Country_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[1]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            D_email_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            OW1_Organisation_xml = e
#        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
#            OW1_Adress_xml = e
#        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
#            OW1_City_xml = e
#        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
#            OW1_Postalcode_xml = e
#        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
#            OW1_Country_xml = e
#        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
#            OW1_email_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[3]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            OW2_Organisation_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[1]/gmd:MD_Keywords":
            subject_study0_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[1]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            subject_study_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[2]/gmd:MD_Keywords":#/gmd:keyword":
            project_phase0_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[2]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            project_phase_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[3]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            location_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[3]/gmd:MD_Keywords":#/gmd:keyword":
            location0_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[4]/gmd:MD_Keywords":#/gmd:keyword":
            variable0_xml = e
        elif tree.getpath(e) == ID + "gmd:descriptiveKeywords[4]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            variable_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useLimitation/gco:CharacterString":
            Use_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition":
            Date1_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition":
            Date2_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[2]":
            Depth_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:minimumValue/gco:Real":
            Depth1_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:maximumValue/gco:Real":
            Depth2_xml = e   
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format":#/gmd:name":
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
        elif tree.getpath(e) == ID + "gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:otherConstraints[1]/gco:CharacterString":
            access_xml = e
        elif tree.getpath(e) == ID + "gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:otherConstraints[2]/gco:CharacterString":
            cite_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:applicationSchemaInfo/gmd:MD_ApplicationSchemaInformation/gmd:name/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:applicationSchemaInfo/gmd:MD_ApplicationSchemaInformation/gmd:name/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime":
            Creation_date1_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL":
            url_xml = e
        elif tree.getpath(e) == "/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString":
            urlname_xml = e         
        elif tree.getpath(e) == ID + "gmd:extent[3]" + loc + "gmd:westBoundLongitude/gco:Decimal" or tree.getpath(e) == ID + "gmd:extent[2]" + loc + "gmd:westBoundLongitude/gco:Decimal":
            West_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[3]" + loc + "gmd:eastBoundLongitude/gco:Decimal" or tree.getpath(e) == ID + "gmd:extent[2]" + loc + "gmd:eastBoundLongitude/gco:Decimal":
            East_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[3]" + loc + "gmd:southBoundLatitude/gco:Decimal" or tree.getpath(e) == ID + "gmd:extent[2]" + loc + "gmd:southBoundLatitude/gco:Decimal":
            South_xml = e
        elif tree.getpath(e) == ID + "gmd:extent[3]" + loc + "gmd:northBoundLatitude/gco:Decimal" or tree.getpath(e) == ID + "gmd:extent[2]" + loc + "gmd:northBoundLatitude/gco:Decimal":
            North_xml = e 
#Remplisage du fichier xml pour chaque donnée
    
    data={}
    title = Title_xml.text.encode('ascii', 'xmlcharrefreplace')
    data['title'] = title.decode('utf-8', 'ignore')
    data['id_title'] = ID_title_xml.text
    data['abstract'] = Abstract_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    data['data_type'] = datatype_xml.attrib['codeListValue']

    data['geosys'] = reference_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    data['east'] = float(East_xml.text)
    data['north'] = float(North_xml.text)
    data['south'] = float(South_xml.text)
    data['west'] = float(West_xml.text)

    if 'Depth1_xml.text' in locals():
        data['depth1'] = float(Depth1_xml.text)   
        data['depth2'] = float(Depth2_xml.text)
    else:
        data['depth1'] = ''
        data['depth2'] = ''
    
    data['Creation_date'] = Creation_date_xml.text
    T1 = Date1_xml.text
    (data['t1'], data['h1']) = T1.split('T')
    T2 = Date2_xml.text
    if isinstance(T2, str):
        (data['t2'], data['h2']) = T2.split('T')
        data['T3'] = 1
    else:
        data['T3'] = 0
        data['t2'] = None
        data['h2'] = None
    
    data['subj'] = []
    Len_su = len(subject_study0_xml)
    for i in range(0, Len_su - 2):
        data['subj'].append(subject_study0_xml[i][0].text)

    data['proj'] = []
    Len_pro = len(project_phase0_xml)
    for i in range(0, Len_pro - 2):
        data['proj'].append(project_phase0_xml[i][0].text)
    
    data['loc'] = []
    Len_loc = len(location0_xml)
    for i in range(0, Len_loc - 2):
        data['loc'].append(location0_xml[i][0].text)
        
    data['var'] = []
    Len_var = len(variable0_xml)
    for i in range(0, Len_var - 2):
        data['var'].append(variable0_xml[i][0].text)
    
    data['forma'] = []
    Len_for = len(format0_xml)
    for i in range(0, Len_for - 1):
        data['forma'].append(format0_xml[i][0].text)

    if 'Quality_xml' in locals():
        data['quality'] = Quality_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    else:
        data['quality'] = ''
    if 'Process_step_xml' in locals():
        data['process'] = Process_step_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    else:
        data['process'] = ''    
    if 'Use_xml' in locals():
        data['use_lim'] = Use_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    else:
        data['use_lim'] = ''
    if 'Citation_xml' in locals():
        data['biblio'] = Citation_xml.text.lstrip('References:').encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    else:
        data['biblio'] = ''
    if 'access_xml' in locals():
        data['access1'] = access_xml.text
    else:
        data['access1'] = 'Confidentiality Level 0: Public'
    if 'cite_xml' in locals():
        data['cite'] = cite_xml.text.lstrip('How to cite:').encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    else:
        data['cite'] = ''
    data['resource_contact1'] = POC_Organisation_xml.text
    if 'OW2_Organisation_xml' in locals():
        data['owner2'] = OW1_Organisation_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
        data['owner1'] = OW2_Organisation_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    else:
        data['owner2'] = 'None'
        data['owner1'] = OW1_Organisation_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')
    data['distributor1'] = D_Organisation_xml.text.encode('ascii', 'xmlcharrefreplace').decode('utf-8', 'ignore')

    
    return data