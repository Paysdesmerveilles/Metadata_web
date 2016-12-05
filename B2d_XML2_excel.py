# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:15:57 2016

@author: Alice FREMAND
"""
def xml(title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1,T2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor, name):
    from lxml import etree
    from copy import deepcopy
    import csv
    with open('Contact.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        contact_list = list(reader) 
    #Changement de direction
    from os import chdir
    import matplotlib.pyplot as plt
    # Les variables sont chargés via le formulaire développé dans test5_widget.py
    # Le chargement 
    #Analyser le fichier xml pour remplacer les attributs voulus
    doc=etree.parse('Metadata_template3.xml')
    root=doc.getroot()
    tree = etree.ElementTree(root)
    for e in root.iter():
        if tree.getpath(e)=="/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            POC_Organisation_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            POC_Adress_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            POC_City_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            POC_Postalcode_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            POC_email_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            POC_Country_xml=e
#        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:dateStamp/gco:DateTime":
#            Creation_date_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code/gco:CharacterString":
            reference_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString":
            Title_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime":
            Creation_date_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:abstract/gco:CharacterString":
            Abstract_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:organisationName/gco:CharacterString":
            OW1_Organisation_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            OW1_Adress_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            OW1_City_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            OW1_Postalcode_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            OW1_Country_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[1]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            OW1_email_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]":
            OW1_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:organisationName/gco:CharacterString":
            OW2_Organisation_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            OW2_Adress_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            OW2_City_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            OW2_Postalcode_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            OW2_Country_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[1]/gmd:CI_ResponsibleParty[2]/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            OW2_email_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString":
            D_Organisation_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            D_Adress_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            D_City_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            D_Postalcode_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            D_Country_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            D_email_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[1]/gmd:MD_Keywords/gmd:keyword":
            subject_study0_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[1]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            subject_study_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[2]/gmd:MD_Keywords/gmd:keyword":
            project_phase0_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[2]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            project_phase_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[3]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            location_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[3]/gmd:MD_Keywords/gmd:keyword":
            location0_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[4]/gmd:MD_Keywords/gmd:keyword":
            variable0_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords[4]/gmd:MD_Keywords/gmd:keyword/gco:CharacterString":
            variable_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useLimitation/gco:CharacterString":
            Use_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition":
            Date1_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[1]/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition":           
            Date2_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:minimumValue/gco:Real":
            Depth1_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[2]/gmd:EX_Extent/gmd:verticalElement/gmd:EX_VerticalExtent/gmd:maximumValue/gco:Real":
            Depth2_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal":
            West_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal":
            East_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal":
            South_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent[3]/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal":     
            North_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:name":
            format0_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:name/gco:CharacterString":
            format1_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement/gco:CharacterString":           
            Quality_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:processStep/gmd:LI_ProcessStep/gmd:description/gco:CharacterString":
            Process_step_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:processStep/gmd:LI_ProcessStep/gmd:source/gmd:LI_Source/gmd:description/gco:CharacterString":
            Citation_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:dataQualityInfo[1]/gmd:DQ_DataQuality/gmd:scope/gmd:DQ_Scope/gmd:level/gmd:MD_ScopeCode":
            datatype_xml=e
        elif tree.getpath(e)=="/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:accessConstraints/gmd:MD_RestrictionCode":
            access_xml=e   
    
    print(name)
    #Remplisage du fichier xml pour chaque donnée
    
    Title_xml.text=title
    Abstract_xml.text=abstract
    root[10][0][0][0][0][0].attrib['codeListValue']=data_type
    North_xml.text=str(North)
    East_xml.text=str(East)
    South_xml.text=str(South)
    West_xml.text=str(West)
    Depth1_xml.text=str(Depth1)
    Depth2_xml.text=str(Depth2)
    Date1_xml.text=T1
    Date2_xml.text=T2
    Creation_date_xml.text=Creation_date
    
    Len_su=len(subject_Study)
    subject_study_xml.text=subject_Study[0]
    if Len_su>1:
        for i in range(0, Len_su-1):
            subject_study0_xml.getparent()[i].addnext(deepcopy(subject_study0_xml))
            subject_study0_xml.getparent()[i+1][0].text=subject_Study[i+1]         
    
    Len_pro=len(project_Phase)
    project_phase_xml.text=project_Phase[0]
    if Len_pro>1:
        for i in range(0, Len_pro-1):
            project_phase0_xml.getparent()[i].addnext(deepcopy(project_phase0_xml))
            project_phase0_xml.getparent()[i+1][0].text=project_Phase[i+1]   
    
    Len_loc=len(location)
    location_xml.text=location[0]
    if Len_loc>1:
        for i in range(0, Len_loc-1):
            location0_xml.getparent()[i].addnext(deepcopy(location0_xml))
            location0_xml.getparent()[i+1][0].text=location[i+1]
    
    
    Len_var=len(variables)
    variable_xml.text=variables[0]
    if Len_var>1:
        for i in range(0, Len_var-1):
            variable0_xml.getparent()[i].addnext(deepcopy(variable0_xml))
            variable0_xml.getparent()[i+1][0].text=variables[i+1]
    
    
    Len_for=len(format1)
    format1_xml
    format1_xml.text=format1[0]
    if Len_var>1:
        for i in range(0, Len_for-1):
            format0_xml.getparent()[i].addnext(deepcopy(format0_xml))
            format0_xml.getparent()[i+1][0].text=format1[i+1]
    else:
        format1_xml.text=format1[0]
    
    Quality_xml.text=quality
    Process_step_xml.text=process
    Use_xml.text=use_lim
    access_xml.attrib['codeListValue']=access
    Citation_xml.text=citation

    condition_contact(resource_contact,POC_Organisation_xml,POC_Adress_xml, POC_City_xml,POC_Postalcode_xml , POC_Country_xml, POC_email_xml, contact_list)
    condition_contact(distributor,D_Organisation_xml,D_Adress_xml, D_City_xml,D_Postalcode_xml , D_Country_xml, D_email_xml, contact_list)
    condition_contact(owner1,OW1_Organisation_xml,OW1_Adress_xml, OW1_City_xml,OW2_Postalcode_xml , OW1_Country_xml, OW1_email_xml, contact_list)
    condition_contact(owner2, OW2_Organisation_xml,OW2_Adress_xml, OW2_City_xml,OW2_Postalcode_xml , OW2_Country_xml, OW2_email_xml, contact_list)
    if owner2=='':
        OW1_xml.remove(OW1_xml[1])
    else:
        condition_contact(owner2, OW2_Organisation_xml,OW2_Adress_xml, OW2_City_xml,OW2_Postalcode_xml , OW2_Country_xml, OW2_email_xml, contact_list)
#    if owner1==0:
#        OW1_xml.remove(OW1_xml[0])      
    doc.write('File/XML/%s.xml' %name, xml_declaration=True)
    
    
def condition_contact(type_contact, organisation, adress, city, post_code, country, mail, contact_list):
    if type_contact=='EOST/ IPGS':
        variable=1
    elif type_contact=='BRGM':
        variable=2
    elif type_contact=='Es Géothermie':
        variable=3 
    elif type_contact=='GEIE':
        variable=4
    else:
        return
    organisation.text=contact_list[variable][0]
    adress.text=contact_list[variable][1]
    city.text=contact_list[variable][3]
    post_code.text=contact_list[variable][2]
    country.text=contact_list[variable][4]
    mail.text=contact_list[variable][5]
