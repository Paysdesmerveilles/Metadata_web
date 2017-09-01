#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:59:44 2016

@author: Standard
"""
def xml2B2d(filePath):
    from lxml import etree
    import io
    class IdentityData:
        """Class that define data by:
            - its title
            -its abstract
            -its data type"""
    
        def __init__(self, title, ID_title, abstract, data_type):
            "Building the class"""
            self.title = title
            self.ID_title = ID_title
            self.abstract = abstract
            self.data_type = data_type
    
    class LocationData:
        """ Class that gives location information:
        -geographic coordinate system
        -North, SOuth, East, West
        -Depth"""
    
        def __init__(self, geosys, north, south, east, west):
            self.geosys = geosys
            self.north = north
            self.south = south
            self.east = east
            self.west = west

    class TimeData:
        """Class that gives information about time:
            -creation date of data
            -start time, end time of experiment"""
        def __init__(self, t1, t2, h1, h2, T3, Creation_date):
            self.t1 = t1
            self.t2 = t2
            self.h1 = h1
            self.h2 = h2
            self.T3 = T3
            self.Creation_date = Creation_date
    
    class KeywordData:
        """Class that gives information about keywords:
            - subject of study
            - project phase
            - location
            -variable"""
        def __init__(self, subject_study, project_phase, location, variables):
            self.subject_study = subject_study
            self.project_phase = project_phase
            self.location = location
            self.variables = variables
    
    class QualityData:
        """class that gives information about quality of data:
            -format1
            - quality
            - process
            - use_lim
            - access
            - citation"""
        def __init__(self, format1, quality, process, use_lim, access, citation):
            self.format1 = format1
            self.quality = quality
            self.process = process
            self.use_lim = use_lim
            self.access = access
            self.citation = citation
    
    class PersonneData:
        """"Clas that gives information about :
            - the distributor
            - the owner
            - the resource contact of the data """
    
        def __init__(self, resource_contact, owner1, owner2, distributor):
            self.resource_contact = resource_contact
            self.owner1 = owner1
            self.owner2 = owner2
            self.distributor = distributor


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
        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString":
            OW1_Adress_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString":
            OW1_City_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString":
            OW1_Postalcode_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gco:CharacterString":
            OW1_Country_xml = e
        elif tree.getpath(e) == ID + "gmd:pointOfContact[2]/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString":
            OW1_email_xml = e
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
        elif tree.getpath(e) == ID + "gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useLimitation/gco:CharacterString":
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
        elif tree.getpath(e) == ID + "gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:otherConstraints/gco:CharacterString":
            access_xml = e
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

    title = Title_xml.text.encode('ascii', 'xmlcharrefreplace')
    ID_title = ID_title_xml.text
    abstract = Abstract_xml.text.encode('ascii', 'xmlcharrefreplace')
    data_type = datatype_xml.attrib['codeListValue']
    DataID = IdentityData(title, ID_title, abstract, data_type)
    geosys = reference_xml.text
    East = float(East_xml.text)
    North = float(North_xml.text)
    South = float(South_xml.text)
    West = float(West_xml.text)
    DataLoc = LocationData(geosys, North, South, East, West)
    if 'Depth1_xml.text' in locals():
        DataLoc.Depth1 = float(Depth1_xml.text)   
        DataLoc.Depth2 = float(Depth2_xml.text)
    else:
        DataLoc.depth1 = ''
        DataLoc.depth2 = ''     
    
    Creation_date = Creation_date_xml.text
    T1 = Date1_xml.text
    (t1, h1) = T1.split('T')
    T2 = Date2_xml.text
    if isinstance(T2, str):
        [t2, h2] = T2.split('T')
        T3 = 1
    else:
        T3 = 0
        t2 = None
        h2 = None
    
    Subject_study = []
    Len_su = len(subject_study0_xml)
    for i in range(0, Len_su - 2):
        Subject_study.append(subject_study0_xml[i][0].text)

    Project_phase = []
    Len_pro = len(project_phase0_xml)
    for i in range(0, Len_pro - 2):
        Project_phase.append(project_phase0_xml[i][0].text)
    
    location = []
    Len_loc = len(location0_xml)
    for i in range(0, Len_loc - 2):
        location.append(location0_xml[i][0].text)
        
    variables = []
    Len_var = len(variable0_xml)
    for i in range(0, Len_var - 2):
        variables.append(variable0_xml[i][0].text)
    
    format1 = []
    Len_for = len(format0_xml)
    for i in range(0, Len_for - 1):
        format1.append(format0_xml[i][0].text)

    if 'Quality_xml' in locals():
        quality = Quality_xml.text.encode('ascii', 'xmlcharrefreplace')
    else:
        quality = ''
    if 'Process_step_xml' in locals():
        process = Process_step_xml.text.encode('ascii', 'xmlcharrefreplace')
    else:
        process = ''    
    if 'Use_xml.text' in locals():
        use_lim = Use_xml.text.encode('ascii', 'xmlcharrefreplace')
    else:
        use_lim = ''
    if 'Citation_xml' in locals():
        citation = Citation_xml.text.encode('ascii', 'xmlcharrefreplace')
    else:
        citation = ''

    access = access_xml.text
    citation = Citation_xml.text.encode('ascii', 'xmlcharrefreplace')

    owner1 = OW1_Organisation_xml.text
    owner2 = 0

    resource_contact = POC_Organisation_xml.text
    
    distributor = D_Organisation_xml.text
    
    DataTime = TimeData(t1, t2, h1, h2, T3, Creation_date)
    
    DataKeyword = KeywordData(Subject_study, Project_phase, location, variables)
    DataQuality = QualityData(format1, quality, process, use_lim, access, citation)
    DataPersonne = PersonneData(resource_contact, owner1, owner2, distributor)
    
    return DataID, DataLoc, DataTime, DataKeyword, DataQuality, DataPersonne
